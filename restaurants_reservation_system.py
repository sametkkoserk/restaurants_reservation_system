from tkinter import *
from tkinter import ttk
import dbm
import pickle

class Gui():

    def windowd(self):#created window
        self.window = Tk()
        self.window.resizable(FALSE, FALSE)
        self.window.configure(background="grey")
        self.window.title("Restaurant Reservation System")
        self.window.geometry("+200+150")
        self.db=dbm.open("restaurants.db","c")


        app.up()

    def up(self):#created the upper frames and entries.
        rst=restorant()
        rzrv=table_rezervation()


        self.caption = Label(app.window, text="RESTAURANT RESERVATİON SYSTEM", bg="blue", fg="white", font=("", "25", "bold"))
        self.caption.grid(row=0, column=0,columnspan=10, sticky=EW)

        self.seçenekler=Frame(bg="grey")
        self.seçenekler.grid(row=1,column=0,sticky=EW,pady=10)

        self.r_name=Label(self.seçenekler,text="Restaurant name:",font=("", "10", "italic"),bg="grey")
        self.r_name.grid(row=1,column=0,sticky=EW)

        self.e_name=Entry(self.seçenekler)
        self.e_name.grid(row=1,column=1,padx=15)

        self.n_tables = Label(self.seçenekler, text="Number of tables:", font=("", "10", "italic"), bg="grey")
        self.n_tables.grid(row=1, column=2,  padx=15)

        self.n_tables2 = Entry(self.seçenekler)
        self.n_tables2.grid(row=1, column=3)

        self.new_r=Button(self.seçenekler,text="Create new restaurant",command=rst.newrst)
        self.new_r.grid(row=1, column=4,padx=25)

        self.seçenekler2=Frame(bg="grey")
        self.seçenekler2.grid(row=2,column=0,sticky=EW)

        self.chose_r=Label(self.seçenekler2,text="Restaurant:",font=("", "10", "italic"),bg="grey")
        self.chose_r.grid(row=2,column=0,sticky=EW)

        self.chose_r2=ttk.Combobox(self.seçenekler2,values=rst.listes,textvariable="Not selected")
        self.chose_r2.grid(row=2,column=1,padx=15)
        self.chose_r2.bind("<<ComboboxSelected>>", rst.alreadyrst)
        self.chose_r2.set("Not selected")

        self.delete=Button(self.seçenekler2,text="Delete",command=rst.rstdelete)
        self.delete.grid(row=2,column=2,padx=15)

        self.seçenekler3=Frame(bg="grey")
        self.seçenekler3.grid(row=3,column=0,sticky=EW,pady=10)

        self.table_l=Label(self.seçenekler3,text="Table:",font=("", "10", "italic"),bg="grey")
        self.table_l.grid(row=3,column=0,sticky=EW)

        self.table_e=Label(self.seçenekler3,text="[Not selected]",font=("", "10", "italic"),bg="grey")
        self.table_e.grid(row=3,column=1,sticky=EW,padx=25)

        self.customer_l=Label(self.seçenekler3,text="Customer name:",font=("", "10", "italic"),bg="grey")
        self.customer_l.grid(row=3,column=2,sticky=EW)

        self.customer_e=Entry(self.seçenekler3)
        self.customer_e.grid(row=3,column=3,padx=20)

        self.phone_l=Label(self.seçenekler3,text="Customer phone number:",font=("", "10", "italic"),bg="grey")
        self.phone_l.grid(row=3,column=4,sticky=EW)

        self.phone_e=Entry(self.seçenekler3)
        self.phone_e.grid(row=3,column=5,padx=20)

        self.save=Button(self.seçenekler3,text="Save/Update reservation",command=rzrv.real_rezervation)
        self.save.grid(row=3,column=6,padx=15)

        self.delete_re=Button(self.seçenekler3,text="Delete reservation",command=rzrv.delete_rzrv)
        self.delete_re.grid(row=3,column=7,padx=10)

        self.label=Label(self.window,bg="grey")
        self.label.grid(row=4,column=1,pady=160)





    def tables(self,table):#created the tables with controlling old rezervation depend on restaurants
        rzrv=table_rezervation()
        self.border = Frame(app.window, borderwidth=2, relief="solid",bg="grey")
        self.border.grid(row=4, column=0, sticky=EW, padx=10,columnspan=6)

        self.table_numbk = pickle.loads(app.db[app.chose_r2.get()])

        self.a=0
        if table%3!=0:
            self.a=1
        for i in range(int(table/3)+self.a):
            self.button1 = Button(self.border, text=(i*3)+1, width=9, height=3, bg="green", font=("", "15", "italic"))
            self.button1.grid(row=4, column=i, padx=10, pady=10)
            if self.table_numbk[1] != []:
                for j in self.table_numbk[1]:
                    if j[2] == (i * 3) + 1:
                        self.button1["bg"] = "red"
            self.button1.bind('<Button-1>', rzrv.rezervation)
            i+=1

        self.a=0
        if table%3>1:
            self.a=1
        for i in range(int(table/3)+self.a):
            self.button2 = Button(self.border, text=(i*3)+2, width=9, height=3, bg="green", font=("", "15", "italic"))
            self.button2.grid(row=5, column=i, padx=10, pady=10)
            if self.table_numbk[1] != []:
                for j in self.table_numbk[1]:
                    if j[2] == (i * 3) + 2:
                        self.button2["bg"] = "red"
            self.button2.bind('<Button-1>', rzrv.rezervation)

            i+=1

        for i in range(int(table/3)):
            self.button3 = Button(self.border, text=(i*3)+3, width=9, height=3, bg="green", font=("", "15", "italic"))
            self.button3.grid(row=6, column=i, padx=10, pady=10)
            if self.table_numbk[1] != []:
                for j in self.table_numbk[1]:
                    if j[2] == (i * 3) + 3:
                        self.button3["bg"] = "red"
            self.button3.bind('<Button-1>', rzrv.rezervation)

            i+=1

class restorant:
    def __init__(self):#adding the restaurants to combobox list
        self.listes=[]
        for i in app.db:
            self.listes.append(i)

    def newrst(self):#if all of input is available for creating restaurant, create new restaurants
        if app.n_tables2.get()=="" or app.e_name.get()=="":
            self.newrst_l=Label(app.seçenekler,text="Fill the form completely" ,bg="red",font=("", "10", "italic"))
            self.newrst_l.grid(row=1, column=5)
            app.seçenekler.after(2000,self.newrst_l.destroy)

        elif app.n_tables2.get().isdigit() ==False:
            self.newrst_l = Label(app.seçenekler, text="Table num. can be digits only", bg="red",font=("", "10", "italic"))
            self.newrst_l.grid(row=1, column=5)
            app.seçenekler.after(2000,self.newrst_l.destroy)

        elif int(app.n_tables2.get())<=6 or int(app.n_tables2.get())>=25 :
            self.newrst_l = Label(app.seçenekler, text="Table num. only can be between 6 and 24", bg="red",font=("", "10", "italic"))
            self.newrst_l.grid(row=1, column=5)
            app.seçenekler.after(2000,self.newrst_l.destroy)

        else:
            self.table_num=pickle.dumps([app.n_tables2.get(),[]])
            app.db[app.e_name.get()]=self.table_num
            app.up()
            self.newrst_l=Label(app.seçenekler,text="Restaurant created" ,bg="green",font=("", "10", "italic"))
            self.newrst_l.grid(row=1, column=5)
            app.seçenekler.after(2000,self.newrst_l.destroy)

    def alreadyrst(self,events):#for each restaurants find the table number.
        self.table_num2=pickle.loads(app.db[app.chose_r2.get()])
        self.unicorn=self.table_num2[0]
        app.tables(int(self.unicorn))
    def rstdelete(self):
        if app.chose_r2.get()!="Not selected":
            self.delete=Button(app.seçenekler2,text="Click again to delete",command=self.rstdelete2)
            self.delete.grid(row=2,column=2,padx=15)
    def rstdelete2(self):#delete the restaurant from database

        try:
            del app.db[app.chose_r2.get()]
            app.border.destroy()
            app.up()
            self.chose_d=Label(app.seçenekler2,text="deleted",font=("", "10", "italic"),bg="red")
            self.chose_d.grid(row=2,column=3,sticky=EW)
            app.seçenekler2.after(2000, self.chose_d.destroy)
            self.delete = Button(app.seçenekler2, text="Delete", command=self.rstdelete)
            self.delete.grid(row=2, column=2, padx=15)
        except:
            pass

class table_rezervation:

    def rezervation(self,event):# chose the table and make it selected table
        global a
        self.widget=event.widget
        a=self.widget
        app.table_e["text"]=self.widget["text"]
        self.table_numbk2 = pickle.loads(app.db[app.chose_r2.get()])
        b=0
        for i in self.table_numbk2[1]:
            if i[2]==self.widget["text"]:
                app.customer_e.delete(0, "end")
                app.phone_e.delete(0, "end")
                app.customer_e.insert(0,i[0])
                app.phone_e.insert(0,i[1])
                b+=1
        if b==0:
            app.customer_e.delete(0, "end")
            app.phone_e.delete(0, "end")

    def real_rezervation(self):# after controll create new rezervation.

        if app.table_e["text"]=="[Not selected]":
            self.newrst_l=Label(app.seçenekler3,text="First select the table" ,bg="red",font=("", "10", "italic"))
            self.newrst_l.grid(row=3, column=8)
            app.seçenekler3.after(2000,self.newrst_l.destroy)
        elif app.phone_e.get()=="" or app.customer_e.get()=="":
            self.newrst_l=Label(app.seçenekler3,text="Fill the form completely" ,bg="red",font=("", "10", "italic"))
            self.newrst_l.grid(row=3, column=8)
            app.seçenekler3.after(2000,self.newrst_l.destroy)

        elif app.phone_e.get().isdigit() ==False:
            self.newrst_l = Label(app.seçenekler3, text="Phone num. can be digits only", bg="red",font=("", "10", "italic"))
            self.newrst_l.grid(row=3, column=8)
            app.seçenekler3.after(2000,self.newrst_l.destroy)

        else:
            self.table_numbk = pickle.loads(app.db[app.chose_r2.get()])
            self.table_numbk[1].append ([app.customer_e.get(),app.phone_e.get(),a["text"]])
            self.table_numbkd=pickle.dumps(self.table_numbk)
            app.db[app.chose_r2.get()]=self.table_numbkd
            a["bg"]="red"
            self.newrst_l=Label(app.seçenekler3,text="Rezervation created" ,bg="green",font=("", "10", "italic"))
            self.newrst_l.grid(row=3, column=8)
            app.seçenekler3.after(2000,self.newrst_l.destroy)

    def delete_rzrv(self):#delete the rezervation at selected table
        if app.table_e["text"]=="[Not selected]":
            self.newrst_l=Label(app.seçenekler3,text="First select the table" ,bg="red",font=("", "10", "italic"))
            self.newrst_l.grid(row=3, column=8)
            app.seçenekler3.after(2000,self.newrst_l.destroy)

        else:
            try:
                self.table_numd = pickle.loads(app.db[app.chose_r2.get()])
                self.table_numd[1].remove([app.customer_e.get(),app.phone_e.get(),a["text"]])
                self.table_numd2  = pickle.dumps(self.table_numd)
                app.db[app.chose_r2.get()] = self.table_numd2
                a["bg"]="green"
                self.newrst_l=Label(app.seçenekler3,text="Rezervation deleted" ,bg="red",font=("", "10", "italic"))
                self.newrst_l.grid(row=3, column=8)
                app.customer_e.delete(0, "end")
                app.phone_e.delete(0, "end")
                app.seçenekler3.after(2000,self.newrst_l.destroy)
            except:
                pass


app = Gui()
app.windowd()
app.window.mainloop()