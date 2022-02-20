from abc import ABC, abstractmethod
from events import Event

class Publisher(ABC):

    @abstractmethod
    def subscribe(self, observer: "Subscriber", event: Event) -> None:
        pass

    @abstractmethod
    def unsubscribe(self, observer: "Subscriber", event: Event) -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass


class Subscriber(ABC):
    @abstractmethod
    def update(self, job: str) -> None:
        pass


