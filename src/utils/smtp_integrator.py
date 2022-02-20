import os
import smtplib
from email.message import EmailMessage
from threading import Thread

from patterns.singleton.singleton import Singleton


class SMTPIntegrator(metaclass=Singleton):
    defaultMailer: str

    def __init__(self) -> None:
        try:
            self.mailer = os.environ.get("SMTP_MAIL_ADDRESS")
            self.host = os.environ.get("SMTP_HOST")
            self.port = os.environ.get("SMTP_PORT")
            del os.environ["SMTP_MAIL_ADDRESS"]
            del os.environ["SMTP_HOST"]
            del os.environ["SMTP_PORT"]
        except Exception as error:
            print(f"Failed to setup default mailer due to error: {error}")

    def sendEmail(self, subject: str, content: str, destEmail: str):
        email_thread = Thread(target=self.__sendEmail, args=(subject,content,destEmail))
        email_thread.start()
        


    def __sendEmail(self, subject: str, content: str, destEmail: str):
        print(f"Sending email '{subject}' to {destEmail}...")

        try:
            msg = EmailMessage()
            msg.set_content(content)
            msg['Subject'] = subject
            msg['From'] = self.mailer
            msg['To'] = destEmail
            s = smtplib.SMTP(self.host, port=self.port)
            s.send_message(msg)
            s.quit()
            print(f"Email '{subject}' to {destEmail} sent succesfully :)")
        except Exception as error:
            print(f"Failed to send email to {destEmail} due to error: {error}")