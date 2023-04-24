import tkinter
from tkinter import messagebox
import os

title = "Performance Booster"
message = "Are you sure that you want to boost your performance?"

confirm = tkinter.messagebox.askquestion(title=title, message=message)

message = "Your performance is boosted. Enjoy!"

if confirm == "yes":
    os.system('bootup.bat')
    tkinter.messagebox.showinfo(title=title, message=message)
