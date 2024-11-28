from tkinter import *
from tkinter import messagebox
from student_db import Database
db = Database("c:/class/students.db")
win = Tk()
win.geometry('600x400')
win.config(bg="white")
#funcs=============================================
def show():
    lst_info.delete(0,END)
    records = db.show()
    
    for rec in records:
        lst_info.insert(END,f'{rec[0]},{rec[1]},{rec[2]},{rec[3]},{rec[4]}')
def add():
    if ent_fname.get() =='' or ent_lname.get()=='' or ent_pas.get() =='':
        messagebox.showerror("Error","The fname,lname,password filds must be filled.")
        return
    db.add(ent_fname.get(),ent_lname.get(),ent_name_c.get(),ent_pas.get())
    show()

def clear():
    ent_fname.delete(0,END)
    ent_lname.delete(0,END)
    ent_name_c.delete(0,END)
    ent_pas.delete(0,END)
    ent_fname.focus_set()
def delete():
    res = messagebox.askyesno("delete","areyou sur to delete item?")
    if res == True:
         db.delete(ent_fname.get())
    show()

def enter():
    result = db.search(ent_pas1.get())
    print(result)
    
    if result :
        win2 = Tk()
        win2.geometry("300x300")
        lbl_welcome = Label(win2,text=".خوش آمدید",font="lotus 18 bold",fg="red").pack(pady=50)
        win2.mainloop()
    else:
        messagebox.showerror("Error","invalid password")
def exit():
    win.destroy()

def select(event):
    clear()
    index = lst_info.curselection()
    data = lst_info.get(index)
    result = data.split(',')
    ent_fname.insert(0,result[1])
    ent_lname.insert(0,result[2])
    ent_name_c.insert(0,result[3])
    ent_pas.insert(0,result[4])
#widget============================================
lbl_fname = Label(win,text=":نام",font='lotus 13 bold',bg= "white")
lbl_fname.place(x=500,y=20)
lbl_star = Label(win,text="*",font="arial 13 bold",fg="red",bg='white')
lbl_star.place(x=310,y=20)
ent_fname = Entry(win,font="lotus 10")
ent_fname.place(x=330,y=20)
lbl_lname = Label(win,text=":نام خانوادگی",font='lotus 13 bold',bg= "white")
lbl_lname.place(x=190,y=20)
lbl_star1 = Label(win,text="*",font="arial 13 bold",fg="red",bg='white')
lbl_star1.place(x=10,y=20)
ent_lname = Entry(win,font="lotus 10")
ent_lname.place(x=30,y=20)
lbl_name_c = Label(win,text=":نام دوره",font='lotus 13 bold',bg= "white")
lbl_name_c.place(x=500,y=60)
ent_name_c = Entry(win,font="lotus 10")
ent_name_c.place(x=330,y=60)
lbl_pas = Label(win,text=":رمز ورود",font='lotus 13 bold',bg= "white")
lbl_pas.place(x=190,y=60)
ent_pas= Entry(win,font="lotus 10")
ent_pas.place(x=30,y=60)
lbl_star = Label(win,text="*",font="arial 13 bold",fg="red",bg='white')
lbl_star.place(x=10,y=60)
lbl_pas1 = Label(win,text=":رمز ورود",font='lotus 13 bold',bg= "white")
lbl_pas1.place(x=400,y=350)
ent_pas1 = Entry(win,font="lotus 10",width=50)
ent_pas1.place(x=30,y=350)

lst_info = Listbox(win,width=50)
lst_info.place(x=30,y=130)
lst_info.bind("<<ListboxSelect>>",select)

btn_show = Button(win,text="نمایش همه",font="lotus 12 bold",bg="violet",width=12,command=show)
btn_show.place(x=400,y=100)
btn_add = Button(win,text="اضافه کردن",font="lotus 12 bold",bg="orange",width=12,command=add)
btn_add.place(x=400,y=140)
btn_clear = Button(win,text="خالی کردن ورودی ها",font="lotus 12 bold",bg="green",width=12,command=clear)
btn_clear.place(x=400,y=180)
btn_delete = Button(win,text="حذف کردن",font="lotus 12 bold",bg="yellow",width=12,command=delete)
btn_delete.place(x=400,y=220)
btn_exit = Button(win,text="خروج",font="lotus 12 bold",bg="red",width=12,command=exit)
btn_exit.place(x=400,y=260)
btn_enter = Button(win,text="ورود به سامانه",font="lotus 12 bold",bg="blue",width=12,command=enter)
btn_enter.place(x=400,y=300)

win.mainloop()