# these are you health points and your opponents health points
hp = 100
enemyhp = 100

# this lets your opponet use a move at random
import random

# these are the level 2 water moves if you pick the pokemon totidile
wgun = 40
bubble = 30

# these are the level 2 fire move if you pick the pokemon Cyntiquil
flame_wheel = 35
fire = 40

# this picks the pokemon you use for level 2
p=0

# these are the enemy moves on level one
ember = 30
bite = 20

# these are your moves on level one
tackle=25
thunder = 30

# all pokemon use heal and it adds 20 life points to your hp
heal = 20

# this controls the game itself
g=0

# this controls your moves
m=0
e=0

# this introduces level 1 and shows what pokemon you are using and what pokemon you will be fighting
print("A wild Charizard  has appeared")
print("go Pikachu, prepare to battle")

# g controls the entire game when its = to 0 its level 1
while g == 0:

    # M starts as 0 but when you pick a move it changes and it triggers an if statement depending on what move you pick
    while m == 0:
        m = int(input("what move would you like to use, press 1 for tackle, press 2 for thunder, or press 3 for heal"))

        # this is the first move tackle if you type 1 then it takes the enemy hp and subtracts it by tackle
        if m == 1:
            enemyhp = enemyhp - tackle
            int(enemyhp)
            print("enemy took 25 damage")
            # this displays the opponents health so you can see how much damage you need to knock them out
            print("opponent health = " +str(enemyhp))
            # this resets the move to 0 and restarts the move sequence so you can choose another move
            m = 0

        # this move activates thunder which does more damge to the opponets hp then tackle
        elif m == 2:
            enemyhp = enemyhp - thunder
            int(enemyhp)
            print("enemy took 30 damage")
            print("opponent health = " +str(enemyhp))
            m=0

        # this is the heal mechanic so if you pick 3 it takes you hp and adds the heal variable
        elif m == 3:
            hp = hp + heal # it heals your hp by 20 points and you can do this as many times as possible
            int(hp)
            print("you healed 20 points")
            print("your health = " +str(hp))
            """this displays your current health and the cool thing about this move is you can 
            get you health up as high as you can so if you use it enogh you can make your hp go from 100 to 200"""
            m=0

        else:  # if you type a wrong number this will tell you that and you will need to reset
            print("not a valid move please try again")

        #  if your hp goes below 0 you have lost and your opponent won so you can rematch them
        if hp < 1:
            g = int(input("game over you lost press 0 for rematch"))
            #  this restores you health for the rematch
            hp = 100
            enemyhp = 100

        # if the enemys hp goes below 0 you win so you have the option to rematch or go to level 2
        elif enemyhp < 1:
            g = int(input("congratulations you win press 0 for rematch or press 4 for next level"))
            # this stops the first move set so you can use a diffrent set of moves
            if g == 4:
                m=5
            hp = 100
            enemyhp = 100
        # this is the opponents move that the ai will use
        move1 = 0
    while move1 == 0:
        move1=random.randint(1,3) # this makes the opponent choose a random move from 3 options
        if move1 == 1:
            hp = hp - ember
            int(hp)
            print("charizard used ember")
            # this shows your current health ssince the opponet took away some of your hp when they use there move
            print("your health = " +str(hp))

        elif move1 == 2:
            hp = hp - bite
            int(hp)
            print("charizard used bite")
            print("your health = " +str(hp))

        elif move1 == 3: # the ai also has acsess to the heal mechanic that was explained above
            enemyhp = enemyhp + heal
            int(enemyhp)
            print("charizard healed 20 points")
            print("opponents health = " +str(enemyhp))

        if hp < 1:
            g=1
            g=int(input("game over you lost press 0 for rematch"))
            hp = 100
            enemyhp = 100

        elif enemyhp < 1:
            g=1
            g = int(input("congratulations you win press 0 for rematch press 4 to go to the next level"))
            hp = 100
            enemyhp = 100
""" this is level 2 where you can select your pokemon and move set and then fight a harder pokemon. all the moves do 
more damage then level one and its a lot harder to beat your oppoenet"""
while g == 4:
        print("welcome to level 2")
        #  you can pick a pokemon this time and they have diffrent moves you can use
        g=int(input("press 5 for the water type Totidile or press 6 for the fire pokemon Cyntiquil"))
        hp = 100
        enemyhp = 100

#  if you pick The water pokemon totidile you will fight the fire pokemon cyntiquil
while g == 5:
    m = int(input("press 1 for water gun, press 2 for bubble, or press 3 to heal "))
    # the move mechanics work the same as level one they just do more damage and take away more hp
    if m == 1:
        enemyhp = enemyhp - wgun
        int(enemyhp)
        print("enemy took 40 damage")
        print("opponent health = " + str(enemyhp))

    elif m == 2:
        enemyhp = enemyhp - 30
        int(enemyhp)
        print("enemy took 30 damage")
        print("opponent health = " + str(enemyhp))

    elif m == 3:
        hp = hp + heal
        int(hp)
        print("you healed 20 points")
        print("your health = " + str(hp))

    else:
        print("not a valid move please try again")
    #  if you lose you can rematch level 2
    if hp < 1:
        g = 1
        g = int(input("game over you lost press 4 for rematch"))
        hp = 100
        enemyhp = 100

    elif enemyhp < 1:
        #  if you beat level 2 you have finished the game
        print("congratulations you beat the game")
        g = 1
        # you can contiune playing level 2 if you press 4
        g = int(input("congratulations press 4 for level 2 rematch"))
        hp = 100
        enemyhp = 100
    if g == 4:
        print("welcome to level 2")
        g=int(input("press 5 for the water type Totidile or press 6 for the fire pokemon Cyntiquil"))
        hp = 100
        enemyhp = 100
    move2 = 0
    m = 0
    e = 0
    # this is the same randomised mechanic as above
    while move2 == 0:
        move2 = random.randint(1, 3)
    if move2 == 1:
        hp = hp - flame_wheel
        int(hp)
        print("cyntiquil used ember")
        print("your health = " + str(hp))

    elif move2 == 2:
        hp = hp - fire
        int(hp)
        print("cyntiquil used fire beam")
        print("your health = " + str(hp))

    elif move2 == 3:
        enemyhp = enemyhp + heal
        int(enemyhp)
        print("cyntiquil healed 20 points")
        print("opponents health = " + str(enemyhp))

    if hp < 1:
        g = 1
        g = int(input("game over you lost press 0 for rematch"))
        hp = 100
        enemyhp = 100

    elif enemyhp < 1:
        g = 1
        g = int(input("congratulations you win press 4 for level 2 rematch"))
        hp = 100
        enemyhp = 100

    if g == 4:
        print("welcome to level 2")
        g=int(input("press 5 for the water type Totidile or press 6 for the fire pokemon Cyntiquil"))
        hp = 100
        enemyhp = 100


while g == 6:  # now you are playing as the fire pokemon cyntiquil
    m = int(input("press 1 for Flame wheel press 2 for fire beam, or press 3 to heal "))
    if m == 1: # same move mechanics
        enemyhp = enemyhp - flame_wheel
        int(enemyhp)
        print("enemy took 35 damage")
        print("opponent health = " + str(enemyhp))

    elif m == 2:
        enemyhp = enemyhp - fire
        int(enemyhp)
        print("enemy took 40 damage")
        print("opponent health = " + str(enemyhp))

    elif m == 3:
        hp = hp + heal
        int(hp)
        print("you healed 20 points")
        print("your health = " + str(hp))

    else:
        print("not a valid move please try again")

    if hp < 1:
        g = 1
        g = int(input("game over you lost press 0 for rematch"))
        hp = 100
        enemyhp = 100

    elif enemyhp < 1:
        g = 1
        g = int(input("congratulations you win  press 4 for level 2"))
        hp = 100
        enemyhp = 100
    if g == 4:
        print("welcome to level 2")
        g=int(input("press 5 for the water type Totidile or press 6 for the fire pokemon Cyntiquil"))
        hp = 100
        enemyhp = 100

    move3 = 0
    m = 0
    e = 0
    while move3 == 0:
        move3 = random.randint(1, 3)
    if move3 == 1:
        hp = hp - wgun
        int(hp)
        print("totidile used water gun")
        print("your health = " + str(hp))

    elif move3 == 2:
        hp = hp - bubble
        int(hp)
        print("totidile used bubble")
        print("your health = " + str(hp))

    elif move3 == 3:
        enemyhp = enemyhp + heal
        int(enemyhp)
        print("totidile healed 20 points")
        print("opponents health = " + str(enemyhp))

    if hp < 1:
        g = 1
        g = int(input("game over you lost press 0 for rematch"))
        hp = 100
        enemyhp = 100
    elif enemyhp < 1:
        g = 1
        g = int(input("congratulations you win press 0 for level one or press 4 for level 2"))
        hp = 100
        enemyhp = 100

    if g == 4:
        print("welcome to level 2")
        g=int(input("press 5 for the water type Totidile or press 6 for the fire pokemon Cyntiquil"))
        hp = 100
        enemyhp = 100



















