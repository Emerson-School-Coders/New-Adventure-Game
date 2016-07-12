lives=5
gold=10
damagem=1
special=[]
import time
import random
import math
def rendscreen(text):
    cls()
    print("--------------------------------------------------------------------------------")
    print("Gold: "+ str(gold) + " Lives: " + str(lives))
    print("Special items: "+str(special))
    print("--------------------------------------------------------------------------------")
    print(text)
def rendscreenf():
    cls()
    print("--------------------------------------------------------------------------------")
    print("Gold: "+ str(gold) + " Lives: " + str(lives))
    print("Special items: "+str(special))
    print("Health: "+str(health)+" Enemy Health: "+str(enemyh))
    print("--------------------------------------------------------------------------------")
def cls():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
cls()
print("Press enter to go to the next screen.")
input()
cls()
print("--------------------------------------------------------------------------------")
print("-----------Welcome to the forest------------------------------------------------")
print("-----------Are you ready?-------------------------------------------------------")
print("--------------------------------------------------------------------------------")
print("Press Enter to Continue...")
input("")
cls()
lives=5
gold=10
move="None"
rdone=0
ldone=0
while move!="L" and move!="l" and move!="R" and move!="R" and move!="s" and move!="S":
    rendscreen("You are walking in a forest.  You come to a part you don't know. You go ahead.")
    move=input("Do you go left(L), right(R) or straight(S)")
    if move=="L" or move=="l":
        if ldone==1:
            rendscreen("You've already gone here!")
            input()
            move="0"
        else:
            rendscreen("You found a chest! Inside it was 5 bars of gold.(enter to continue)")
            input()
            gold +=5
            rendscreen("It's at a dead end, however. You walk back.")
            input()
            move="0"
            ldone=1
    elif move=="R" or move=="r":
        if rdone==1:
            rendscreen("You've already gone here!")
            input()
            move="0"
        else:
            rendscreen("You walk into a trap and lose a life.(enter to continue)")
            input()
            lives+=-1
            rendscreen("You walk back.")
            input()
            move="0"
            rdone=1
rendscreen("You walk forward for a while.(enter to continue)")
input()
rendscreen("The ground begins to shake...(enter to continue)")
input()
cls()
print("Louder...")
time.sleep(1)
rendscreen("You come up to a monster!")
time.sleep(1)
rendscreen("'I will eat you!'")
time.sleep(1)
rendscreen("How to fight: Press K to kick and P to punch.")
input()
rendscreen("When it's your enemy's turn, hope for the best!")
input()
rendscreen("Press enter to start.")
input()
health=1000
enemyh=200
while enemyh>0:
    rendscreenf()
    fmove="0"
    while fmove!="k" and fmove!="K" and fmove!="p" and fmove!="P" and fmove!="adminpass":
        fmove=input("K to kick or P to punch")
    if fmove=="K" or fmove=="k":
        sub=math.floor(random.random()*10)+5
        enemyh=enemyh-sub*10
        print("Damage dealt: "+ str(sub*10))
        input()
    elif fmove=="adminpass":
        enemyh=0
    else:
        sub=math.floor(random.random()*10)
        enemyh+=-sub*18
        print("Damage dealt: "+ str(sub*18))
        input()
    rendscreenf()
    time.sleep(.2)
    if enemyh>0:
        health+=-math.floor(random.random()*100)
        health+=-60
        print("Monster attacks! Damage dealt: "+ str(sub+60))
        input()
rendscreen("You won the battle!")
input()
rendscreen("The monster had 20 gold and you gained two lives from defeating him!")
gold+=20
lives+=2
input()
rendscreen("You continue along the path.")
input()
ebhealth=0
special=[]
berries=0
while berries != "y" and berries != "Y" and berries != "N" and berries != "n":
    rendscreen("You find some berries.  Do you eat them? Y for yes and N for no.")
    berries=input()
if berries=="y" or berries=="Y":
    rendscreen("Under the leaves, you found a glove!  It grants +50 health in all battles!")
    ebhealth+=50
    special.append("Glove")
    input()
    rendscreen("After eating some berries, you continue walking.")
else:
    rendscreen("You continue walking.")
input()
river="0"
while river!="Y" and river!="y" and river!="N" and river!="n": 
    rendscreen("After walking for quite some time, you come to a river.  There's a bear right behind you.  Do you try to cross the river? Y/N")
    river=input()
if river=="Y" or river=="y":
    rendscreen("You manage to cross the river, but you get sick and lose a life.")
    lives+=-1
else:
    rendscreen("You stay and fight the bear!")
    input()
    health=1000+ebhealth
    enemyh=400
    while enemyh>0:
        rendscreenf()
        fmove="0"
        while fmove!="k" and fmove!="K" and fmove!="p" and fmove!="P" and fmove!="adminpass":
            fmove=input("K to kick or P to punch")
        if fmove=="K" or fmove=="k":
            sub=math.floor(random.random()*10)+6
            enemyh=enemyh-sub
            print("Damage dealt: "+ str(sub))
            input()
        elif fmove=="adminpass":
            enemyh=0
        else:
            sub=math.floor(random.random()*10)
            enemyh+=-sub*1.85
            print("Damage dealt: "+ str(sub*1.85))
            input()
        rendscreenf()
        time.sleep(.2)
        if enemyh>0:
            sub=math.floor(random.random()*10)*1.4
            health+=-sub
            health+=-4
            print("Bear attacks! Damage dealt: "+ str(sub+4))
            input()
        if health<0:
            lives+=-1
            health=1000+ebhealth
    rendscreen("You won the battle!!!")
    input()
    rendscreen("You keep the fur coat from the bear.  It gives you +200 health in all battles!")
    input()
    ebhealth+=200
    special.append("Fur Coat")
    rendscreen("You decide to put down a log and cross the river.")
input()
rendscreen("Now that you're across the river, you decide to start exploring.")
input()
move="0"
lgone="0"
rgone="0"
while move!="L" and move!="l" and move!="R" and move!="R" and move!="s" and move!="S":
    rendscreen("Do you go left(L), right(R) or straight(S)")
    move=input()
    if move=="l" or move=="L":
        if lgone=="0":
            lgone="1"
            rendscreen("You go left. You find some food.  You you eat it? Y/N")
            food1=0
            while food1 != "y" and food1 != "Y" and food1 != "N" and food1 != "n":
                food1=input()
            if food1=="y" or food1=="Y":
                rendscreen("It was poisoned!  Lose a life")
                lives+=-1
                input()
            else:
                rendscreen("You decide not to eat and you go back.")
                input()
        else:
            rendscreen("You've already gone this way!")
            input()
        move="0"
    elif move=="r" or move=="R":
        if rgone=="0":
            rgone="1"
            rendscreen("You found a chest!  Inside it is 25 gold!")
            gold+=25
            input()
        else:
            rendscreen("You've already gone this way!")
            input()
        move="0"
    else:
        rendscreen("There's a giant!")
        input()
        rendscreen("'I demand 40 gold or I will FIGHT YOU!'")
        input()
        fight="0"
        if gold<40:
            rendscreen("You must fight the giant.")
            giantf="1"
            input()
        else:
            watf="?"
            rendscreen("Do you want to fight? Y/N")
            while watf!="Y" and watf!="y" and watf!="N" and watf!="n":
                watf=input()
            if watf=="y" or watf=="Y":
                giantf="1"
            else:
                giantf="0"
if giantf=="1":
    health=1000+ebhealth
    enemyh=1300
    while enemyh>0:
        rendscreenf()
        fmove="0"
        while fmove!="l" and fmove!="k" and fmove!="K" and fmove!="p" and fmove!="P" and fmove!="adminpass":
            fmove=input("K to kick or P to punch")
        if fmove=="k" or fmove=="K":
            sub=math.floor(random.random()*10)+6
            enemyh+=-sub
            print("Damage dealt: "+ str(sub))
            input()
        elif fmove=="adminpass":
            enemyh=0
        elif fmove=="l":
            health=-1
        else:
            sub=math.floor(random.random()*10)
            enemyh+=-sub*1.9
            print("Damage dealt: "+ str(sub*1.9))
            input()
        rendscreenf()
        if enemyh>0:
            sub=math.floor(random.random()*10)*1.5
            health+=-sub
            health +=-6
            print("Giant attacks!  Damage dealt: "+ str(sub+6))
            input()
        if health<0:
            lives+=-1
            health=1000+ebhealth
            print("You lost a life.")
            input()
    rendscreen("You defeated the giant!")
    input()
    rendscreen("The giant was hoarding 200 gold!")
    input()
    gold+=200
    rendscreen("You also gain a life from defeating the giant.")
    input()
    lives+=1
    rendscreen("The giant also had a spear.  It grants double damage in all battles!")
    damagem+=1
    special.append("Spear")
    input()
else:
    rendscreen("You decided not to fight the giant and pay him 40 gold.")
    gold+=-40
    input()
rendscreen("You continue walking, now that you're past the giant.")
input()
rendscreen("On the path, you find a bomb!  Use it once to destroy an enemy.  You can only use it once, however, so use it wisely")
special.append("Bomb")
input()
rendscreen("Now that you have the bomb, you continue walking.")
#special.remove("Bomb")###How to remove bomb!!!
input()
rendscreen("You come up to a dragon!")
print("    \ |  (  \ ( \.(               )")
print("                      _____")
print("  \  \ \  `  `   ) \             (  ___                 / _   \\")
print(" (_`    \+   . x  ( .\            \/   \____-----------/ (o)   \_")
print("- .-               \+  ;          (  O                           \____")
print("                          )        \_____________  `              \  /")
print("(__                +- .( -'.- <. - _  VVVVVVV VV V\                 \/")
print("  .    /./.+-  . .- /  +--  - .     \______________//_              \_______")
print("(_____            ._._: <_ - <- _  (--  _AAAAAAA__A_/                  |")
print("  (__ ' /x  / x _/ (                                  \___'          \     /")
print(" , x / ( '  . / .  /                                      |           \   /")
print("    /  /  _/ /    +                                      /              \/")
print("   '  (__/                                             /                  \\")
input()
if giantf=="1":
    rendscreen("'You killed my good friend the giant!  I will EAT YOU!'")
    input()
    health=1000+ebhealth
    enemyh=1500
    while enemyh>0:
        rendscreenf()
        fmove="0"
        if "Bomb" in special:
            while fmove!="l" and fmove!="k" and fmove!="K" and fmove!="p" and fmove!="P" and fmove!="adminpass" and fmove!="B" and fmove!="b":
                fmove=input("K to kick or P to punch or B to use bomb")
        else:
            while fmove!="l" and fmove!="k" and fmove!="K" and fmove!="p" and fmove!="P" and fmove!="adminpass":
                fmove=input("K to kick or P to punch")
        if fmove=="k" or fmove=="K":
            sub=math.floor(random.random()*10)+6
            enemyh+=-sub*damagem
            print("Damage dealt: "+ str(sub*damagem))
            input()
        elif fmove=="adminpass":
            enemyh=0
        elif fmove=="l":
            health=-1
        elif fmove=="B" or fmove=="b":
            special.remove("Bomb")
            enemyh=0
        else:
            sub=math.floor(random.random()*10)
            enemyh+=-sub*1.9*damagem
            print("Damage dealt: "+ str(sub*1.9*damagem))
            input()
        rendscreenf()
        if enemyh>0:
            sub=math.floor(random.random()*10)*1.5
            health+=-sub
            health +=-6
            print("Dragon attacks!  Damage dealt: "+ str(sub+6))
            input()
        if health<0:
            lives+=-1
            health=1000+ebhealth
            print("You lost a life.")
            input()
    rendscreen("You beat the dragon!")
    input()
else:
    rendscreen("Thank you for paying the giant.  You may pass.")
    input()
    rendscreen("The dragon lets you pass, and you continue on your way.")
    input()
rendscreen("You found another bomb on the path!")
special.append("Bomb")
input()
