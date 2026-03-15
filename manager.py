from typing import TypedDict


def validate_password(password: str, min_len: int = 8) -> bool:
    return len(password) >= min_len


class EmailData(TypedDict):
    sender: str
    receivers: list[str]
    body: str


class EmailObject:
    """Represents an email message."""

    def __init__(self, sender: str, receivers: list[str], body: str) -> None:
        self.sender = sender
        self.receivers = receivers
        self.body = body

    @classmethod
    def create(cls, email: EmailData) -> "EmailObject":
        return cls(email["sender"], email["receivers"], email["body"])

    def _send_email(self, email: str) -> bool:
        pass

    def send_email(self) -> None:
        rec_str = "; ".join(self.receivers)
        email = f"sender: {self.sender} receiver: {rec_str} body: {self.body}"
        self._send_email(email)
