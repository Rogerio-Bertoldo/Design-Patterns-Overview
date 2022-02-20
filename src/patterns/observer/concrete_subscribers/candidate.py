import sys

from contract import Publisher, Subscriber
from events import Event
from utils.smtp_integrator import SMTPIntegrator


class Candidate(Subscriber):
    def __init__(self, name: str, job: str, email: str) -> None:
        self.name = name
        self.job = job
        self.email = email

    def setAlert(self, notifier: Publisher, event: Event) -> None:
        notifier.subscribe(observer=self, event=event)

    def removeAlert(self, notifier: Publisher, event: Event) -> None:
        notifier.unsubscribe(observer=self, event=event)

    def update(self, job: str) -> None:
        SMTPIntegrator().sendEmail(
            subject=f'New Job - {job}',
            content=f"Hello, {self.name}. A new job for {job} is available ;)",
            destEmail=self.email
        )
