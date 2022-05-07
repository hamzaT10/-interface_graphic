colors=['blue']
def slider():
	global count,text
	if(len(text)<count):
		cont=0
		text=''
	text=text+text[count]
	title.configure(text=text)
	color=random.choice(colors)
	title.config(bg=color)
	count+=1
	root.after(400,slider)

def fetch_data(event=None):
	db=sqlite3.connect('BD.db')
	con=db.cursor()
	con.execute("select * from student")
	rows = con.fetchall()
	if len(rows) != 0:
		student_table.delete(*student_table.get_children())
		for row in rows:
			student_table.insert('', END, values=row)
		db.commit()
	db.close()

def show_all():
	db=sqlite3.connect('BD.db')
	con=db.cursor()
	rows=con.execute('select * from student')
	for row in rows:
		student_table.insert('',END,values=row)
	db.commit()
	db.close()
	fetch_data()

def search_data():
	db=sqlite3.connect('BD.db')
	con=db.cursor()
	con.execute(
		"select * from student where  " + str(search_var.get()) + " Like '%" + str(search_entry.get()) + "%'")
	rows = con.fetchall()
	if len(rows) != 0:
		student_table.delete(*student_table.get_children())
		for row in rows:
			student_table.insert('', END, values=row)
		db.commit()
	db.close()




def delete_data():
	db = sqlite3.connect('BD.db')
	con = db.cursor()
	con.execute("delete from student where roll_var='"+roll_var.get()+"'")
	db.commit()
	db.close()
	fetch_data()
	messagebox.showinfo('Student', 'Student has been deleted')
	clear()


def update():
	db=sqlite3.connect('BD.db')
	con=db.cursor()
	con.execute("update student set name_var='"+name_var.get()+"',email_var='"+email_var.get()+"',gender_var='"+gender_var.get()+"',contact_var='"+contact_var.get()+"',dob_var='"+dob_var.get()+"',adress_txt='"+address_text.get(1.0,END)+"' where roll_var='"+roll_var.get()+"'")
	messagebox.showinfo('student','Data updated')
	db.commit()
	fetch_data()
	clear()
	db.close()

def get_cursor(event=None):
	cursor_row=student_table.focus()
	content=student_table.item(cursor_row)
	row=content['values']
	roll_var.set(row[0])
	name_var.set(row[1])
	email_var.set(row[2])
	gender_var.set(row[4])
	contact_var.set(row[3])
	dob_var.set(row[5])
	address_text.delete(1.0,END)
	address_text.insert(END,row[6])

def clear():
	roll_var.set('')
	name_var.set('')
	email_var.set('')
	gender_var.set('')
	contact_var.set('')
	dob_var.set('')
	address_text.delete(1.0,END)

def add_student():
	db = sqlite3.connect('BD.db')
	con = db.cursor()
	con.execute("insert into student values('"+roll_var.get()+"','"+name_var.get()+"','"+email_var.get()+"','"+dob_var.get()+"','"+gender_var.get()+"','"+contact_var.get()+"','"+address_text.get(1.0,'end')+"');")
	db.commit()
	db.close()
	fetch_data()
	messagebox.showinfo('Student','Data added')
	clear()



from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3
import random
count=0
text=' Student Manegment  System ---++--- '

root=Tk()
root.title('Student Manegment System')
root.geometry('1530x800+0+0')
title=Label(root,text='',font='timesnewroman 30 bold',fg='white',bg='powder blue',bd=4,relief=RAISED,width=10)
title.pack(side='top',fill='x')
##################variables
roll_var=StringVar()
name_var=StringVar()
email_var=StringVar()
gender_var=StringVar()
contact_var=StringVar()
dob_var=StringVar()
search_var=StringVar()
#####################mange_frame
manage_frame=Frame(root,bd=4,relief=RIDGE,bg='powder blue')
manage_frame.place(x=20,y=80,width=550,height=545)
#Manage Title
m_title=Label(manage_frame,text='MANAGE STUDENT',font='timesnewroman 30 bold',fg='white',bg='green',bd=2,relief=RAISED)
m_title.grid(row=0,columnspan=2,padx=20,pady=20)

#labes
lbl_roll=Label(manage_frame,text='Roll No.',font='timesnewroman 19 bold',fg='green',bd=0,bg='powder blue',relief=RAISED)
lbl_roll.grid(row=1,column=0,padx=20,pady=10,sticky='w')

rool_entry=ttk.Entry(manage_frame,font='timesnewroman 19 bold',textvariable=roll_var)
rool_entry.grid(row=1,column=1,padx=20,pady=10,sticky='w')

lbl_name=Label(manage_frame,text='Name',font='timesnewroman 19 bold',fg='pink',bd=0,bg='powder blue',relief=RAISED)
lbl_name.grid(row=2,column=0,padx=20,pady=10,sticky='w')

name_entry=ttk.Entry(manage_frame,font='timesnewroman 19 bold',textvariable=name_var)
name_entry.grid(row=2,column=1,padx=20,pady=10,sticky='w')

lbl_email=Label(manage_frame,text='Email',font='timesnewroman 19 bold',fg='blue',bd=0,bg='powder blue',relief=RAISED)
lbl_email.grid(row=3,column=0,padx=20,pady=10,sticky='w')

email_entry=ttk.Entry(manage_frame,font='timesnewroman 19 bold',textvariable=email_var)
email_entry.grid(row=3,column=1,padx=20,pady=10,sticky='w')

lbl_gender=Label(manage_frame,text='Gender',font='timesnewroman 19 bold',fg='red',bd=0,bg='powder blue',relief=RAISED)
lbl_gender.grid(row=4,column=0,padx=20,pady=10,sticky='w')

combo_gender=ttk.Combobox(manage_frame,width=18,font='timesnewroman 20 bold',state='r',textvariable=gender_var)
combo_gender['values']=('Male','Female','Other ')
combo_gender.grid(row=4,column=1,padx=20,pady=10,sticky='w')
combo_gender.set('Select Gender')


lbl_contact=Label(manage_frame,text='Contact',font='timesnewroman 19 bold',fg='green',bd=0,bg='powder blue',relief=RAISED)
lbl_contact.grid(row=5,column=0,padx=20,pady=10,sticky='w')

contact_entry=ttk.Entry(manage_frame,font='timesnewroman 19 bold',textvariable=contact_var)
contact_entry.grid(row=5,column=1,padx=20,pady=10,sticky='w')

lbl_dob=Label(manage_frame,text='D.O.B',font='timesnewroman 19 bold',fg='white',bd=0,bg='powder blue',relief=RAISED)
lbl_dob.grid(row=6,column=0,padx=20,pady=10,sticky='w')

dob_entry=ttk.Entry(manage_frame,font='timesnewroman 19 bold',textvariable=dob_var)
dob_entry.grid(row=6,column=1,padx=20,pady=10,sticky='w')


lbl_address=Label(manage_frame,text='Address',font='timesnewroman 19 bold',fg='black',bd=0,bg='powder blue',relief=RAISED)
lbl_address.grid(row=7,column=0,padx=20,pady=10,sticky='w')

address_text=Text(manage_frame,width=20,height=3,font='timesnewroman 19 bold')
address_text.grid(row=7,column=1,padx=20,pady=10,sticky='w')
######### button frames
btn_frame=Frame(root,bd=4,relief=RIDGE,bg='green')
btn_frame.place(x=23,y=625,width=545)

add_btn=Button(btn_frame,text='ADD',width=13,height=2,fg='white',bg='crimson',command=add_student)
add_btn.grid(row=0,column=0,padx=10,pady=10)

update_btn=Button(btn_frame,text='UPDATE',width=13,height=2,fg='white',bg='crimson',command=update)
update_btn.grid(row=0,column=1,padx=10,pady=10)

delete_btn=Button(btn_frame,text="DELETE",width=13,height=2,fg='white',bg='crimson',command=delete_data)
delete_btn.grid(row=0,column=2, padx=10,pady=10)

clear_btn=Button(btn_frame,text='CLEAR',width=13,height=2,fg='white',bg='crimson',command=clear)
clear_btn.grid(row=0,column=3,padx=10,pady=10)

####################details frame

details_frame=Frame(root,bd=0,relief=RIDGE,bg='blue')

details_frame.place(x=600,y=80,width=750,height=600)

search_label=Label(details_frame,text='Search By',fg='red',font='timesnewroman 19 bold',bg='powder blue',relief=RAISED,bd=0)
search_label.grid(row=0,column=0,padx=20,pady=10)

search_combo=ttk.Combobox(details_frame,textvariable=search_var,width=17,font='timesnewroman 13 bold',state='r')
search_combo['values']=('Select Option','roll_var','name_var','email_var','dob_var','gender_var','contact_var','adress_txt')
search_combo.grid(row=0,column=1,padx=0,pady=10,sticky='w')

search_entry=ttk.Entry(details_frame,font='timesnewroman 12 bold')
search_entry.grid(row=0,column=2,padx=10,pady=10,sticky='w')

search_btn=Button(details_frame,text='Search',width=12,height=2,fg='green',bg='white',command=search_data)
search_btn.grid(row=0,column=3,padx=0,pady=10)

showall_btn=Button(details_frame,text='Show All',width=12,height=2,fg='green',bg='white',command=show_all)
showall_btn.grid(row=0,column=4,padx=2,pady=10)
##########333 table frame
table_frame=Frame(details_frame,bd=4,relief=RIDGE,bg='powder blue')

table_frame.place(x=10,y=70,width=725,height=515)
scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
student_table=ttk.Treeview(table_frame,column=('roll','name','email','dob','gender','contact','address'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
scroll_x.pack(side='bottom',fill='x')
scroll_y.pack(side='right',fill='y')
scroll_x.config(command=student_table.xview)
scroll_y.config(command=student_table.yview)

student_table.heading('roll',text='Roll No')
student_table.heading('name',text='Name')
student_table.heading('email',text='Email')
student_table.heading('dob',text='DOB')
student_table.heading('gender',text='Gender')
student_table.heading('contact',text='Contact')
student_table.heading('address',text='Address')
student_table['show']='headings'

student_table.column('roll',width=90)
student_table.column('name',width=130)
student_table.column('email',width=120)
student_table.column('dob',width=120)
student_table.column('gender',width=100)
student_table.column('contact',width=120)
student_table.column('address',width=150)
student_table.pack(fill='both',expand=1)
#fetch_data()
slider()
table = ttk.Treeview(root, columns=(1, 2, 3, 4, 5, 6, 7), height=5, show="headings")
con = sqlite3.connect("BD.db")
con.execute("create table if not exists student( roll_var integer, name_var text  , email_var text , dob_var text, gender_var text, contact_var, adress_txt text)  ")
cuser = con.cursor()
select = cuser.execute("select *  from student")
for row in select:
    table.insert('', END, value=row)

student_table.bind('<ButtonRelease-1>',get_cursor)
root.mainloop()