from abc import ABC, abstractmethod
class Notification(ABC):
    @abstractmethod
    def send(self,message):
        pass
class EmailNotification(Notification):
    def send(self,message):
        print(f"Sending Email: {message}")
class SMSNotification(Notification):
    def send(self,message):
        print(f"Sending SMS : {message}")
class PushNotification(Notification):
    def send(self,message):
        print(f"Sending Push Notification: {message}")

email = EmailNotification()
sms = SMSNotification()
push = PushNotification()
email.send("Hello Prasanna, hope you are doing well")
sms.send("Hey Prasanna, what's up?")
push.send("hola Prasanna, khana kha liya kya?")
class NotificationService :
    def __init__(self):
        self.notifications = []
    def add_notification(self,notification):
        self.notifications.append(notification)
    def send_to_all(self,message):
        for notifiaction in self.notifications :
            notifiaction.send(message)
service = NotificationService()
service.add_notification(EmailNotification())
service.add_notification(SMSNotification())   
service.add_notification(PushNotification())
service.send_to_all("Hello Prasanna, hope you are doing well")
