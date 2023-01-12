import tkinter
import customtkinter

from nlp_mini_project import ProfHinglishFilter

customtkinter.set_appearance_mode("System")  
customtkinter.set_default_color_theme("blue")  

def show_entry_fields():
  p1= e1.get()
  customtkinter.CTkLabel(app,text="No profanities detected!",font=("Helvetica", 20)).place(x=100,y=240)

  model=ProfHinglishFilter(p1)
  result=model.filter_gaali()
  print("Expletives detected and filtered! Please avoid using swear words.\n",result)
  customtkinter.CTkLabel(app,text="Input:" + e1.get(),font=("Helvetica", 20)).place(x=100,y=240)
  if result[1]==result[0]:
    customtkinter.CTkLabel(app,text="No profanities detected!",font=("Helvetica", 20)).place(x=100,y=240)
  else:
    customtkinter.CTkLabel(app,font=("Helvetica", 20),text="The filtered text is as follows:\n"+result[0]).place(x=100,y=240)


app = customtkinter.CTk() 
app.geometry("600x500")
app.title("Hinglish Profanity filter")


label = customtkinter.CTkLabel(master=app, text="Hinglish Profanity filter", font=("Helvetica", 24, "bold"))
label.place(x=300, y=40, anchor=tkinter.CENTER)

e1 = customtkinter.CTkEntry(master=app, 
        placeholder_text="Enter your message", 
        corner_radius=10,
        width=400,
        font=("Helvetica", 20)
        )
e1.pack(fill="x", pady=(80, 0), ipady=20, padx=10)


# Use CTkButton instead of tkinter Button
button = customtkinter.CTkButton(master=app, text="CTkButton", font=("Helvetica", 24, "bold"), command=show_entry_fields)
button.pack(ipadx=10, ipady=10, pady=(20, 0))

app.mainloop()
