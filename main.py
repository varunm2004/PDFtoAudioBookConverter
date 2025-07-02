import pyttsx3
import PyPDF2
import pdfreader
from tkinter.filedialog import *

book = askopenfilename() # requests user to give a book file

pdfreader = PyPDF2.PdfReader(book) # assigns book object a pdf reader

pages = len(pdfreader.pages) # returns number of pages in the pdf


for num in range(0,pages): # for loop from first page to last page
    page = pdfreader.pages[num] # makes each page be returned as an object
    text = page.extract_text() # extracts all the plain text from the page
    player = pyttsx3.init() 
    player.say(text)
    player.runAndWait()

