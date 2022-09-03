import json

from pathlib import Path
from pyeditorjs import EditorJsParser


EXAMPLE_JSON = json.loads((Path(__file__).parent / 'example.json').read_text(encoding='utf-8'))
PARSER = EditorJsParser(content=EXAMPLE_JSON)



def test_parser():
    """
        Tests HTML rendering.
    """

    html = PARSER.html(True)

    print(html)
    (Path(__file__).parent / 'example.html').write_text(html + '\n', encoding='utf-8')



def test_extra():
    """
        Obtains text only from the blocks.

        WARNING: This does not sanitize the texts.
    """

    all_texts = []

    for block in PARSER:
        text = getattr(block, 'text', None)
        if text:
            all_texts.append(text)

    print(all_texts)


if __name__ == '__main__':
    test_parser()
    test_extra()
