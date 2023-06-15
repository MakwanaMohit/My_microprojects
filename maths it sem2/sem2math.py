import pyperclip

# =========================Functions=========================

def matrix_valid(array):
  column_check = len(array[0])
  try:
      for i in range(len(array)):
          if len(array[i]) != column_check:
              raise ValueError("you enter an invail matrix please enter an valid matrix")
  except ValueError as e:
    print(e)
    return False
  else:
      return True

def squre_valid(array):
  row_count = len(array)
  if matrix_valid(array):
      try:
          for i in range(len(array)):
              if len(array[i]) != row_count:
                  raise ValueError("this is not a squre matrix please enter squre and a valid matrix")
      except ValueError as e:
        print(e)
        return False
      else:
          return True
        
def multiplication_valid(array1,array2):
  if(matrix_valid(array1) and matrix_valid(array2)):
    try:
      if(len(array1[0]) != len(array2)):
        if(len(array2[0]) == len(array1)):
           raise ValueError("for these two matrix multiplication as AB is not possible.\nif you want to do multiplication as BA,\n then re-input values in invers form ")
        else:
           raise ValueError("these both matrix is not valid for multiplication.\nplese enter valid matrixs with matrix1 column = matrix2 row")
    except ValueError as e:
       print(e)
       return False
    else:
       return True

    

def transpose(array):
  transpose_list = []
  if matrix_valid(array):
    for i in range(len(array[0])):
      row_elements = []
      for j in range(len(array)):
        row_elements.append(array[j][i])
      transpose_list.append(row_elements)
    return transpose_list

def multiplication(array1,array2):
  multiplication_array = []
  if multiplication_valid(array1,array2):
    for i in range(len(array1)):
      row_elements = []
      for j in range(len(array2[0])):
        element = 0
        for k in range(len(array1[0])):
           value = array1[i][k]*array2[k][j]
           element = element+value
        row_elements.append(element)
      multiplication_array.append(row_elements)
      
    return multiplication_array
  

def indentity_matrix(array):
   indentity_matrix = []
   for i in range(len(array)):
      row = []
      for j in range(len(array)):
        if i != j:
           row.append(0)
        else:
           row.append(1)
      indentity_matrix.append(row)
   return indentity_matrix

def invers_matrix(array):
   array_ = array
   indentity_matrix_ = indentity_matrix(array_)
   invers_matrix = indentity_matrix_

   for i in range(len(array_[0])):#this forloop is for column 
      for j in range(len(array_)):#this is for making 1 in diagonal
         if i == j :
            element_row_multiply = 1/array_[j][i]
            for row in range(len(array_[0])):
               array_[j][row] = array_[j][row]*element_row_multiply
               invers_matrix[j][row] = invers_matrix[j][row]*element_row_multiply
   
      for j in range(len(array_)):
         if i != j :
            element_row_add = array_[j][i] * (-1)
            for row in range(len(array_[0])):
               array_[j][row] = array_[j][row] + array_[i][row]*element_row_add  
               invers_matrix[j][row] = invers_matrix[j][row] + invers_matrix[i][row]*element_row_add  
   return invers_matrix


def input_to_list(row,column):
    n = column
    main_list = []
    for i in range(1,1+row):
        a = []
        while len(a) != column:
            a = list(map(int,input("\nEnter the element for row :"+str(i)+"\t").strip().split(',')))[:n]
            if len(a) != column:
                print("you didn't enter all value for this row so please re enter this row as per your order")
        main_list.append(tuple(a))
    return tuple(main_list) 

def take_matrix_input():
    array = tuple()
    print("is your matrix in copied in your clipboard ?")
    choice = input("type yes if you have, else type no\t")
    if choice == "yes":
       mat = pyperclip.paste()
       mat_str = [i for i in mat.split(']') if i != '']
       matrix = []
       for str in mat_str:
           s_list = [i for i in str.split(',') if i != '']
           op_l = []
           for i in s_list:
               element = ''
               for j in range(len(i)):
                   if i[j] == '[' or i[j] == ']' or i[j] == '':
                       pass
                   else:
                       element = element+i[j]
               op_l.append(float(element))
           matrix.append(tuple(op_l))
       return tuple(matrix)
       

          
    else:
       while True:
          order = input("enter your matrix order in 3x3 format\t").split('x')
          row = int(order[0])
          column = int(order[1])
          if row == column:
             print("order of your matrix is:",row,"X",column)
             array = input_to_list(row,column)
             return array
          else:
             print('to find invers you have to enter a squre matrix so please enter squre matrix order')

def tuple_list(inp_mat):
   matrix1 = []

   for i in inp_mat:
      matrix1.append(list(i))
   return matrix1



