from tkinter import * 
from tkinter import ttk

class todolist:
  def __init__(self,root):
        self.root=root
        self.root.title("To-Do-List")
        self.root.geometry("650x500+300+200")
  
    
##label creation

        self.label=Label(self.root, text="To-Do-List-App",font="ariel,30,bold",width=10,bd=5,bg="blue",fg="black")
        self.label.pack(side="top",fill=BOTH)

        self.label2=Label(self.root, text="Add Task",font="ariel,30,bold",width=10,bd=5,bg="blue",fg="black")
        self.label2.place(x=50,y=80)

        self.label3=Label(self.root, text="Tasks",font="ariel,30,bold",width=10,bd=5,bg="blue",fg="black")
        self.label3.place(x=250,y=60)

        self.main_text=Listbox(self,root,height=9,bd=5,width=25,font="ariel,30,italic bold")
        self.main_text.place(x=280,y=120)

        self.text=text(self,root,height=9,bd=5,width=25,font="ariel,10,bold")
        self.text.place(x=20,y=120)
  def add():
    content=self.text.get(1.0,END)
    self.main_text.insert(END,content)
    with open("data.txt","a") as file:
       file.write(content)
       file.seek(0)
       file.close()
    self.text.delete(1.0,END)
    self.button=Button(self.root,text="ADD",font="ariel,20 bold italic",
                width=10,bd=5,bg='blue',fg='black',command=add)
    self.button.place(x=30,y=190)
  def delete():
        delete_=self.main_text.curselection()
        look=self.main_text.get(delete_)
        with open("data.txt","r+")as f:
            new_f=f.readlines()
            f.seek(0)
            for line in new_f:
                item=str(look)
                if item not in line:
                    f.write(line)
            f.truncate()
        self.main_text.delete(delete_)

        with open('data.txt',"r")as file:
          read=file.readlines()
          for i in read:
            ready=i.split()
            self.main_text.insert(END,ready)
            file.close()
            self.button2=Button(self.root,text="DELETE",font="ariel,20 bold italic",
                         width=10,bd=5,bg='blue',fg='black',command=delete)
            self.button2.place(x=30,y=290)
def main():
   root=Tk()
   ui=todolist(root)
   root.mainloop()
