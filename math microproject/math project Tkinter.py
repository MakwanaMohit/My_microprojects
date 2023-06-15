from tkinter import *
import math 

root = Tk()
root.title("Math Micro Project")
root.geometry('490x580+500+150')
root.maxsize(500,600)
root.minsize(490,580)
root.config(bg="skyblue")

# ==========Function===============

def sinθ():
    vector_1 = str(e1.get())
    vector_2 = str(e2.get())
    v1_x = (int((vector_1)[2:4]))
    v1_y = (int((vector_1)[6:8]))
    v1_z = (int((vector_1)[10:12]))

    v2_x = (int((vector_2)[2:4]))
    v2_y = (int((vector_2)[6:8]))
    v2_z = (int((vector_2)[10:12]))

    cross_v_x = ((v1_y * v2_z)-(v1_z * v2_y))
    cross_v_y = -((v1_x * v2_z)-(v1_z * v2_x))
    cross_v_z = ((v1_x * v2_y)-(v1_y * v2_x))

    magn_cross_v = (cross_v_x)**2 + (cross_v_y)**2 + (cross_v_z)**2
    magn_A = (v1_x)**2 + (v1_y)**2 + (v1_z)**2
    magn_B = (v2_x)**2 + (v2_y)**2 + (v2_z)**2

    angle = (magn_cross_v**0.5)/((magn_A**0.5)*(magn_B**0.5))
    angle_degree = math.degrees(math.asin(angle))


    l3.place_configure(x=30, y=168)
    l3.config (text="cross product   :",font=('arial 20',16,'bold'), bg="skyblue")
    e4.place_configure(x=340,y=210)
    l4.place(x=30, y=210)
    e3.place(x=210,y=168)

    e3.delete(0,'end')
    e3.insert(END,("( "+str(cross_v_x)+", "+str(cross_v_y)+", "+str(cross_v_z)+" )"))

    e4.delete(0,'end')
    e4.insert(END,("√"+str(magn_cross_v)))

    e5.delete(0,'end')
    e5.insert(END,("√"+str(magn_A)))

    e6.delete(0,'end')
    e6.insert(END,("√"+str(magn_B)))

    e7.delete(0.1,'end')
    e7.insert(END,("sin\u207B\u00b9 (√"+str(magn_cross_v)+"                         /√"+str(magn_A*magn_B)+")")) 
    
    e8.delete(0,'end')
    e8.insert(END,(str(angle_degree))[:5]+"°")



def cosθ():
    vector_1 = str(e1.get())
    vector_2 = str(e2.get())
    v1_x = (int((vector_1)[2:4]))
    v1_y = (int((vector_1)[6:8]))
    v1_z = (int((vector_1)[10:12]))

    v2_x = (int((vector_2)[2:4]))
    v2_y = (int((vector_2)[6:8]))
    v2_z = (int((vector_2)[10:12]))

    dotproduct = (v1_x * v2_x) + (v1_y * v2_y) + (v1_z * v2_z)
    magn_A = (v1_x)**2 + (v1_y)**2 + (v1_z)**2
    magn_B = (v2_x)**2 + (v2_y)**2 + (v2_z)**2

    angle = dotproduct/((magn_A**0.5)*(magn_B**0.5))
    angle_degree = math.degrees(math.acos(angle))


    l4.place_forget()
    e3.place_forget()

    e4.place_configure(x=210,y=185)
    l3.place_configure(x=30,y=185)
    l3.config(text="Dot product       :",font=('arial 20',16,'bold'), bg="skyblue")
    e4.delete(0,'end')
    e4.insert(END,dotproduct)

    e5.delete(0,'end')
    e5.insert(END,("√"+str(magn_A)))

    e6.delete(0,'end')
    e6.insert(END,("√"+str(magn_B)))

    e7.delete(0.1,'end')
    e7.insert(END,("cos\u207B\u00b9 ("+str(dotproduct)+"                             /√"+str(magn_A*magn_B)+")")) 

    e8.delete(0,'end')
    e8.insert(END,(str(angle_degree))[:5]+"°")



# ==========lable===============

h1 = Label(root, text="IT Sem:1 Math :Micro Project",font=('arial 20',16,'bold'), bg="skyblue")
h1.place(x=90, y=10)

h2 = Label(root, text="This Math project can find Angel Between two vectors",font=('arial 20',13,'bold'), bg="skyblue")
h2.place(x=30, y=40)

h3 = Label(root, text="Made by :Makawana Mohit", bg="skyblue")
h3.place(x=330, y=560)

l1 = Label(root, text="first vector cordinate          :",font=('arial 20',16,'bold'), bg="skyblue")
l1.place(x=30, y=90)

l2 = Label(root, text="second vector cordinate    :",font=('arial 20',16,'bold'), bg="skyblue")
l2.place(x=30, y=125)

l3 = Label(root, text="cross product   :",font=('arial 20',16,'bold'), bg="skyblue")
l3.place(x=30, y=168)

l4 = Label(root, text="Magnitude of cross product :",font=('arial 20',16,'bold'), bg="skyblue")
l4.place(x=30, y=210)

l5 = Label(root, text="Magnitude of first vector       :",font=('arial 20',16,'bold'), bg="skyblue")
l5.place(x=30, y=245)

l6 = Label(root, text="Magnitude of second vector :",font=('arial 20',16,'bold'), bg="skyblue")
l6.place(x=30, y=280)

l7 = Label(root, text="Value of 	       : θ =",font=('arial 20',16,'bold'), bg="skyblue")
l7.place(x=30, y=330)

l8 = Label(root, text="Angel between two vector :θ =",font=('arial 20',16,'bold'), bg="skyblue")
l8.place(x=30, y=430)

l9 = Label(root, text="Calculate using ",font=('arial 20',16,'bold'), bg="skyblue")
l9.place(x=150, y=470)



# =========Entry Box=========

e1=Entry(root,justify=CENTER , width=12, font=('arial 20',15,'bold'))
e1.insert(END,str("( +X, +Y, +Z )"))
e1.place(x=320,y=90)

e2=Entry(root,justify=CENTER , width=12, font=('arial 20',15,'bold'))
e2.insert(END,str("( +X, +Y, +Z )"))
e2.place(x=320,y=125)

e3=Entry(root,justify=CENTER , width=12, font=('arial 20',15,'bold'))
e3.insert(END,str("( +X, +Y, +Z )"))
e3.place(x=210,y=168)

e4=Entry(root,justify=CENTER , width=7, font=('arial 20',15,'bold'))
e4.insert(END,str("|AXB|"))
e4.place(x=340,y=210)

e5=Entry(root,justify=CENTER , width=7, font=('arial 20',15,'bold'))
e5.insert(END,str("|A|"))
e5.place(x=340,y=245)

e6=Entry(root,justify=CENTER , width=7, font=('arial 20',15,'bold'))
e6.insert(END,str("|B|"))
e6.place(x=340,y=280)

e7=Text(root, width=18,height=3, font=('arial 20',15,'bold'))
e7.insert(END,str("sin\u207B\u00b9 (|AXB|                /|A||B|)"))
e7.place(x=220,y=330)

e8=Entry(root,justify=CENTER , width=7, font=('arial 20',15,'bold'))
e8.insert(END,str("360"))
e8.place(x=340,y=430)


# ============button==========

button_1 = Button(root,width=7,text="sin θ ",font=('arial 20',15,'bold') ,command=lambda:sinθ())
button_1.place(x=110,y=510)

button_2 = Button(root,width=7,text="cos θ ",font=('arial 20',15,'bold') ,command=lambda:cosθ())
button_2.place(x=270,y=510)

root.mainloop()