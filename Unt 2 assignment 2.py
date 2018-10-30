w = int(input("how many wins did you get"))
# you enter the amount of wins you got
if w==0:
    # if you got 0 wins you have been eliminated from the competition
    print("you have been eliminated")
elif w<3:
    print("you are in group 3")
elif w<5:
    print("you are in group 2")
    # if you go less the 4 wins but more then 2 you are in group 2
elif w<7:
    print("you are in group 1")
else:
    print("that is an invalid number of wins")
# if they inputted a number like 8 win or something unrealistic is will tell you that its invalid

