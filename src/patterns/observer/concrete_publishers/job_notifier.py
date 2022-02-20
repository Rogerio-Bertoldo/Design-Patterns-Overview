from events import Event
from typing import List
from contract import Publisher, Subscriber

class JobNotifier(Publisher):
    def __init__(self) -> None:
        self.subscribers: List[dict] = []


    def subscribe(self, observer: Subscriber, event: Event) -> None:
        #TODO Create class to store both the event and observer
        self.subscribers.append({"event": event, "observer": observer})


    def unsubscribe(self, observer: Subscriber, event: Event) -> None:

        #TODO Optimize loop
        for sub in self.subscribers:
            if sub.get("event").name == event.name and sub.get("observer") == observer:
                self.subscribers.remove(sub)
                print(f"Observer removed")
                break

    def notify(self, job) -> None:

        for observer in filter(lambda item: item.get("event").name == job, self.subscribers):
            observer.get("observer").update(job)

    def addNewJob(self, job:str):
        self.notify(job)


    