import pyttsx3
import PyPDF2
from tkinter.filedialog import *

book = askopenfilename() # asks  to open a file's name
pdfreader = PyPDF2.PdfFileReader(book) # assigns book to pdf reader

