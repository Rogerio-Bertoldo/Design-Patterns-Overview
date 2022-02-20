import smtplib
from threading import Thread
from email.message import EmailMessage

from contract import Publisher, Subscriber
from events import Event


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
        email_thread = Thread(target=self.__sendEmail, args=(job,))
        email_thread.start()
            

    def __sendEmail(self, job: str):
        print(f"Sending email about {job} to {self.name}...")

        try:
            msg = EmailMessage()
            msg.set_content(f"Hello, {self.name}. A new job for {job} is available ;)")
            msg['Subject'] = f'New Job - {job}'
            msg['From'] = 'rogerionovoteste@gmail.com'
            msg['To'] = self.email
            s = smtplib.SMTP('localhost', port=8281)
            s.send_message(msg)
            s.quit()
            print(f"Email to {self.name} about {job} sent succesfully :)")
        except Exception as error:
            print(f"Failed to send email to {self.name} due to error: {error}")
