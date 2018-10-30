# this is the variable that asks what your speed was
s=int(input("whats your speed"))
if s<51:
    print("your safe")
# if your speed is less then the speed limit your safe from fines
elif s<71:
    print("your fine is 45$")
elif s<80:
    print("your fine is 75$")
elif s>81:
    print("your fine is 150$")
# if the speed was greater then the max limit it still cost 150$
