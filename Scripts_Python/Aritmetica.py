import os


import os
#Funciones
def menu():
    print("::: MENU :::")
    print("[1.] Sumar")
    print("[2.] Restar")
    print("[3.] Multiplicar")
    print("[4.] Dividir")
    print("[5.] Cancelar operación")
    
def calculadora(x, y, z):
    if z == '1' :
        ans = x + y
    elif z== '2':
        ans = x - y
    elif z == '3':
        ans= x * y
    elif z == '4':
        ans = x / y
    elif z == '5':
        print("La operación ha sido cancelada")
        ans = 0
    else:
        print("::: Opción Incorrecta :::")
        ans = 0
    
    return ans
    
#Main
os.system("clear")
n1 = int(input("Ingrese primer numero: "))
n2 = int(input("Ingrese Segundo numero: "))

menu()

op=input("::: Digíte una opción: ")
res = calculadora (n1, n2, op)
print("El resultado de la operación es: ", res)
