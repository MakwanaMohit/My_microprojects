from tkinter import *
root = Tk()
root.title("TextBox Input")
root.geometry('450x210+600+200')
root.config(bg="skyblue")


# ============Function=============

def fromDecimal():
    inputentry = str(e1.get())
    entry = (inputentry)
    decimal = int(entry)
    prin(decimal)

def fromBinary():
    inputentry = str(e2.get())
    entry = (inputentry)
    decimal = int(entry,2)
    prin(decimal)

def fromOctal():
    inputentry = str(e3.get())
    entry = (inputentry)
    decimal = int(entry,8)
    prin(decimal)

def fromHexadicamal():
    inputentry = str(e4.get())
    entry = (inputentry)
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



    
# =========Entry Box===========


e1=Entry(root,justify=CENTER , font=('arial 10',10,'bold'))
e1.insert(END,str("value"))
e1.place(x=180,y=50)

e2=Entry(root,justify=CENTER , font=('arial 10',10,'bold'))
e2.insert(END,str("value"))
e2.place(x=180,y=80)

e3=Entry(root,justify=CENTER , font=('arial 10',10,'bold'))
e3.insert(END,str("value"))
e3.place(x=180,y=110)

e4=Entry(root,justify=CENTER , font=('arial 10',10,'bold'))
e4.insert(END,str("value"))
e4.place(x=180,y=140)


# =============Label=============


l1 = Label(root, text="Decimal Value             :",font=('arial 10',11,'bold'), bg="skyblue")
l1.place(x=30, y=50)

l2 = Label(root, text="Binary Value                :",font=('arial 10',11,'bold'), bg="skyblue")
l2.place(x=30, y=80)

l3 = Label(root, text="Octal Value                  :",font=('arial 10',11,'bold'), bg="skyblue")
l3.place(x=30, y=110)

l4 = Label(root, text="HexaDecimal Value    :",font=('arial 10',11,'bold'), bg="skyblue")
l4.place(x=30, y=140)


# ============button==========

button = Button(root,width=10,text="convert",font=('arial 10 ',10,'bold') ,command=lambda:fromDecimal()).place(x=340,y=46)
button = Button(root,width=10,text="convert",font=('arial 10 ',10,'bold') ,command=lambda:fromBinary()).place(x=340,y=76)
button = Button(root,width=10,text="convert",font=('arial 10 ',10,'bold') ,command=lambda:fromOctal()).place(x=340,y=106)
button = Button(root,width=10,text="convert",font=('arial 10 ',10,'bold') ,command=lambda:fromHexadicamal()).place(x=340,y=136)

root.mainloop()


