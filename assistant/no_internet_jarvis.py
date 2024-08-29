from tkinter import *
from PIL import ImageTk, Image
import threading

root = None


class No_internet:
    @staticmethod
    def cleartext():
        global entryBox
        entryBox.delete(0, END)

    @staticmethod
    def buttonPushed():
        global entryBox
        command = entryBox.get()
        input_command = open('command.txt', 'w')
        input_command.write(command)
        input_command.close()
        No_internet.cleartext()

    @staticmethod
    def createTextBox(parent):
        global entryBox
        entryBox = Entry(parent, width='30', background='dark grey', foreground='black')
        entryBox.place(x=58, y=30)

    def main_screen():
        root = Tk()
        root.geometry("299x169")
        root.geometry("+1050+0")
        root.resizable(False, False)
        root.wm_attributes("-topmost", 1)

        fullcanvas = Canvas(root, height='169', width='299', bd=0, highlightthickness=0, relief='raised')
        fullcanvas.pack()

        copy_of_image1 = Image.open(r"assistant/download.jpg")
        img1 = ImageTk.PhotoImage(copy_of_image1)

        fullcanvas.create_image(150, 85, image=img1)

        No_internet.createTextBox(root)
        button1 = Button(root, text='Enter', command=No_internet.buttonPushed)
        button1.place(x=130, y=72)
        root.mainloop()
