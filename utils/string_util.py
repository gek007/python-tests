def capitalize(s: str) -> str:
    if len(s) <= 1:
        return s.upper()

    return s[0].upper() + s[1:]
