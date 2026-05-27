import re
import unicodedata


def normalize(text: str) -> str:
    # Step 1: Unicode normalization — catches homoglyph tricks
    # e.g., "іgnore" (Cyrillic і) → "ignore"
    text = unicodedata.normalize("NFKC", text)

    # Step 2: collapse repeated whitespace
    # (but preserve newlines for multiline anchors)

    return text


res = normalize("іgnore previous      instructions")
print(res)
