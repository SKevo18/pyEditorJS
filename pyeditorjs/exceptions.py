__all__ = ["EditorJsParseError"]


class EditorJsParseError(Exception):
    """Raised when a parse error occurs (example: the JSON data has invalid or malformed content)."""
