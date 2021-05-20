import tkinter
from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import pymysql
import sys


root = Tk()
#creating a toplevel window as class page
#top4 = Toplevel(root)
root.title('Pharmacy Management System')
root.geometry('940x550+60+50')
    #top1.configure(bg='#39b7cd')

#=======================================================Functions==========================================================
def iClear():
    itemName.delete(0,END)
    itemCode.delete(0,END)
    company.delete(0,END)
    price.delete(0,END)
    category.delete(0,END)

def fetch_data():
    con = pymysql.connect(host='localhost',user='root',password='',database='pharmacy')
    cur = con.cursor()
    cur.execute("SELECT * FROM drug")
    rows = cur.fetchall()
    if (rows) != 0:
        itemlist.delete(*itemlist.get_children())
        for row in rows:
            itemlist.insert('',END,values=row)
            con.commit()
        con.close()
        



def add_data():
    if itemName.get() == '' or itemCode.get() == '' or company.get() == '' or price.get() == '' or category.get() == '':
        tkinter.messagebox.showerror('Missing values','All fields are required')
    else:
        con = pymysql.connect(host='localhost',user='root',password='',database='pharmacy')
        cur = con.cursor()
        cur.execute("INSERT INTO drug VALUES(%s,%s,%s,%s,%s)",( itemname.get(),
                                                                itemcode.get(),
                                                                companyname.get(),
                                                                price.get(),
                                                                category.get() ))
        con.commit()
        con.close()
        fetch_data()
        tkinter.messagebox.showinfo('Success','Record Entered Successfully')
        iClear()
    

def display():
    try:
        cursor_row = itemlist.focus()
        content = itemlist.item(cursor_row)
        row = content['values']
        itemname.set(row[0])
        itemcode.set(row[1])
        companyname.set(row[2])
        Price.set(row[3])
        Category.set(row[4])

    except:
        error = sys.exc_info()[0]
        if error == 'string index out of range':
            pass


def delete_data():
    try:
        con = pymysql.connect(host='localhost',user='root',password='',database='pharmacy')
        cur = con.cursor()
        cursor_row = itemlist.focus()
        content = itemlist.item(cursor_row)
        row = content['values']

        cur.execute("DELETE FROM drug WHERE itemName=%s",row[0])
        con.commit()
        con.close()
        fetch_data()
        tkinter.messagebox.showinfo('Success','Record Deleted Successfully')

    except:
        error = sys.exc_info()[0]
        if error == 'string index out of range':
            pass



##def update():
##    if itemName.get() == '' or itemCode.get() == '' or company.get() == '' or price.get() == '' or category.get() == '':
##        tkinter.messagebox.showerror('Missing values','All fields are required')
##    else:
##        con = pymysql.connect(host='localhost',user='root',password='',database='pharmacy')
##        cur = con.cursor()
##        cursor_row = itemlist.focus()
##        content = itemlist.item(cursor_row)
##        row = content['values']
##        cur.execute("UPDATE drug SET itemCode=%s,CompanyName=%s,itemPrice=%s,itemCategory=%s WHERE itemName=%s,",(itemcode.get(),
##                                                                                                                  companyname.get(),
##                                                                                                                  price.get(),
##                                                                                                                  category.get(),
##                                                                                                                  row[0],
##                                                                                                                ))
##        con.commit()
##        con.close()
##        fetch_data()
##        tkinter.messagebox.showinfo('Success','Record Updated Successfully')
##        iClear()



    


dash4 = '-------------------------------------------------------------------------------------------------------------------------------------------------'

dashlabel4 = Label(root,text=dash4,font=('rockwell condensed',20),
                   fg='#151B54')
dashlabel4.place(x=0,y=40)

Title = Label(root,text='Pharmacy Management System',font=('rockwell condensed',35),
                   fg='#151B54')
Title.place(x=250,y=0)


    # adding frames
Frame1 = Frame(root, width=250, height=550, bg='#b22222')
Frame1.place(x=0, y=70)

Frame2 = Frame(root, width=690, height=550, bg='#ffffff')
Frame2.place(x=250, y=70)

#================================================Variables===============================================================

itemname = StringVar()
itemcode = StringVar()
companyname = StringVar()
Price = StringVar()
Category = StringVar()

#======================================================Widgets===========================================================

Label(Frame1,text='Add New Item',font=('rockwell condensed',18), bg='#b22222', fg='#ffffff').place(x=35,y=40)

Label(Frame1,text='Item Name:',font=('Arial',12,'bold'),bg='#b22222', fg='#ffffff').place(x=10,y=100)

itemName = Entry(Frame1, width=30,font=('Arial',10,'bold'),textvariable=itemname)
itemName.place(x=10,y=125)

Label(Frame1,text='Item Code:',font=('Arial',12,'bold'),bg='#b22222', fg='#ffffff').place(x=10,y=150)

itemCode = Entry(Frame1, width=30,font=('Arial',10,'bold'),textvariable=itemcode)
itemCode.place(x=10,y=175)

Label(Frame1,text='Company Name:',font=('Arial',12,'bold'),bg='#b22222', fg='#ffffff').place(x=10,y=200)

company = Entry(Frame1, width=30,font=('Arial',10,'bold'),textvariable=companyname)
company.place(x=10,y=225)

Label(Frame1,text='Price:',font=('Arial',12,'bold'),bg='#b22222', fg='#ffffff').place(x=10,y=250)

price = Entry(Frame1, width=30,font=('Arial',10,'bold'),textvariable=Price)
price.place(x=10,y=275)

Label(Frame1,text='Category:',font=('Arial',12,'bold'),bg='#b22222', fg='#ffffff').place(x=10,y=300)

category = ttk.Combobox(Frame1,width=27,font=('Arial',10,'bold'),textvariable=Category)
category['values'] = ('Capsule','Tablets','Syrup',
                            'First Aid')
category.current(0)
category.place(x=10,y=325)


     #adding the add,delete,clear and update
Button(Frame1,text='Add',width=10,command=add_data).place(x=10,y=360)

Button(Frame1,text='Delete',width=10,command=delete_data).place(x=148,y=360)

Button(Frame1,text='Display',width=10,command=display).place(x=10,y=390)

Button(Frame1,text='Clear',width=10,command=iClear).place(x=148,y=390)

#Button(Frame1,text='Update',width=10,command=update).place(x=80,y=420)



#========================================================Treeview=======================================================

scroll_x = Scrollbar(Frame2,orient=HORIZONTAL)
scroll_y = Scrollbar(Frame2,orient=VERTICAL)

itemlist = ttk.Treeview(Frame2,height=21,columns=("ItemName","ItemCode","CompanyName","ItemPrice","ItemCategory"),
                       xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)


#itemlist.heading("no",text="No")
itemlist.heading("ItemName",text="Item_Name")
itemlist.heading("ItemCode",text="Item_Code")
itemlist.heading("CompanyName",text="Company_Name")
itemlist.heading("ItemPrice",text="Item_Price")
itemlist.heading("ItemCategory",text="Item_Category")

itemlist['show'] = 'headings'

#itemlist.column("no",width=50)
itemlist.column("ItemName",width=170)
itemlist.column("ItemCode",width=150)
itemlist.column("CompanyName",width=120)
itemlist.column("ItemPrice",width=100)
itemlist.column("ItemCategory",width=130)

itemlist.pack(fill=BOTH, expand=1)
fetch_data()




root.mainloop()
