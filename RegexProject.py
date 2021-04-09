#Author: Guo Tan

from tkinter import *
from re import *
from tkinter import filedialog
from pdfminer import high_level
from PIL import *

'''def email_Extraction():
    pdf_emailextraction()
    email1_extraction()'''

'''def pdf_emailextraction():
    pdf_file = filedialog.askopenfilename(initialdir= "C:/Users/ak244/Desktop", title= "File Handler", filetypes= (("PDF Files", "*.pdf"),))
    pdf_file = high_level.extract_text(pdf_file, password='', page_numbers=None, maxpages=0, caching=True, codec='utf-8', laparams=None)
    pdf_file = findall(' [^,;\s]+@[^,;\s]+ ', pdf_file)
    textfile_out.insert(END, pdf_file)'''

def email1_extraction():
    text_file = filedialog.askopenfilename(initialdir= "C:/Users/ak244/Desktop", title= "File Handler", filetypes= (("Text Files", "*.txt"),))
    text_file = open(text_file, 'r')
    for email in text_file:
        email = findall('[^,;\s]+@[^,;\s]+', email)
        for i in email:
            i = i + ' ' + '\n'
            textfile_out.insert(END, i)

def Phone1_extraction():
    text_file = filedialog.askopenfilename(initialdir= "C:/Users/ak244/Desktop", title= "File Handler", filetypes= (("Text Files", "*.txt"),))
    text_file = open(text_file, 'r')
    for phone in text_file:
        phone = findall("\(\w{3}\)-\w{3}-\w{4}", phone)
        for j in phone:
            j = j + ' ' + '\n'
            textfile_out.insert(END, j)

root = Tk()
root.title("Text File Handler")
root.geometry('800x700+500+200')
photo = PhotoImage(file='backimg.png')
photo = photo.zoom(4,4)
window_background = Label(root, image=photo)
window_background.place(x=0, y=0)
textfile_out = Text(root, font= ("Helvetica", 25))
textfile_out.pack(pady= 100)
img1 = PhotoImage(file="C:/Users/ak244/Desktop/Python/button_extract-email-txt.png")
button_1 = Button(root, padx = 12, pady = 12, image = img1, command = email1_extraction).place(x=100,y=25)
img2 = PhotoImage(file="C:/Users/ak244/Desktop/Python/button_extract-phone-txt.png")
button_2 = Button(root, padx = 12, pady = 12, image= img2, command = Phone1_extraction).place(x=400,y=25)
root.mainloop()