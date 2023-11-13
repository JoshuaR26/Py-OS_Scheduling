from customtkinter import *
from customtkinter import filedialog
from tkinter import *
from tkinter import ttk

root3=CTk()
root3.geometry('750x700')
root3.title('Process Scheduling')

font1 = ('Arial',24)
row_wid = 180

'''CT = [2, 1, 0, 3]
TT = [10, 17, 12, 37]
WT = [0, 10, 7, 12]'''

AT=[]
BT=[]

def run() :
   pass
    
def ask1(*args) :
    filepath = filedialog.askopenfilename()
    EN1.delete(0,'end')
    EN1.insert(0,filepath)



def add_row() :
    #val = (EN1.get(),EN2.get(),EN3.get(),str(CT[0]),str(TT[0]), str(WT[0]))
    val = (EN1.get(),EN2.get(),EN3.get(),'-','-','-')
    AT.append(EN2.get())
    BT.append(EN3.get())
    tv.insert(parent = '',index = 'end', values = val)
    tv.place(x = 20, y = 250)
    '''del CT[0]
    del WT[0]
    del TT[0]'''

#run()
EN1 = CTkEntry(root3,width = row_wid,height = 30,font = ('calibri',20))
EN2 = CTkEntry(root3,width = row_wid,height = 30,font = ('calibri',20))
EN3 = CTkEntry(root3,width = row_wid,height = 30,font = ('calibri',20))
EN1.place(x = 20, y = 130)
EN2.place(x = 230, y = 130)
EN3.place(x = 440, y = 130)


B1 = CTkButton(root3, text = 'Add Row', width=100, height=30, command = add_row)
B1.place(x = 630, y = 130)


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
tv = ttk.Treeview(root3,columns = (1,2,3,4,5),show = "headings", style = "mystyle.Treeview")
tv.heading("1",text = "PID")
tv.column("1",anchor = CENTER,width = row_wid)
tv.heading("2",text = "AT")
tv.column("2",anchor = CENTER,width = row_wid)
tv.heading("3",text = "BT")
tv.column("3",anchor = CENTER,width = row_wid)
tv.heading("4",text = "TAT")
tv.column("4",anchor = CENTER,width = row_wid)
tv.heading("5",text = "WT")
tv.column("5",anchor = CENTER,width = row_wid)
#tv.heading("6",text = "WT")
#tv.column("6",anchor = CENTER,width = row_wid)

# tv.insert(parent = '', index = 'end', values=(1,0,4,'-','-','-'))

tv.place(x = 20,y = 250)

B2 = CTkButton(root3, text = 'Execute', width=100, height=30, command = None)
B2.place(x = 20, y = 650)
root3.mainloop()


