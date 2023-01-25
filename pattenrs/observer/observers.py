from abc import ABC, abstractmethod

class WindowObserver(ABC):
    @abstractmethod
    def action(self):
        pass


class MessageAction(WindowObserver):
    def action(self):
        print("Printing a message")


class EmailAction(WindowObserver):
    def action(self):
        print("Sending email")


class FtpAction(WindowObserver):
    def action(self):
        print("Sending data via FTP")