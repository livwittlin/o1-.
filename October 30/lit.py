import random
a=0
time = 0

def first():
    x = random.randint(1,5)
    time.sleep(x)
    print("boo")



def trick_treat():
    a=random.randint(1, 2)
    if a == 1:
        return "trick"
    if a == 2:
        return "treat"

print(trick_treat())

def three(string):
    return "spooky " + string
print(three())
