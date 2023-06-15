import math 
# ==========Function===============

def sinθ():
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
    print("cross product of vector1 and vector2 ")
    print("( "+str(cross_v_x)+", "+str(cross_v_y)+", "+str(cross_v_z)+" )\n")
    print("Magnitude of cross product :")
    print("|"+str(magn_cross_v)+"|\n")

    print("Magnitude of vector 1 :")
    print("|"+str(magn_A)+"|\n")

    print("Magnitude of vector 2 :")
    print("|"+str(magn_B)+"|\n")

    print("value of :θ = ",("sin\u207B\u00b9 (√"+str(magn_cross_v)+"\n                     /√"+str(magn_A*magn_B)+")"))
    print("degree of :θ = \t",angle_degree)


def cosθ():
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
    print("dot product of vector1 and vector2 ")
    print(dotproduct,"\n")

    print("Magnitude of vector 1 :")
    print("|"+str(magn_A)+"|\n")

    print("Magnitude of vector 2 :")
    print("|"+str(magn_B)+"|\n")

    print("value of :θ = ",("sin\u207B\u00b9 ("+str(dotproduct)+"\n                     /√"+str(magn_A*magn_B)+")"))
    print("degree of :θ = \t",angle_degree)


while True:
    print("this project is to find angel betweem two vector\n")
    print("enter value of vector in ( +X, +Y, +Z )")
    vector_1 = input("vector 1 value in ( +X, +Y, +Z ) formate\n")
    vector_2 = input("vector 2 value in ( +X, +Y, +Z ) formate\n")
    choice = int(input("now enter your choice \n 1 for using sinθ \n 2 for using cosθ \n"))

    if choice == 1:
        sinθ()
    elif choice == 2:
        cosθ()
    else:
        print("wrong input run the code again and try again ")
    loop = input("enter 'yes' if you want to run code again else enter anything\n")
    if loop == 'yes':
        continue
    else:
        break
