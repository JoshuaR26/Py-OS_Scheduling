from customtkinter import *
from customtkinter import filedialog
from tkinter import *
from tkinter import ttk

root3=CTk()
root3.geometry('1000x800')
root3.title('Process Scheduling')

font1 = ('Arial',12,'bold')
row_wid = 200


def run() :
   pass
    
def ask1(*args) :
    filepath = filedialog.askopenfilename()
    EN1.delete(0,'end')
    EN1.insert(0,filepath)

def add_row() :
    val = (EN1.get(),EN2.get(),EN3.get(),'-','-','-')
    tv.insert(parent = '',index = 'end', values = val)
    tv.place(x = 20, y = 250)

#run()
EN1 = CTkEntry(root3,width = row_wid,height = 30,font = ('calibri',16))
EN2 = CTkEntry(root3,width = row_wid,height = 30,font = ('calibri',16))
EN3 = CTkEntry(root3,width = row_wid,height = 30,font = ('calibri',16))
EN1.place(x = 20, y = 130)
EN2.place(x = 220, y = 130)
EN3.place(x = 420, y = 130)

B1 = CTkButton(root3, text = 'Add Row',command = add_row)
B1.place(x = 620, y = 130)

RVAR = IntVar()
RVAR.set(1)
R1 = CTkRadioButton(root3,text = "FFCS", variable = RVAR, value = 1)
R2 = CTkRadioButton(root3,text = "SJF", variable = RVAR, value = 2)
R3 = CTkRadioButton(root3,text = "Round Robin", variable = RVAR, value = 3)
R4 = CTkRadioButton(root3,text = "Prority Based", variable = RVAR, value = 4)
R1.place(x = 20, y = 50)
R2.place(x = 220, y = 50)
R3.place(x = 420, y = 50)
R4.place(x = 620, y = 50)


style = ttk.Style()
style.configure("mystyle.Treeview",font = font1,rowheight = 50)
style.configure("mystyle.Treeview.heading",font  = font1)
style.layout("mystyle.Treeview",[('mystyle.Treeview.treearea',{'sticky':'nwse'})])

tv = ttk.Treeview(root3,columns = (1,2,3,4,5,6),show = "headings", style = "mystyle.Treeview")
tv.heading("1",text = "PID")
tv.column("1",anchor = CENTER,width = row_wid)
tv.heading("2",text = "AT")
tv.column("2",anchor = CENTER,width = row_wid)
tv.heading("3",text = "BT")
tv.column("3",anchor = CENTER,width = row_wid)
tv.heading("4",text = "CT")
tv.column("4",anchor = CENTER,width = row_wid)
tv.heading("5",text = "TAT")
tv.column("5",anchor = CENTER,width = row_wid)
tv.heading("6",text = "WT")
tv.column("6",anchor = CENTER,width = row_wid)

tv.insert(parent = '', index = 'end', values=(1,0,4,'-','-','-'))

tv.place(x = 20,y = 250)

root3.mainloop()


