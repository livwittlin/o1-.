n=int(0)
import random
def doubleEven(n):
    if n % 2 == 0:
        n = n*2
        return (n)
    else:
        return "-1"


print(doubleEven(n = int(input("put in a number"))))

g=int(0)

def grade(g):
    if g < 50:
        return "F"
    if g < 66:
        return "C"
    if g > 92:
        return "A+"

    else:
        print("error")


print(grade(g = int(input("put in your percent"))))

num1 = 0
num2 = 0
num3 = 0

def largestNum(num1, num2, num3):
    num1 = int(input("input number 1"))
    num2 = int(input("input number 2"))
    num3 = int(input("input number 3"))
    if num1 > num2:
        if num1 > num3:
            return num1
        if num3 > num1:
            return num3
    if num2 > num3:
        return num2
    if num3 > num2:
        return num3


print(largestNum(10, 20, 30))


def sumDice(Dice, numRolls):