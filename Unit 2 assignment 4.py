# defineing all the variables and its going to ask how many cookies you want to buy
cookies=int(input("how many cookies would you like to purchase"))
single = int(0)
box = int(0)
crate = int(0)
# if the number of cookies you want to purchase is over 240 it will purchase a crate for you
while cookies>239:
    cookies = cookies-240
    crate = crate+1
print("the amount of crates is " + str (crate))
# if the cookies are more then 1 you can purchase a box which has 12
while cookies>11:
    cookies = cookies-12
    box = box+1
print("the amount of boxes is " + str (box))
# all the leftover cookies go here and it charges you 0.5 per
while cookies>=1:
    cookies = cookies-1
    single = single+1
print("the amount of single cookies is " + str (single))

int(crate)
int(box)
int(single)
# this creates the total by times the idem by the prices and adding them together
total = 0
total = crate*80 + box*5 + single*0.5
print("the total is " + str (total))




