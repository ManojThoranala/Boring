"""/*H******************************************************************************************************************
* FILENAME : pdf_crwaler.py
*
* DESCRIPTION : The script shows how PDF file can be read and further processed, using PyPDF2 Library
*
* NOTES :
*
* AUTHOR :    Manoj Thoranala Manjunatha        
*
*H*/"""

import PyPDF2

path = "path to the pdf file"
pdffile = open(path, 'rb')                     # file handler for pdf file
pdfReader = PyPDF2.PdfFileReader(pdffile)      # 
pages = pdfReader.numPages                     # gives the number of pages in pdf file

for page in range(pages):                      # Looping through all pages and getting text from each page
    pageobj = pdfReader.getPage(page)
    text = pageobj.extractText()               # text has the contents of the pdf page and is in string format 
                                               # now any re.find, fidall, search can be used to find things in the text
