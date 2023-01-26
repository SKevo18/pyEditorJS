from pathlib import Path

import sys

sys.path.append(".")

import setuptools


__description__ = "pyEditorJS"
__author__ = "SKevo"
__copyright__ = "Copyright (c) 2022, SKevo"
__credits__ = ["SKevo"]
__license__ = "MIT"
__version__ = "v1.0.0-beta"
__maintainer__ = "SKevo"
__email__ = "skevo.cw@gmail.com"
__status__ = "4 - Beta"


README_PATH = Path(__file__).parent.absolute() / Path("README.md")

try:
    with open(README_PATH, "r", encoding="utf-8") as readme:
        __readme__ = readme.read()

except Exception:
    __readme__ = "Failed to read README.md!"

__doc__ = __readme__


setuptools.setup(
    name="pyeditorjs",
    packages=setuptools.find_packages(exclude=("tests",)),
    long_description=__readme__,
    long_description_content_type="text/markdown",
    version=__version__,
    license=__license__,
    description=__description__,
    keywords=[
        "editor.js",
        "parser",
        "clean",
        "bleach",
        "wysiwyg",
        "editor",
        "javascript",
        "html",
        "json",
    ],
    author=__author__,
    author_email=__email__,
    url="https://github.com/CWKevo/pyEditorJS",
    install_requires=[],
    classifiers=[
        f"Development Status :: {__status__}",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
