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