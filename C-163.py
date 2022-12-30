from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Color Randomizing game")
root.geometry("600x600")
root.config(bg="#729fe8")

q1rb=StringVar()

q1=Label(root,text="Do you experience shortness of breath during routine activities?",bg="#729fe8",fg="black")
q1.place(relx=0.5,rely=0.2,anchor=CENTER)
q1r1=Radiobutton(root,text="yes",variable=q1rb,value="yes",bg="#729fe8",fg="black")
q1r1.place(relx=0.5,rely=0.25,anchor=CENTER)
q1r2=Radiobutton(root,text="no",variable=q1rb,value="no",bg="#729fe8",fg="black")
q1r2.place(relx=0.5,rely=0.3,anchor=CENTER)



q2rb=StringVar()

q2=Label(root,text="Do you experience shortness of breath while at rest/lying down?",bg="#729fe8",fg="black")
q2.place(relx=0.5,rely=0.35,anchor=CENTER)
q2r1=Radiobutton(root,text="yes",variable=q2rb,value="yes",bg="#729fe8",fg="black")
q2r1.place(relx=0.5,rely=0.4,anchor=CENTER)
q2r2=Radiobutton(root,text="no",variable=q2rb,value="no",bg="#729fe8",fg="black")
q2r2.place(relx=0.5,rely=0.45,anchor=CENTER)



q3rb=StringVar()

q3=Label(root,text="Do you feel short of breath while lying flat and feel the need to stack multiple pillows to sleep well?",bg="#729fe8",fg="black")
q3.place(relx=0.5,rely=0.5,anchor=CENTER)
q3r1=Radiobutton(root,text="yes",variable=q3rb,value="yes",bg="#729fe8",fg="black")
q3r1.place(relx=0.5,rely=0.55,anchor=CENTER)
q3r2=Radiobutton(root,text="no",variable=q3rb,value="no",bg="#729fe8",fg="black")
q3r2.place(relx=0.5,rely=0.6,anchor=CENTER)



q4rb=StringVar()

q4=Label(root,text="Do you experience persistent wheezing / coughing that produces white or pink blood tinged mucus?",bg="#729fe8",fg="black")
q4.place(relx=0.5,rely=0.65,anchor=CENTER)
q4r1=Radiobutton(root,text="yes",variable=q4rb,value="yes",bg="#729fe8",fg="black")
q4r1.place(relx=0.5,rely=0.7,anchor=CENTER)
q4r2=Radiobutton(root,text="no",variable=q4rb,value="no",bg="#729fe8",fg="black")
q4r2.place(relx=0.5,rely=0.75,anchor=CENTER)


q5rb=StringVar()

q5=Label(root,text="Do you experience persistent wheezing / coughing that produces white or pink blood tinged mucus?",bg="#729fe8",fg="black")
q5.place(relx=0.5,rely=0.8,anchor=CENTER)
q5r1=Radiobutton(root,text="yes",variable=q5rb,value="yes",bg="#729fe8",fg="black")
q5r1.place(relx=0.5,rely=0.85,anchor=CENTER)
q5r2=Radiobutton(root,text="no",variable=q5rb,value="no",bg="#729fe8",fg="black")
q5r2.place(relx=0.5,rely=0.9,anchor=CENTER)

def report():
    score=0
    if q1rb.get()=="yes":
        score+=10
    if q2rb.get()=="yes":
        score+=10
    if q3rb.get()=="yes":
        score+=10
    if q4rb.get()=="yes":
        score+=10
    if q5rb.get()=="yes":
        score+=10
    
    if score<=10:
        messagebox.showinfo("Report","You don't need to visit a doctor.")
    elif score>10 and score <=30:
        messagebox.showinfo("Report","You might perhaps need to visit a doctor.")
    else:
        messagebox.showinfo("Report","I strongly advise you to visit a doctor.")

btn=Button(root,text="Generage Report",command=report)
btn.place(relx=0.5,rely=0.95,anchor=CENTER)



root.mainloop()
