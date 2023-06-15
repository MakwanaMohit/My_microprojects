import sem2math as sm
import pyperclip ,os ,subprocess
from tkinter import *
from tkinter import filedialog
from threading import Timer
from tkinter.messagebox import askretrycancel , askyesno

root = Tk()
root.title("Mohit Python Microproject")
root.geometry('450x300+450+200')
root.config(bg="skyblue")

# ============Functions============

def start_menu():
    '''
    main function that start the window 
    '''
    erase_all()
    global path1,path2 ,input_mat1 ,input_mat2,ite
    path1 = ''
    path2 = ''
    input_mat1 = []
    input_mat2 = []
    ite = 0
    if os.path.exists('outputdemo.txt'):
        os.remove('outputdemo.txt')  
    if os.path.exists('input_math_input.txt'):
        os.remove('input_math_input.txt')  
    h1.config(text="IT Sem:1 Python :Micro Project",font=('arial 20',12,'bold'), bg="skyblue")
    h1.place(x=90, y=10)
    h2.config(text="select what you want to do ?",font=('arial 20',12,'bold'), bg="skyblue")
    h2.place(x=100, y=35)
    h3.place(x=295, y=265)
    button1.config(width=13,height=2,text="transpose  ",font=('arial 10 ',10,'bold') ,command=lambda:take_input(1))
    button1.place(x=100,y=90)
    button2.config(width=13,height=2,text="multiplication  ",font=('arial 10 ',10,'bold') ,command=lambda:take_input(2,1))
    button2.place(x=230,y=90)
    button3.config(width=13,height=2,text="invers  ",font=('arial 10 ',10,'bold') ,command=lambda:take_input(3))
    button3.place(x=100,y=150)
    button4.config(width=13,height=2,text="indenty matrix  ",font=('arial 10 ',10,'bold') ,command=lambda:take_input(4))
    button4.place(x=230,y=150)
    button5.config(height=0,width=0,text="  Main Window  ",font=('arial 10 ',8,'bold') ,command=lambda:main_menu())
    button5.place(x=20,y=260)

def main_menu():
    '''
    this function is for return back in main menu
    '''
    reset()
    Timer(1,start_menu).start()

def erase_all():
    '''
    this function clear the window and remove anything from the window
    '''
    root.bind('<Return>',lambda event:None)
    h1.place_forget()
    h2.place_forget()
    h3.place_forget()
    e1.place_forget()
    button0.config(text='',command=NONE)
    button1.config(text='',command=NONE)
    button2.config(text='',command=NONE)
    button3.config(text='',command=NONE)
    button4.config(text='',command=NONE)
    button0.place_forget()
    button1.place_forget()
    button2.place_forget()
    button3.place_forget()
    button4.place_forget()

def reset():
    '''this functiion is compulsory run when we have to reset the code '''
    global ite
    ite = 27

def close_window():
    '''this function can terminate the whole code'''
    erase_all()
    reset()
    # root.quit()
    root.destroy()

def error_message(function,title_ ,message_):
    '''
    this function is for genreating error message 
    '''
    reset()
    ans = function(
        title=title_,
        message=message_
    )
    if ans:
        start_menu()
    else:
        close_window()

# ----------------inputcode started-------------------

def take_input(choice,subchoice = 1):
    erase_all()

    h1.config(text="select how do you want to enter you matrix:"+str(subchoice)+"?",font=('arial 20',12,'bold'), bg="skyblue")
    h1.place(x=50,y=20)
    button1.config(width=29,height=0,text="enter from exiting text file",font=('arial 10 ',10,'bold') ,command=lambda : input_from_txt_file(subchoice,False))
    button1.place(x=60,y=70)
    button2.config(width=29,height=0,text="create a new text file",font=('arial 10 ',10,'bold') ,command=lambda : input_from_txt_file(subchoice,True))
    button2.place(x=60,y=100)
    button3.config(height=0,width=29,text="paste from your keyboard",font=('arial 10 ',10,'bold') ,command= lambda :input_from_clipboard(subchoice))
    button3.place(x=60,y=130)
    global ite
    def func():
        global ite
        print(ite)
        if subchoice ==1 and len(input_mat1) > 0 or subchoice == 2 and len(input_mat2) > 0:
            erase_all()
            ite = 0
            if choice == 1: transpose()

            elif choice ==2 : 
                if subchoice == 1:
                    take_input(2,2)
                else:
                    multiplication()

            elif choice ==3 :
                invers()

            elif choice ==4 :
                indenty()

            elif choice ==2 : indenty()
        else:
            if ite <25:
                Timer(1,func).start()
                ite = ite+1
            elif ite == 27:
                pass
            else:
                error_message(
                    function=askyesno,
                    title_='time limit expire',
                    message_='you didn\'t do anithing until 25 sec, are you want to keep this window on ?'
                )  
    func()

def edit_file(f_path):
    global ite
    ite = -35
    subprocess.Popen(['notepad.exe',str(f_path)])
def input_from_txt_file(mat_choice,new_file_choice):
    erase_all()
    try:
        if new_file_choice:
            f_path = str(os.getcwd())+str('\\input_math_input.txt')
            f1 = open(f_path,'w')
            f1.close()
                
        else:
            f_path = get_file_path()

        if len(f_path)>0:
            h1.config(text='path of your input file is given below')
            h1.place(x=50,y=30)
            c_path = f_path[:50]+'-\n\t'+f_path[50:95]+'-\n\t'+f_path[95:]
            h2.config(text=c_path)
            h2.place(x=10,y=60)
            button1.config(text='edit my file',command=lambda:edit_file(f_path))
            button1.place(x=50,y=150)
            button2.config(text='Enter',command=lambda:txt_file_to_array(f_path,mat_choice))
            button2.place(x=50,y=180)
            root.bind('<Return>',lambda event:txt_file_to_array(f_path,mat_choice))
            
        else:
            raise ValueError
    except ValueError:
        reset()
        error_message(
            function=askretrycancel,
            title_='input error',
            message_='you didnt enter any correct directory for file.\n are you want to run the code again ?'
        )

def txt_file_to_array(m_path,mat_choice):
    '''
    this function is for input from txt file
    '''
    global path1,path2 , input_mat1 ,input_mat2
    try:
        with open(m_path,'r+') as file1:
            dat = file1.read()
            if len(dat)<1:
                error_message(
                    function=askretrycancel,
                    title_= 'empty file error',
                    message_= 'there is nothing in your file,\n first type your matrix in yor txt file then run this again'
                )
            if mat_choice == 1:
                input_mat1 = sm.tuple_list(sm.str_array_to_array(dat))
                path1 = m_path
                return input_mat1 , path1
            else:
                input_mat2 = sm.tuple_list(sm.str_array_to_array(dat))
                path2 = m_path
                return input_mat2 , path2
    except:
        error_message(
            function=askretrycancel,
            title_='file error',
            message_='these is something wrong with your file \nnote that there is only matrix with proper order present in your file. else it throw this error'
        )

def input_from_clipboard(mat_choice):
    '''
    this function is for input from txt file
    '''
    global  input_mat1 , input_mat2
    erase_all()
    h1.config(text='first you have to copy your matrix in clipboard,\nkeep your matrix at 1st postion\n then click paste button')
    h1.place(x=30,y=30)
    button1.config(text='paste',command=lambda: paste(mat_choice))
    button1.place(x=100,y=150)
    root.bind('<Return>',lambda event:paste(mat_choice))

def paste(mat_choice):
    global input_mat1,input_mat2
    try:
        if mat_choice == 1:
            input_mat1 = sm.tuple_list(sm.clipboard_input())
            if len(input_mat1)<1:
                error_message(
                    function=askretrycancel,
                    title_= 'empty copy error',
                    message_= 'there is nothing in your clipboard, first copy your matrix in your clipboard at first postion then run this again'
                )
            else:return input_mat1
        else:
            input_mat2 = sm.tuple_list(sm.clipboard_input())
            if len(input_mat2)<1:
                error_message(
                    function=askretrycancel,
                    title_= 'empty copy error',
                    message_= 'there is nothing in your clipboard, first copy your matrix in your clipboard at first postion then run this again'
                )
            else:return input_mat2
    except:
        reset()
        error_message(
            askretrycancel,
            title_='paste error',
            message_='there is some issue during inputing your matrix.\n copy only matrix without any space or any char. \n are you want to run again ?'
        )
def transpose():
    '''transpose of matrix '''
    o_m = sm.transpose(input_mat1)
    pyperclip.copy(str(o_m))
    give_output(input_mat1,input_mat2,o_m,1)

def multiplication():
    try:
        o_m = sm.multiplication(input_mat1,input_mat2)
        if type(o_m) == ValueError:
            raise ValueError(o_m)
        pyperclip.copy(str(o_m))
        give_output(input_mat1,input_mat2,o_m,2)
    except ValueError as e:
        error_message(
            function=askretrycancel,
            title_='multiplication error',
            message_=str(e)
        )


def invers():
    try:
        o_m = sm.invers_matrix(input_mat1)
        if type(o_m) == ValueError:
            raise ValueError(o_m)
        pyperclip.copy(str(o_m))
        give_output(input_mat1,input_mat2,o_m,2)
    except ValueError as e:
        error_message(
            function=askretrycancel,
            title_='matrix error',
            message_=str(e)
        )


def indenty():
    try:
        o_m = sm.indentity_matrix(input_mat1)
        if type(o_m) == ValueError:
            raise ValueError(o_m)
        pyperclip.copy(str(o_m))
        give_output(input_mat1,input_mat2,o_m,2)
    except ValueError as e:
        error_message(
            function=askretrycancel,
            title_='matrix error',
            message_=str(e)
        )

def get_file_path():
    '''
    this code returns the file path given by user
    '''
    root.file = filedialog.askopenfilename(initialdir="C:\\Users\\makawana mohit\\Desktop",title="Select A File", filetypes=(("text file", "*.txt"),("all files", "*.*")))
    return root.file

# ---------------------OutPut code started -------------------------
    

def save_in_file(inp_mat1,inp_mat2,output_mat,file_path,choice,mode = 'w+'):
    with open(file_path,mode) as op_f:
        op_f.write('\n\npython microproject made by:   makawana mohit :    226340316036\nthanks for using my program\n\nyour input matrix:')
        op_f.write('\ninput matrix 1\n')
        for i in inp_mat1:
            op_f.write('\n\t\t'+str(i))
        if len(inp_mat2)>0:
            op_f.write('\ninput matrix 2\n')
            for j in inp_mat2:
                op_f.write('\n\t\t'+str(j))
        if choice==1:op_f.write('\nTranspose of your matrix is given bealow')
        elif choice==2:op_f.write('\nMultification of your matrix is given bealow')
        elif choice==3:op_f.write('\nInvers of your matrix is given bealow')
        else:op_f.write('\nIndenty matrix of your matrix is given bealow')
        op_f.write('\noutput matrix:')
        for i in output_mat:
            op_f.write('\n\t\t'+str(i))
        # notpad = subprocess.Popen(['notepad.exe','C:\\Users\\makawana mohit\\Desktop\\Matrix it sem 2 math project\\empty.txt'])

def final_window(inp_mat1,inp_mat2,op_mat,ope_choice,savechoice):
    if os.path.exists('outputdemo.txt'):
        os.remove('outputdemo.txt')  
    if savechoice ==1:
        pass
    elif savechoice ==2:
        i = 0
        while True:
            path = 'math_answer_output'+str(i)+'.txt'
            if os.path.exists(path):
                i += 1
            else:
                save_in_file(inp_mat1,inp_mat2,op_mat,path,ope_choice,mode='a')
                break
    elif savechoice ==3:
        path = get_file_path()
        save_in_file(inp_mat1,inp_mat2,op_mat,path,ope_choice)
    elif savechoice ==4:
        path = get_file_path()
        save_in_file(inp_mat1,inp_mat2,op_mat,path,ope_choice,mode='a')
    else:
        if path1 != str(os.getcwd())+str('\\input_math_input.txt') and len(path1)>0:
            save_in_file(inp_mat1,inp_mat2,op_mat,path1,ope_choice,)
        if path2 != str(os.getcwd())+str('\\input_math_input.txt') and len(path2)>0:
            save_in_file(inp_mat1,inp_mat2,op_mat,path2,ope_choice,)



    erase_all()
    if savechoice!= 1:
        mo = 'Thank you for using my program\n your output is succesfully saved in file'
    else:
        mo = 'Thank you for using my program'
    h1.config(text=mo)
    h1.place(x=90,y=30)
    button5.config(height=0,width=35,font=('arial 10 ',10,'bold'))
    button5.place_configure(x=75,y=220)

def give_output(inp_mat1,inp_mat2,op_mat2,ope_choice):
    global notpad
    notpad = 1
    erase_all()
    h1.config(text='out put of your question is successfully copied\n in your keyboard\nnow select how do you want to save answer in file?')
    h1.place(x=30,y=30)

    button0.config(height=0,width=35,font=('arial 10 ',10,'bold'),command=lambda:final_window(inp_mat1,inp_mat2,op_mat2,ope_choice,1),text='don\'t save in file')
    button1.config(height=0,width=35,font=('arial 10 ',10,'bold'),command=lambda:final_window(inp_mat1,inp_mat2,op_mat2,ope_choice,2),text='create a new file and save')
    button2.config(height=0,width=35,font=('arial 10 ',10,'bold'),command=lambda:final_window(inp_mat1,inp_mat2,op_mat2,ope_choice,3),text='clear everything and save in selected file')
    button3.config(height=0,width=35,font=('arial 10 ',10,'bold'),command=lambda:final_window(inp_mat1,inp_mat2,op_mat2,ope_choice,4),text='keep the data and append in selected file')
    button4.config(height=0,width=35,font=('arial 10 ',10,'bold'),command=lambda:final_window(inp_mat1,inp_mat2,op_mat2,ope_choice,5),text='save in file from input is given')

    button0.place(x=75,y=100)
    button1.place(x=75,y=130)
    button2.place(x=75,y=160)
    button3.place(x=75,y=190)
    button5.place_forget()
    if path1 != str(os.getcwd())+str('\\input_math_input.txt') and len(path1)>0 or path2 != str(os.getcwd())+str('\\input_math_input.txt') and len(path2)>0:
        button4.place(x=75,y=220)
    save_in_file(inp_mat1,inp_mat2,op_mat2,'outputdemo.txt',ope_choice)
    notpad = subprocess.Popen(['notepad.exe','outputdemo.txt'])



# ==========lable===============

h1 = Label(root)
h2 = Label(root)
h3 = Label(root, text="Made by :Makawana Mohit\nEn. 226340316036", bg="skyblue")


# ============button==========

button0 = Button(root)
button1 = Button(root)
button2 = Button(root)
button3 = Button(root)
button4 = Button(root)
button5 = Button(root)

# =========Entry Box===========

e1=Entry(root,justify=CENTER , font=('arial 10',10,'bold'))

start_menu()

# take_input()
root.protocol('WM_DELETE_WINDOW', close_window)
root.bind('<Escape>',lambda event :close_window())
root.mainloop()
