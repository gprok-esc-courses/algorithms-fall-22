import tkinter as tk
from observers import MessageAction, EmailAction, FtpAction

class Window:
    def __init__(self):
        self.observers = []
        self.win = tk.Tk()
        self.win.geometry("300x300")

        label = tk.Label(text="Observer Pattern")
        label.pack()

        btn = tk.Button(text="Click Me", command=self.btn_event)
        btn.pack()

    def start(self):
        self.win.mainloop()

    def register_observer(self, observer):
        self.observers.append(observer)

    def btn_event(self):
        print("==========================")
        for obs in self.observers:
            obs.action()

w = Window()
w.register_observer(MessageAction())
w.register_observer(EmailAction())
w.register_observer(FtpAction())
w.start()




