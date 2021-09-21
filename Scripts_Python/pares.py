import os

os.system("clear")

print ("Ingrese primer numero: ")
n1 = int(input())
n2 = int(input("Ingrese segundo numero: "))

if n1 > n2 :
    print("El mayor es: ", n1)
else :
    print("El mayor es: ", n2)

suma = n1+n2

print ("La suma es: ", suma)
