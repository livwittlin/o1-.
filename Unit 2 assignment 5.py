# this lets you square root and use other compicated math equations
import math
# defining variables
a=0
r=0
b=0
d=0
c=0
p=0
# this entire script is in a while loop so depending on what r == will select the program
while r == 0:
    r=int(input("type 1 for Quick Pythagoras, type 2 for Tip Calculator, type 3 for Temperature converter"))
    # if r == 1 it activates the pythagoras calculator
    if r==1:
        # you put in you numbers for a and b
        a=int(input("enter number one"))
        b=int(input("enter number two"))
        # this part does the math they times and be by themselves and then adds them to create d then d is square rooted
        a = a*a
        b = b*b
        d = a+b
        int(d)
        d = (math.sqrt(d))
        print(round(d,2))
        # this changes r back to 0 so you can select a different menu option
        r = 0

    elif r==2:
        # this is a tip calculator so you input what your bill was and how much you would like to tip
        t = int(input("what was your bill total"))
        p=int(input("what percent would you like to tip"))
        # this does the math so it takes the tip and makes it into a decimal then times that number by the total
        p = p/100
        t = t*p
        # this rounds the total tip to two decimal places
        print("your tip amount is " + str(round(t,2)))
        r = 0

    elif r==3:
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









