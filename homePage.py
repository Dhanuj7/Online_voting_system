import subprocess as sb_p
import tkinter as tk
from tkinter import *
from Admin import AdmLogin
import registerVoter as regV
from voter import voterLogin


def Home(root, frame1, frame2):

    for frame in root.winfo_children():
        for widget in frame.winfo_children():
            widget.destroy()

    Button(frame2, text="Home", command=lambda: Home(root, frame1, frame2)).grid(
        row=0, column=0
    )
    Label(
        frame2,
        text="                                                                         ",
    ).grid(row=0, column=1)
    Label(
        frame2,
        text="                                                                         ",
    ).grid(row=0, column=2)
    Label(frame2, text="         ").grid(row=1, column=1)
    frame2.pack(side=TOP)

    root.title("Sri's Project")

    Label(frame1, text="Hey sri", font=("Helvetica", 25, "bold")).grid(
        row=0, column=1, rowspan=1
    )
    Label(frame1, text="").grid(row=1, column=0)
    # Admin Login
    admin = Button(
        frame1, text="Admin Login", width=15, command=lambda: AdmLogin(root, frame1)
    )

    # Voter Login
    voter = Button(
        frame1, text="Voter Login", width=15, command=lambda: voterLogin(root, frame1)
    )

    # New Tab
    newTab = Button(
        frame1,
        text="New Window",
        width=15,
        command=lambda: sb_p.call("start python homePage.py", shell=True),
    )

    registerVoter = Button(
        frame1,
        text="Register Voter",
        width=15,
        command=lambda: regV.Register(root, frame1),
    )

    Label(frame1, text="").grid(row=2, column=0)
    Label(frame1, text="").grid(row=4, column=0)
    Label(frame1, text="").grid(row=6, column=0)
    Label(frame1, text="").grid(row=8, column=0)
    admin.grid(row=3, column=1, columnspan=2)
    voter.grid(row=7, column=1, columnspan=2)
    newTab.grid(row=9, column=1, columnspan=2)
    registerVoter.grid(row=5, column=1, columnspan=2)
    frame1.pack()
    root.mainloop()


def new_home():
    root = Tk()
    root.geometry("500x500")
    frame1 = Frame(root)
    frame2 = Frame(root)
    Home(root, frame1, frame2)


if __name__ == "__main__":
    new_home()
