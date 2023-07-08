import typing as t

from dataclasses import dataclass


from .exceptions import EditorJsParseError
from .blocks import *


@dataclass
class EditorJsParser:
    """
    An Editor.js parser.
    """

    content: dict
    """The JSON data of Editor.js content."""

    def __post_init__(self) -> None:
        if not isinstance(self.content, dict):
            raise EditorJsParseError(
                f"Content must be `dict`, not {type(self.content).__name__}"
            )

    @staticmethod
    def _get_block(data: dict) -> t.Optional[EditorJsBlock]:
        """
        Obtains block instance from block data.
        """

        BLOCKS_MAP: t.Dict[str, t.Type[EditorJsBlock]] = {
            "header": HeaderBlock,
            "paragraph": ParagraphBlock,
            "list": ListBlock,
            "delimiter": DelimiterBlock,
            "code": CodeBlock,
            "quote": QuoteBlock,
            "media": MediaBlock,
            "raw": RawBlock,
            "embed": EmbedBlock
        }

        _type = data.get("type", None)

        try:
            return BLOCKS_MAP[_type](_data=data)

        except KeyError:
            return None

    def blocks(self) -> t.List[t.Type[EditorJsBlock]]:
        """
        Obtains a list of all available blocks from the editor's JSON data.
        """

        all_blocks: t.List[t.Type[EditorJsBlock]] = []
        blocks = self.content.get("blocks", [])

        if not isinstance(blocks, list):
            raise EditorJsParseError(
                f"Blocks is not `list`, but `{type(blocks).__name__}`"
            )

        for block_data in blocks:
            block = self._get_block(data=block_data)
            if block is None:
                continue

            all_blocks.append(block)

        return all_blocks

    def __iter__(self) -> t.Iterator[t.Type[EditorJsBlock]]:
        """Returns `iter(self.blocks())`"""

        return iter(self.blocks())

    def html(self, sanitize: bool = False) -> str:
        """
        Renders the editor's JSON content as HTML.

        ### Parameters:
        - `sanitize` - whether to also sanitize the blocks' texts/contents.
        """

        return "\n".join([block.html(sanitize=sanitize) for block in self.blocks()])
