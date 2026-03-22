from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, message: str) -> None:
        pass


class EmailNotifier(Observer):
    def update(self, message: str) -> None:
        print(f"EmailNotifier: {message}")


email_notifier = EmailNotifier()
email_notifier.update("Hello, world!")
