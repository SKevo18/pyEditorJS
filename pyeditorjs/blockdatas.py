import typing as t

import string
from random import choice

from dataclasses import dataclass, field
from bleach import clean, linkify
from bleach.sanitizer import ALLOWED_TAGS

class BlockDataError(Exception): pass

def sanitize(string: str) -> str:
    return clean(linkify(string), tags=ALLOWED_TAGS + ['mark'])


CLASSES = {
    'h': [
        'text-3xl font-extrabold',
        'text-2xl font-bold',
        'text-xl',
        'text-lg',
        'text-md',
        'text-base italic'
    ],
    'ul': {
        'ordered': 'list-decimal',
        'unordered': 'list-disc'
    },
    'figure': 'text-center rounded-lg',
    'img': 'mx-auto',
    'figcaption': 'italic py-2'
}



@dataclass
class EditorjsBlock:
    # TODO: Possible vulnerability: Decide whether or not to generate a new ID just Python-side.
    # Using ID from JSON lets attacker to create a custom JSON and use already existing IDs to mess with the webpage.
    id: str = ''.join(choice(string.ascii_letters + string.digits) for _ in range(10))

    @property
    def as_html(self) -> NotImplemented:
        return NotImplemented



@dataclass
class ParagraphBlock(EditorjsBlock):
    text: str = ''


    @property
    def sanitized_text(self) -> str:
        return sanitize(self.text)


    @property
    def as_html(self) -> str:
        return f'<p id="{self.id}" class="mt-2 mb-2">{self.sanitized_text}</p>'



@dataclass
class HeaderBlock(ParagraphBlock):
    level: int = 5

    @property
    def as_html(self) -> str:
        if not 1 <= self.level <= 6:
            raise BlockDataError(f'Header level must be between 1 and 6, not {self.level}.')


        return f'<h{self.level} id="{self.id}" class="{CLASSES["h"][self.level - 1]} mt-4 mb-2 font-sans">{super().as_html}</h{self.level}>'



@dataclass
class ListBlock(EditorjsBlock):
    style: t.Literal['unordered', 'ordered'] = 'unordered'
    items: t.List[str] = field(default_factory=list)


    @property
    def sanitized_items(self) -> t.List[str]:
        return [sanitize(item) for item in self.items]


    @property
    def as_html(self) -> str:
        if self.style != 'unordered' and self.style != 'ordered':
            raise BlockDataError(f'Invalid list style type: {self.style}')

        if len(self.items) <= 0:
            raise BlockDataError("Empty list.")


        html = f'<ul id="{self.id}" class="{CLASSES["ul"][self.style]} ml-10 marker:font-bold mt-2 mb-2">\n'
        for item in self.sanitized_items:
            html += f'\t<li>{item}</li>\n'
        html += "</ul>"


        return html



@dataclass
class DelimiterBlock(EditorjsBlock):
    @property
    def as_html(self):
        return f'<p id="{self.id}" class="text-3xl text-center pt-6 pb-2">* * *</p>'



@dataclass
class ImageBlock(EditorjsBlock):
    file_url: str = None
    caption: str = ''
    withBorder: bool = False
    stretched: bool = False
    withBackground: bool = False


    @property
    def as_html(self) -> str:
        if not self.file_url:
            raise BlockDataError('Missing file URL for ImageData.')

        return f'<figure id="{self.id}" class="{CLASSES["figure"]} {"bg-indigo-200" if self.withBackground else ""}">' +\
                    f'<img class="{CLASSES["img"]} {"border-indigo-100" if self.withBorder else ""} {"max-w-none" if self.stretched else ""} {"w-4/6" if self.withBackground else ""}" src="{self.file_url}" alt="{self.caption}">' +\
                    (f'<figcaption class="{CLASSES["figcaption"]}">{self.caption}</figcaption>' if len(self.caption) > 0 else '') +\
                '</figure>'



# TODO: Could be possibly handled more elegantly:
def convert_to_block(raw: dict) -> t.Optional[t.Type[EditorjsBlock]]:
    type = raw.get("type", None)

    if type == 'paragraph':
        return ParagraphBlock(
            id=raw['id'],
            text=raw['data']['text']
        )
    
    elif type == 'header':
        return HeaderBlock(
            id=raw['id'],
            text=raw['data']['text'],
            level=raw['data']['level']
        )

    elif type == 'list':
        return ListBlock(
            id=raw['id'],
            style=raw['data']['style'],
            items=raw['data']['items']
        )

    elif type == 'image':
        return ImageBlock(
            id=raw['id'],
            file_url=raw['data']['file']['url'], # TODO: What if it's base64 encoded? Should probably use *.get() to do conditional check and handle both cases
            caption=raw['data']['caption'],
            withBorder=raw['data']['withBorder'],
            stretched=raw['data']['stretched'],
            withBackground=raw['data']['withBackground']
        )
    
    elif type == 'delimiter':
        return DelimiterBlock()


    return None
