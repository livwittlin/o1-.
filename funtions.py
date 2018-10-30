
import random
a = 1
b = 5
w = 1
r = 1
c=1
d=1
def hello_world():
    print("hello world")

hello_world()

def data():
    w=input("type a word")
    print(str(w))
    print(str(w))
    print(str(w))
    print(str(w))
    print(str(w))
data()

def letter():
    a=input("type a word")
    a = a.upper()
    print(a)
    return
letter()


def random():
    r = random.randint(1,100)
    b = int(input('type a lottery number'))
    c = int(input('type a lottery number'))
    d = int(input('type a lottery number'))
    if b == r:
        print("you win")
    if c == r:
        print("you win")
    if d == r:
        print("you win")


random()