import math
a=0
b=0
c=0
d=0

def take_num():
    a=int(input("number 1"))
    b=int(input("number 2"))

    return a + b

print(take_num())


def compare():
    c = int(input("number 1"))
    d = int(input("number 2"))
    if c == d:
        print("true")
    else:
        print("false")

compare()

def pythagoream():
        a=int(input("enter number one"))
        b=int(input("enter number two"))
        # this part does the math they times and be by themselves and then adds them to create d then d is square rooted
        a = a*a
        b = b*b
        d = a+b
        int(d)
        d = (math.sqrt(d))
        print(round(d,2))

pythagoream()

def tip():
        t = int(input("what was your bill total"))
        p=int(input("what percent would you like to tip"))
        p = p/100
        t = t*p
        # this rounds the total tip to two decimal places
        print("your tip amount is " + str(round(t,2)))
        r = 0
tip()

def cvsf():
        c=0
        f=0
        # this determines if your converting celsius to fahrenheit or vice versa
        c = int(input("for celsius to fahrenheit type 1 for fahrenheit to celsius type 2"))
        if c == 1:
            # you input your temperature in celsius and it times it by 1.8 and adds 32 to create the fahrenheit temp
            y=int(input("what is the celsius temperature"))
            y=y*1.8
            y=y+32
            print("the temperature in fahrenheit is " + str (round(y, 2)))
            r = 0

        if c == 2:
            # this takes you fahrenheit temp and converts it to celsius by dividing by 1.8 and then taking away 32
            f=int(input("what is the fahrenheit temperature"))
            f = f/1.8
            f = f-32
            # then it prints you final answer rounded to 2 decimals
            print("the temperature in celsius is " + str (round(f, 2)))
            r = 0
cvsf()