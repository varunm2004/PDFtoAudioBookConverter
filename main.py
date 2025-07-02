import pyttsx3
import PyPDF2
from tkinter.filedialog import *

book = askopenfilename() # asks  to open a file's name
pdfreader = PyPDF2.PdfFileReader(book) # assigns book to pdf 
pages = len(pdfreader.pages) # returns num of pages in pdf

# this section reads all the data from the collected PDF

for num in range(0,pages): # for loop from first page to last page
    page = pdfreader.pages[num] # makes each page be returned as an object
    text = page.extract_text() # extracts all the plain text from the page
    player = pyttsx3.init() 
    player.say(text)
    player.runAndWait()

