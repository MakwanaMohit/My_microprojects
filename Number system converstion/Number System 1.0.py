from tkinter import *
root = Tk()
root.title("TextBox Input")
root.geometry('400x250+600+200')
root.config(bg="skyblue")


# ============Function=============

def todecimal ():
    inputentry = str(t1.get())
    type = (inputentry)[:2]
    entry = (inputentry)[3:]
    if type=="0i":
        decimal = int(entry)

    elif type=="0b":
        decimal = int(entry,2)

    elif type=="0o":
        decimal = int(entry,8)

    elif type=="0x":
        decimal = int(entry,16)

    prin(decimal)


def prin(decimal):
    binary = bin(decimal)[2:]
    octal = oct(decimal)[2:]
    hexadecimal = hex(decimal)[2:]
    
    e1.delete(0,'end')
    e1.insert(END,str(decimal))

    e2.delete(0,'end')
    e2.insert(END,str(binary))

    e3.delete(0,'end')
    e3.insert(END,str(octal))

    e4.delete(0,'end')
    e4.insert(END,str(hexadecimal))


def secondwindow():
    sroot = Tk()
    sroot.title("TextBox Input")
    sroot.geometry('400x250+220+480')
    sroot.config(bg="skyblue")
    l1 = Label(sroot, text="type the value as show below",font=('arial 10',11,'italic bold'), bg="skyblue")
    l1.place(x=90, y=10)

    # =========Entry Box===========

    e0=Entry(sroot,justify=CENTER , font=('arial 10',10,'bold'))
    e0.insert(END,str("0i:value"))
    e0.place(x=180,y=50)

    e1=Entry(sroot,justify=CENTER , font=('arial 10',10,'bold'))
    e1.insert(END,str("0b:value"))
    e1.place(x=180,y=80)

    e2=Entry(sroot,justify=CENTER , font=('arial 10',10,'bold'))
    e2.insert(END,str("0o:value"))
    e2.place(x=180,y=110)

    e3=Entry(sroot,justify=CENTER , font=('arial 10',10,'bold'))
    e3.insert(END,str("0x:value"))
    e3.place(x=180,y=140)

    e4=Entry(sroot,justify=CENTER , font=('arial 10',10,'bold'))
    e4.insert(END,str("0b:1101"))
    e4.place(x=180,y=170)


    # =============Label=============

    l1 = Label(sroot, text="for Decimal",font=('arial 10',11,'italic bold'), bg="skyblue")
    l1.place(x=30, y=50)

    l2 = Label(sroot, text="for Binary",font=('arial 10',11,'italic bold'), bg="skyblue")
    l2.place(x=30, y=80)

    l3 = Label(sroot, text="for Octal",font=('arial 10',11,'italic bold'), bg="skyblue")
    l3.place(x=30, y=110)

    l4 = Label(sroot, text="for HexaDecimal ",font=('arial 10',11,'italic bold'), bg="skyblue")
    l4.place(x=30, y=140)

    l5 = Label(sroot, text="Example",font=('arial 10',11,'italic bold'), bg="skyblue")
    l5.place(x=30, y=170)

    l6 = Label(sroot, text="then press on convert button to convert the value",font=('arial 10',11,'italic bold'), bg="skyblue")
    l6.place(x=30, y=200)



# =========Entry Box===========

t1=Entry(root,justify=CENTER , font=('arial 10',10,'bold'))
t1.insert(END,str("0i:value"))
t1.place(x=192,y=50)

e1=Entry(root,justify=CENTER , font=('arial 10',10,'bold'))
e1.place(x=192,y=80)

e2=Entry(root,justify=CENTER , font=('arial 10',10,'bold'))
e2.place(x=192,y=110)

e3=Entry(root,justify=CENTER , font=('arial 10',10,'bold'))
e3.place(x=192,y=140)

e4=Entry(root,justify=CENTER , font=('arial 10',10,'bold'))
e4.place(x=192,y=170)


# =============Label=============

l1 = Label(root, text="enter the value here  :",font=('arial 10',11,'bold'), bg="skyblue")
l1.place(x=30, y=50)

l2 = Label(root, text="Decimal Value             :",font=('arial 10',11,'bold'), bg="skyblue")
l2.place(x=30, y=80)

l3 = Label(root, text="Binary Value                :",font=('arial 10',11,'bold'), bg="skyblue")
l3.place(x=30, y=110)

l4 = Label(root, text="Octal Value                  :",font=('arial 10',11,'bold'), bg="skyblue")
l4.place(x=30, y=140)

l5 = Label(root, text="HexaDecimal Value    :",font=('arial 10',11,'bold'), bg="skyblue")
l5.place(x=30, y=170)


# ============button==========

button = Button(root,width=10,text="convert",font=('arial 10 ',10,'bold') ,command=lambda:todecimal()).place(x=183,y=200)

button = Button(root,width=10,text="how to use",font=('arial 10 ',10,'bold') ,command=lambda:secondwindow()).place(x=90,y=200)





root.mainloop()


