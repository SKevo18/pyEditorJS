import typing as t

from dataclasses import dataclass
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
    }
}



@dataclass
class EditorjsBlock:
    # TODO: Possible vulnerability: Decide whether or not to generate a new ID Python-side.
    # Using ID from JSON lets attacker to create a custom JSON and use already existing IDs to mess with the webpage.
    id: str

    @property
    def as_html(self) -> NotImplemented:
        return NotImplemented



@dataclass
class ParagraphData(EditorjsBlock):
    text: str


    @property
    def sanitized_text(self) -> str:
        return sanitize(self.text)


    @property
    def as_html(self) -> str:
        return f'<p id="{self.id}" class="mt-2 mb-2">{self.sanitized_text}</p>'



@dataclass
class HeaderData(ParagraphData):
    level: int

    @property
    def as_html(self) -> str:
        if not 1 <= self.level <= 6:
            raise BlockDataError(f'Header level must be between 1 and 6, not {self.level}.')


        return f'<h{self.level} id="{self.id}" class="{CLASSES["h"][self.level - 1]} mt-4 mb-2 font-sans">{super().as_html}</h{self.level}>'



@dataclass
class ListData(EditorjsBlock):
    style: t.Literal['unordered', 'ordered']
    items: t.List[str]


    @property
    def sanitized_items(self) -> t.List[str]:
        return [sanitize(item) for item in self.items]


    @property
    def as_html(self) -> str:
        if self.style != 'unordered' and self.style != 'ordered':
            raise BlockDataError(f'Invalid list style type: {self.style}')


        html = f'<ul id="{self.id}" class="{CLASSES["ul"][self.style]} ml-10 marker:font-bold mt-2 mb-2">\n'
        for item in self.sanitized_items:
            html += f'\t<li>{item}</li>\n'
        html += "</ul>"


        return html


# TODO: Could be possibly handled more elegantly:
def convert_to_block(raw: dict) -> t.Optional[t.Type[EditorjsBlock]]:
    type = raw.get("type", None)

    if type == 'paragraph':
        return ParagraphData(
            id=raw['id'],
            text=raw['data']['text']
        )
    
    elif type == 'header':
        return HeaderData(
            id=raw['id'],
            text=raw['data']['text'],
            level=raw['data']['level']
        )

    elif type == 'list':
        return ListData(
            id=raw['id'],
            style=raw['data']['style'],
            items=raw['data']['items']
        )


    return None
