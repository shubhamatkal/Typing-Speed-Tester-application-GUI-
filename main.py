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


#second row
backward = Button(window,
                  text='<<',
                  bg='lightblue1', fg='black',
                  font='Helvetica 20',
                  )

para_title = Label(window, fg='black', bg='white', text="self.topic.get()", font='Helvetica 22')

forward = Button(window,
                 text='>>',
                 bg='lightblue1', fg='black',
                 font='Helvetica 20')

backward.grid(row=1, column=0, pady=35)
para_title.grid(row=1, column=1, pady=35)
forward.grid(row=1, column=2, pady=(35))






#end code
window.mainloop()