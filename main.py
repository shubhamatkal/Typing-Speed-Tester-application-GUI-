#imports
from tkinter import *

#creating tkinter window
window = Tk()
window.geometry("1345x680")
window.title("Typing Speed And Accuracy Test")
window.configure(bg = "azure2")

#TODO Home page for application ================================
#heading label
header = Label(window,
            text= 'Select Paragraph For Test',
            font= 'rockwell 25 bold underline'
            , fg= 'black')
header.grid(row=0 , column=0 , columnspan=3, pady=20)






#end code
window.mainloop()