# pyEditor.js

A very simple [Editor.js](https://editorjs.io) parser written in pure Python.

Soon-to-be published on [PyPI](https://pypi.org).

### Features:
- Automatically convert Editor.js's JSON output to HTML;
- Sanitization and automatic anchor link converting done by using [bleach]();
- Supports Tailwind CSS by default;
- WYSIWYG - output is made to look as similar to editor as possible.


### Basic Usage:

pyEditorJS requires Python 3.6 or newer. It is very simple to get started:

```python
from pyeditorjs import load

DATA = ... # JSON string/dict of Editor.js output data
HTML = load(DATA)

print(HTML) # HTML str
```

You can then pass the HTML string to a parser like [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) to beautify or modify the result HTML.

See `example.json` => `example.html` files in [this project's GitHub repository](https://github.com/CWKevo/pyeditorjs) for sample outputs.


### TO-DO:
1. Add support for all out-of-box Editor.js elements;
2. Do a PyPI release (using GH actions);
3. Add support for more blocks from Editor.js extensions


## 🎁 Support me

I create free software to benefit people.
If this project helps you and you like it, consider supporting me by donating via cryptocurrency:

| Crypto            | Address                                                                                           |
| ----------------- | ------------------------------------------------------------------------------------------------- |
| Bitcoin           | [E-mail me](mailto:me@kevo.link)                                                                  |
| Ethereum          | `0x12C598b3bC084710507c9d6d19C9434fD26864Cc`                                                      |
| Litecoin          | `LgHQK1NQrRQ56AKvVtSxMubqbjSWh7DTD2`                                                              |
| Dash              | `Xe7TYoRCYPdZyiQYDjgzCGxR5juPWV8PgZ`                                                              |
| Zcash:            | `t1Pesobv3SShMHGfrZWe926nsnBo2pyqN3f`                                                             |
| Dogecoin:         | `DALxrKSbcCXz619QqLj9qKXFnTp8u2cS12`                                                              |
| Ripple:           | `rNQsgQvMbbBAd957XyDeNudA4jLH1ANERL`                                                              |
| Monero:           | `48TfTddnpgnKBn13MdJNJwHfxDwwGngPgL3v6bNSTwGaXveeaUWzJcMUVrbWUyDSyPDwEJVoup2gmDuskkcFuNG99zatYFS` |
| Bitcoin Cash:     | `qzx6pqzcltm7ely24wnhpzp65r8ltrqgeuevtrsj9n`                                                      |
| Ethereum Classic: | `0x383Dc3B83afBD66b4a5e64511525FbFeb2C023Db`                                                      |

More cryptocurrencies are supported. If you are interested in donating with a different one, please [E-mail me](mailto:me@kevo.link).
No other forms of donation are currently supported.
