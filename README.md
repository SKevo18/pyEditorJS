# pyEditorJS

A minimal, fast, Python 3.6+ package for parsing [Editor.js](https://editorjs.io) content.

## Features

- Handles all out-of-the-box Editor.js elements;
- Optional sanitization via the `bleach` library;
- Checks whether the data is valid (e. g.: a header can't have more than 6 levels), and raises `EditorJsParseError` if data is malformed;
- Uses Editor.js's class names for styles, so the output will be consistent with WYSIWYG (see [Editor.js's example style](https://github.com/codex-team/editor.js/blob/8ae8823dcd6877d63241fcb94694a8a18744485d/example/assets/demo.css) and [styles documentation](https://editorjs.io/styles))

## Installation

```bash
    pip install pyeditorjs
```

**Optional:** install [bleach](https://pypi.org/project/bleach) for clean HTML:

```bash
    pip install bleach
```

## Usage

### Quickstart

```python
from pyeditorjs import EditorJsParser

editor_js_data = ... # your Editor.js JSON data
parser = EditorJsParser(editor_js_data) # initialize the parser

html = parser.html(sanitize=True) # `sanitize=True` requires `bleach` to be installed
print(html) # your clean HTML
```

### Obtain texts only (for creating audio-only version, for example)

> **WARNING:** This does not sanitize the texts! Please, call `bleach.clean(...)` directly. This also doesn't obtain text from bold texts, markers, etc... - you should use [BeautifulSoup](https://pypi.org/project/beautifulsoup4/) for this.

```python
#import bleach
from pyeditorjs import EditorJsParser

editor_js_data = ... # your Editor.js JSON data
parser = EditorJsParser(editor_js_data) # initialize the parser

all_texts = []

for block in parser:
    text = getattr(block, 'text', None)

    if text:
        all_texts.append(text) # all_texts.append(bleach.clean(text))

print(all_texts)
```

## Disclaimer

This is a community-provided project, and is not affiliated with the Editor.js team.
It was created in my spare time. I cannot make sure that it will receive consistent updates.

Because of this, PRs, bug reports and suggestions are welcome!
