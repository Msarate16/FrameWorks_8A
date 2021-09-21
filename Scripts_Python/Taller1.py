import os
from random import randint


def dices():
    status =True

    while status:
        dice1 = randint(0,100)
        dice2 = randint(0,100)
        print("Dado 1: ", dice1)
        print("Dado 2: ", dice2)

        if dice1 == dice2:
            status=False
            print("::: Es su primer par::: ")
        elif dice1 == dice2:
            status = False
            print("::: Es su segundo par, ha ganado")
        elif dice1 + dice2 == 100:
            
            key = input("::: Presiona cualquier tecla para lanzar los dados nuevamente :::")

dices()