from tkinter import *
import time#module
import numpy as np
from PIL import ImageTk, Image
import random#module
from tkinter import messagebox
import os.path
menu_data = np.genfromtxt('Menu.csv',delimiter = ',',skip_header=1)
menu = []
for i in menu_data:
    menu.append(int(i))
window = Tk()
window.geometry("1600x8000")
window.title("CAFE BILL MANAGEMENT")

ll = Label(window, text="----------------- BATCH 5 COFFEE HOUSE -----------------", font=("roman", 30))
ll.place(x=75, y=20)
ll.configure(bg="grey", fg="black")

lt = time.asctime(time.localtime(time.time()))
time_label = Label(window, font=('aria', 12,), text=lt, fg="black")
time_label.place(x=75, y=80)

def calculate():
    if (e1.get() == ""):
        m1 = 0
    else:
        m1 = e1.get()
    if (e2.get() == ""):
        m2 = 0
    else:
        m2 = e2.get()
    if (e3.get() == ""):
        m3 = 0
    else:
        m3 = e3.get()
    if (e4.get() == ""):
        m4 = 0
    else:
        m4 = e4.get()
    if (e5.get() == ""):
        m5 = 0
    else:
        m5 = e5.get()
    if (e6.get() == ""):
        m6 = 0
    else:
        m6 = e6.get()
    if (e7.get() == ""):
        m7 = 0
    else:
        m7 = e7.get()
    if (e8.get() == ""):
        m8 = 0
    else:
        m8 = e8.get()
    if (e9.get() == ""):
        m9 = 0
    else:
        m9 = e9.get()
    if (e10.get() == ""):
        m10 = 0
    else:
        m10 = e10.get()
    if (e11.get() == ""):
        m11 = 0
    else:
        m11 = e11.get()
    if (e12.get() == ""):
        m12 = 0
    else:
        m12 = e12.get()
    cus_name = e13.get()
    if cus_name =="":
        messagebox.showerror('Error', 'Enter the name!!')
        return
    cus_num = e14.get()
    if cus_num=="" or len(cus_num)!=10:
        messagebox.showerror('Error', 'Please enter valid Phone no')
        return
    try :
        pno = int(cus_num)
    except:
        messagebox.showerror('Error', 'Please enter valid Phone no')
        e14.set("")
        return
    try:
        m = int(m1)+int(m2)+int(m3)+int(m4)+int(m5)+int(m6)+int(m7)+int(m8)+int(m9)+int(m10)+int(m11)+int(m12)
        total = (int(m1) * menu[0] + int(m2) * menu[1] + int(m3) * menu[2] + int(m4) * menu[3] + int(m5) * menu[4] + int(m6) * menu[5] + int(m7) * menu[6] + int(m8) * menu[7] + int(m9) * menu[8] + int(m10) * menu[9] + int(m11) * menu[10] + int(m12) * menu[11])
        e15.set(str(total))
        if m<=0:
            messagebox.showerror('No values', 'Please enter values')
            return 
        
        def bill_reciept():
    
            bill_win = Tk()
            bill_win.geometry("900x700")
            bill_win.title("BILL RECIEPT")
            f = Frame(bill_win,bd = 10)
            f.place(x=45, y=20, width=550, height=660)
            f.configure(bg="mistyrose4")

            bt = Label(f, text="BILL RECIEPT", font="arial 15 bold", bd=7).pack()
            text = Text(f,font = 'arial 15 bold')
            text.pack()
            name = str(e13.get())+str(random.randint(100,300))
            def file_save():
                if(os.path.isfile(name)):
                    files(name+"a"+str(random.randint(10,150))+".txt",total)
                else:
                    files(name+".txt",total)
            def files(name,total):
                
                with open(name,'a') as f:
                    f.write("===========BATCH 5 COFFEE SHOP===========")
                    f.write("\nCustomer Name  :"+e13.get())
                    f.write("\nPhone no       :"+e14.get())
                    f.write("\n-----------------------------------------------------------------------\n")
                    f.write('ITEMS\t\t QUANTITY \t RATE(1)\t COST')
                    f.write("\n-----------------------------------------------------------------------")
                    if (e1.get() == ""):
                        pass
                    else:
                        m1 = int(e1.get())
                        f.write("\nSingle\t\t  "+str(m1)+"\t          "+str(menu[0])+"\t          "+str(m1*menu[0]))
                    if (e2.get() == ""):
                        pass
                    else:
                        m2 = int(e2.get())
                        f.write("\nDouble\t\t  "+str(m2)+"\t          "+str(menu[1])+"\t          "+str(m2*menu[1]))
                    if (e3.get() == ""):
                        pass
                    else:
                        m3 = int(e3.get())
                        f.write("\nAmerican\t  "+str(m3)+"\t          "+str(menu[2])+"\t          "+str(m3*menu[2]))
                    if (e4.get() == ""):
                        pass
                    else:
                        m4 = int(e4.get())
                        f.write("\nCappuccino\t  "+str(m4)+"\t          "+str(menu[3])+"\t          "+str(m4*menu[3]))
                    if (e5.get() == ""):
                        pass
                    else:
                        m5 = int(e5.get())
                        f.write("\nLatte \t\t  "+str(m5)+"\t          "+str(menu[4])+"\t          "+str(m5*menu[4]))
                    if (e6.get() == ""):
                        pass
                    else:
                        m6 = int(e6.get())
                        f.write("\nMacchaito\t  "+str(m6)+"\t          "+str(menu[5])+"\t          "+str(m6*menu[5]))
                    if (e7.get() == ""):
                        pass
                    else:
                        m7 = int(e7.get())
                        f.write("\nMocha \t\t  "+str(m7)+"\t          "+str(menu[6])+"\t          "+str(m7*menu[6]))
                    if (e8.get() == ""):
                        pass
                    else:
                        m8 = int(e8.get())
                        f.write("\nAdd Jelly\t  "+str(m8)+"\t          "+str(menu[7])+"\t          "+str(m8*menu[7]))
                    if (e9.get() == ""):
                        pass
                    else:
                        m9 = int(e9.get())
                        f.write("\nAdd Flavor\t  "+str(m9)+"\t          "+str(menu[8])+"\t          "+str(m9*menu[8]))
                    if (e10.get() == ""):
                        pass
                    else:
                        m10 = int(e10.get())
                        f.write("\nBlack Coffee\t  "+str(m10)+"\t          "+str(menu[9])+"\t          "+str(m10*menu[9]))
                    if (e11.get() == ""):
                        pass
                    else:
                        m11 = int(e11.get())
                        f.write("\nIce Latte\t  "+str(m11)+"\t          "+str(menu[10])+"\t          "+str(m11*menu[10]))
                    if (e12.get() == ""):
                        pass
                    else:
                        m12 = int(e12.get())
                        f.write("\nIce Cappucino\t  "+str(m12)+"\t          "+str(menu[11])+"\t          "+str(m12*menu[11]))
                    
                    f.write("\n-----------------------------------------------------------------------")
                    f.write("\nTotal amount : "+str(total))
                    f.write("\nGST(6%) :"+str(total*0.06))
                    total = total +total*0.06
                    f.write("\nFinal Amount : "+str(total))
            
                    Save = Tk()
                    Save.geometry('400x400')
                    Save.title("SAVED")
                    Label(Save , text = "BILL IS SAVED!!",font = "arial 30 bold").place(x=50,y=150)
            text.insert(END,"===========BATCH 5 COFFEE SHOP===========")
            text.insert(END,"\nCustomer Name\t:"+e13.get())
            text.insert(END,"\nPhone no\t          :"+e14.get())
            text.insert(END,"\n-----------------------------------------------------------------------\n")
            text.insert(END,'ITEMS\t\t QUANTITY \t RATE(1)\t COST')
            text.insert(END,"\n-----------------------------------------------------------------------")
            if (e1.get() == ""):
                pass
            else:
                m1 = int(e1.get())
                text.insert(END,"\nSingle\t\t  "+str(m1)+"\t      "+str(menu[0])+"\t      "+str(m1*menu[0]))
            if (e2.get() == ""):
                pass
            else:
                m2 = int(e2.get())
                text.insert(END,"\nDouble\t\t  "+str(m2)+"\t      "+str(menu[1])+"\t      "+str(m2*menu[1]))
            if (e3.get() == ""):
                pass
            else:
                m3 = int(e3.get())
                text.insert(END,"\nAmerican\t\t  "+str(m3)+"\t      "+str(menu[2])+"\t      "+str(m3*menu[2]))
            if (e4.get() == ""):
                pass
            else:
                m4 = int(e4.get())
                text.insert(END,"\nCappuccino\t\t  "+str(m4)+"\t      "+str(menu[3])+"\t      "+str(m4*menu[3]))
            if (e5.get() == ""):
                pass
            else:
                m5 = int(e5.get())
                text.insert(END,"\nLatte \t\t  "+str(m5)+"\t      "+str(menu[4])+"\t      "+str(m5*menu[4]))
            if (e6.get() == ""):
                pass
            else:
                m6 = int(e6.get())
                text.insert(END,"\nMacchaito\t\t  "+str(m6)+"\t      "+str(menu[5])+"\t      "+str(m6*menu[5]))
            if (e7.get() == ""):
                pass
            else:
                m7 = int(e7.get())
                text.insert(END,"\nMocha \t\t  "+str(m7)+"\t      "+str(menu[6])+"\t      "+str(m7*menu[6]))
            if (e8.get() == ""):
                pass
            else:
                m8 = int(e8.get())
                text.insert(END,"\nAdd Jelly\t\t  "+str(m8)+"\t      "+str(menu[7])+"\t      "+str(m8*menu[7]))
            if (e9.get() == ""):
                pass
            else:
                m9 = int(e9.get())
                text.insert(END,"\nAdd Flavor\t\t  "+str(m9)+"\t      "+str(menu[8])+"\t      "+str(m9*menu[8]))
            if (e10.get() == ""):
                pass
            else:
                m10 = int(e10.get())
                text.insert(END,"\nBlack coffee\t\t  "+str(m10)+"\t      "+str(menu[9])+"\t      "+str(m10*menu[9]))
            if (e11.get() == ""):
                pass
            else:
                m11 = int(e11.get())
                text.insert(END,"\nIce Latte\t\t  "+str(m11)+"\t      "+str(menu[10])+"\t      "+str(m11*menu[10]))
            if (e12.get() == ""):
                pass
            else:
                m12 = int(e12.get())
                text.insert(END,"\nIce Cappucino\t\t  "+str(m12)+"\t      "+str(menu[11])+"\t      "+str(m12*menu[11]))
            def close():
                bill_win.destroy()
                Reset()
            text.insert(END,"\n-----------------------------------------------------------------------")
            text.insert(END,"\nTotal Amount : "+str(total))
            text.insert(END,"\nGST(6%) :"+str(total*0.06))
            final = total +total*0.06
            text.insert(END,"\nFinal Amount : "+str(final))
            bn = Button(bill_win,text = "SAVE",font=('bold', 14), width=10, command=file_save)
            bn.place(x=700,y=200)
            bn.configure(fg="black", bg="grey")
            bn1 = Button(bill_win,text = "QUIT",font = ('bold',14),width = 10,command = close)
            bn1.place(x=700,y=400)
            bn1.configure(fg="black",bg="grey")
        bill_reciept()
    except:
        messagebox.showerror('Error', 'Please enter integers only')
        e1.set("")
        e2.set("")
        e3.set("")
        e4.set("")
        e5.set("")
        e6.set("")
        e7.set("")
        e8.set("")
        e9.set("")
        e10.set("")
        e11.set("")
        e12.set("")
        
def Reset():
    e1.set("")
    e2.set("")
    e3.set("")
    e4.set("")
    e5.set("")
    e6.set("")
    e7.set("")
    e8.set("")
    e9.set("")
    e10.set("")
    e11.set("")
    e12.set("")
    e13.set("")
    e14.set("")
    e15.set("")
    #text.delete(1.0,END)

e1 = StringVar()
e2 = StringVar()
e3 = StringVar()
e4 = StringVar()
e5 = StringVar()
e6 = StringVar()
e7 = StringVar()
e8 = StringVar()
e9 = StringVar()
e10 = StringVar()
e11 = StringVar()
e12 = StringVar()
e13 = StringVar()
e14 = StringVar()
e15 = StringVar()


f1 = Frame(window)
f1.place(x=1140, y=80, width=200, height=570)
f1.configure(bg="mistyrose4")

l0 = Label(window, text="MENU", font=("roman", 22))
l0.place(x=1190, y=90)
l0.configure(fg="black")
l01 = Label(window, text="HOT COFFEE", font=("roman", 16))
l01.place(x=1170, y=150)
l01.configure(bg="navajowhite4", fg="black")
l1 = Label(window, text="Single...........Rs."+str(menu[0]), font=("bold",13))
l1.place(x=1165, y=190)
l2 = Label(window, text="Double..........Rs."+str(menu[1]), font=("bold",13))
l2.place(x=1165, y=220)
l3 = Label(window, text="American......Rs."+str(menu[2]), font=("bold",13))
l3.place(x=1165, y=250)
l4 = Label(window, text="Cappuccino..Rs."+str(menu[3]), font=("bold",13))
l4.place(x=1165, y=280)
l5 = Label(window, text="Latte.............Rs."+str(menu[4]), font=("bold",13))
l5.place(x=1165, y=310)
l6 = Label(window, text="Macchiato.....Rs."+str(menu[5]), font=("bold",13))
l6.place(x=1165, y=340)

l02 = Label(window, text="ICE BLENDED", font=("roman", 16))
l02.place(x=1170, y=374)
l02.configure(bg="navajowhite4", fg="black")
l7 = Label(window, text="Mocha..........Rs."+str(menu[6]), font=("bold",13))
l7.place(x=1165, y=410)
l8 = Label(window, text="Add Jelly........Rs."+str(menu[7]), font=("bold",13))
l8.place(x=1165, y=440)
l9 = Label(window, text="Add flavor.......Rs."+str(menu[8]), font=("bold",13))
l9.place(x=1165, y=470)

l03 = Label(window, text="ICE COFFEE", font=("roman", 16))
l03.place(x=1170, y=503)
l03.configure(bg="navajowhite4", fg="black")
l10 = Label(window, text="Black Coffee..Rs."+str(menu[9]), font=("bold",13))
l10.place(x=1165, y=540)
l11 = Label(window, text="Lattee............Rs."+str(menu[10]), font=("bold",13))
l11.place(x=1165, y=570)
l12 = Label(window, text="Cappuccino...Rs."+str(menu[11]), font=("bold",13))
l12.place(x=1165, y=600)

c1 = Label(window,text="Customer Name :",font =("roman",12),bd=7)
c1.place(x=75 , y = 110)
c1.configure(bg="mistyrose4",fg="black")
tc1 = Entry(window,textvariable = e13,bd=10)
tc1.place(x=210,y=110)

c2 = Label(window,text="Phone No :",font =("roman",12),bd=7)
c2.place(x=400 , y = 110)
c2.configure(bg="mistyrose4",fg="black")
tc2 = Entry(window,textvariable = e14,bd=10)
tc2.place(x=490,y=110)

l001 = Label(window, text="Hot Coffee(Quantity ordered)", font=("roman", 14))
l001.place(x=715, y=90)
l001.configure(bg="mistyrose4", fg="black")
l13 = Label(window, text="Single", font=("bold", 14))
l13.place(x=715, y=130)
te1 = Entry(window, textvariable=e1)
te1.place(x=715, y=165)
l14 = Label(window, text="Double", font=("bold", 14))
l14.place(x=915, y=130)
te2 = Entry(window, textvariable=e2)
te2.place(x=915, y=165)
l15 = Label(window, text="American", font=("bold", 14))
l15.place(x=715, y=185)
te3 = Entry(window, textvariable=e3)
te3.place(x=715, y=215)
l16 = Label(window, text="cappuccino", font=("bold", 14))
l16.place(x=915, y=185)
te4 = Entry(window, textvariable=e4)
te4.place(x=915, y=215)
l17 = Label(window, text="Latte", font=("bold", 14))
l17.place(x=715, y=235)
te5 = Entry(window, textvariable=e5)
te5.place(x=715, y=265)
l18 = Label(window, text="Macchiato", font=("bold", 14))
l18.place(x=915, y=235)
te6 = Entry(window, textvariable=e6)
te6.place(x=915, y=265)

l002 = Label(window, text="Ice Blend(Quantity ordered)", font=("roman", 14))
l002.place(x=715, y=305)
l002.configure(bg="mistyrose4", fg="black")
l19 = Label(window, text="Mocha", font=("bold", 14))
l19.place(x=715, y=340)
te7 = Entry(window, textvariable=e7)
te7.place(x=715, y=375)
l20 = Label(window, text="Add Jelly", font=("bold", 14))
l20.place(x=915, y=340)
te8 = Entry(window, textvariable=e8)
te8.place(x=915, y=375)
l21 = Label(window, text="Add flavor", font=("bold", 14))
l21.place(x=715, y=395)
te9 = Entry(window, textvariable=e9)
te9.place(x=715, y=425)

l003 = Label(window, text="Ice Coffee(Quantity ordered)", font=("roman", 14))
l003.place(x=715, y=460)
l003.configure(bg="mistyrose4", fg="black")
l22 = Label(window, text="Black Coffe", font=("bold", 14))
l22.place(x=715, y=495)
te10 = Entry(window, textvariable=e10)
te10.place(x=715, y=530)
l23 = Label(window, text="Latte", font=("bold", 14))
l23.place(x=915, y=495)
te11 = Entry(window, textvariable=e11)
te11.place(x=915, y=530)
l24 = Label(window, text="Cappucino", font=("bold", 14))
l24.place(x=715, y=555)
te12 = Entry(window, textvariable=e12)
te12.place(x=715, y=590)

img = ImageTk.PhotoImage(Image.open("cof.jpg"))
pic_label = Label(window, image = img)
pic_label.place(x=95 , y = 180)

b = Button(window, text="GENERATE BILL", font=('bold', 14), width=15, command=calculate)
b.place(x=715, y=680)
b.configure(fg="black", bg="grey")
r = Button(window, text="RESET", font=( 'bold',14), width=10, command=Reset)
r.place(x=915, y=680)
r.configure(fg="black", bg="grey")
final_amt = Label(window, font=('bold',18), text="TOTAL", bg="grey", fg="black")
final_amt.place(x=1100, y=682)
tot = Entry(window, font=('arial', 15, 'bold'), text=e15, width=6,bd=6)
tot.place(x=1190, y=680)

window.mainloop()