from tkinter import *

from nlp_mini_project import ProfHinglishFilter


def show_entry_fields():
  p1= e1.get()

  model=ProfHinglishFilter(p1)
  result=model.filter_gaali()
  print("Expletives detected and filtered! Please avoid using swear words.\n",result)
  Label(master,text="Input:" + e1.get(),font=("Arial", 16)).place(x=120,y=270)
  if result[1]==result[0]:
    Label(master,text="No profanities detected!",font=("Arial", 16)).place(x=140,y=370)
  else:
    Label(master,font=("Arial", 16),text="The filtered text is as follows:\n"+result[0]).place(x=120,y=370)



master=Tk()
master.title("Hinglish Profanity Filter")
master.geometry("600x600")

label=Label(master,text="Hinglish Profanity filter"
            ,bg="black",fg="white", font=("Arial", 24)).place(x=150,y=30)

e1=Entry(master,font=("Arial", 24))

e1.place(x=135,y=100)

Button(master,text='Filter',font=("Arial", 24),command=show_entry_fields).place(x=270,y=150)

mainloop()