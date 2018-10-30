average=0
classes=int(input("how many classes did you take"))
# how many classes you take and this will also be the number we divide by when finding the avrage

for x in range(0,classes):
    average=average+int(input("type your averages"))
    # put in the diffrent class averages and the code adds all the numbers and makes a total
int(average)
average=average/classes
# this takes the totaled avrages and divides them by the amount of classes
print(average)