from tkinter import *
from tkinter import filedialog

import pyttsx3 
import PyPDF2

#----Terminal commands----

# python -m venv venv - makes Environment
# . venv/Scripts/activate - to start env
# pip install pyttsx3
# pip install PyPDF2


root = Tk()
root.geometry('350x350')

label_page = Label(root, text="Starting Page Number").pack()
start_page_number = Entry(root)
start_page_number.pack()

label = Label(root, text="Which book you want to read?").pack()

def fileDialog():
    path = filedialog.askopenfilename()
    book = open(path, 'rb')
    pdfReader = PyPDF2.PdfFileReader(book)
    pages = pdfReader.numPages
    speaker = pyttsx3.init()
    
    for num in range(int(start_page_number.get()), pages):
        page = pdfReader.getPage(num)
        txt = page.extractText()
        speaker.say(txt)
        speaker.runAndWait()

Button(root, text="Choose Book", command=fileDialog).pack()

root.mainloop()
