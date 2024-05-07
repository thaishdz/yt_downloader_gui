from tkinter import *


class ErrorMessageLabel:

    def __init__(self, parent, message=''):
        self.error_message_label = Label(parent, text=message)
        self.error_message_label.pack()


    def clean_error_message_label(self):
        self.error_message_label.destroy()