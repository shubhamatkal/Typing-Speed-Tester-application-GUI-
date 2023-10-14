#imports
from tkinter import *
from resources import paragraphs as p

#getting hold of paragraph topic and paragraph

#converting to list
topic_list =  list(p.indian_mythology_paragraphs.keys())
para_list =  list(p.indian_mythology_paragraphs.values())

TOPIC =  topic_list[0]
PARAGRAPH = para_list[0]
topic_index = 0
number_of_paragraphs = 11

#TODO ===== DEFINING SOME FUNCTIONS =============================
def go_forward():
    #change the para_title label
    global topic_index
    global number_of_paragraphs
    topic_index += 1
    para_title.configure(text=topic_list[topic_index % number_of_paragraphs])
    paragraph.configure(text=para_list[topic_index % number_of_paragraphs])

def go_backwards():
    global topic_index
    global number_of_paragraphs
    if topic_index == 0:
        topic_index = 10
    else:
        topic_index -= 1
    para_title.configure(text=topic_list[topic_index])
    paragraph.configure(text=para_list[topic_index])

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
                  command= go_backwards
                  )

para_title = Label(window, fg='black', bg='white', text=topic_list[0], font='Helvetica 22')

forward = Button(window,
                 text='>>',
                 bg='lightblue1', fg='black',
                 font='Helvetica 20', command=go_forward)

backward.grid(row=1, column=0, pady=35)
para_title.grid(row=1, column=1, pady=35)
forward.grid(row=1, column=2, pady=(35))


#adding paragraph
paragraph = Message(window, text=para_list[topic_index], fg='black', bg='ivory3', width=1000, justify='center',
                       font='Verdana\ Pro 18')
paragraph.grid(row=2, column=0, columnspan=3)

# add start button
start_test = Button(window, text="Start Test", font='Verdana\ Pro 15', borderwidth=3, bg='lightblue1',
                    fg='black')
start_test.grid(row=3, column=1, pady=10)


#add exit button 
exit = Button(window,
            text= 'Exit',
            font= 'Verdana\ Pro 15',
            borderwidth= 3,
            bg= 'lightblue1', fg= 'black')
exit.grid(row = 4, column = 1)





#end code
window.mainloop()