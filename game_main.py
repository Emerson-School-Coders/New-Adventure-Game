#created by Emerson-School-Coders
import runpy
import time
import random
import os
do_menu=0
def clear():
    try:
        os.system("clear")
    except:
        os.system("cls")
if __name__=="__main__":
    try:
        already_ran = open(".done","r")
        already_ran.close()
    except:
        runpy.run_path("about.py")
        #run about.py
        time.sleep(1)
        already_ran = open(".done","w")
        already_ran.write("Already Ran!!!")
        already_ran.close()
    
    try:
        save_test = open("game_save.ags","r")
        save_test.close()
        save_avaliable = 1
    except:
        save_avaliable = 0
    if save_avaliable == 1:
        save_array = []
        with open('game_save.ags', 'r') as f:
            for line in f:
                save_array.append(line.strip())
        save_array_items = []
        with open('items.ags', 'r') as f:
            for line in f:
                save_array_items.append(line.strip())
        print("Continue Save: " + save_array[0] + "?")
        continue_save = "INVALID"
        while continue_save != "Y" and continue_save != "y" and continue_save != "N" and continue_save != "n":
            continue_save=input("Y/n?")
        if continue_save=="y" or continue_save=="Y":
            print("Loading save")
            world_name=save_array[0]
            print("world_name="+save_array[0])
            gold=int(save_array[1])
            print("gold="+save_array[1])
            lives=int(save_array[2])
            print("lives="+save_array[2])
            xp=int(save_array[3])
            print("xp="+save_array[3])
            armor=int(save_array[4])
            print("armor="+save_array[4])
            attack_multiplier=int(save_array[5])
            print("attack_multiplier="+save_array[5])
            bonus_health=int(save_array[6])
            print("bonus_health="+save_array[6])
            difficulty=int(save_array[7])
            print("difficulty="+save_array[7])
            items=save_array_items
            print("items="+str(save_array_items))
            print("Game loaded from save!")
            continue=open("continue.agsl","w")
            continue.write(1)
            continue.close()
            runpy.run_path("version-"+save_array[8]+".py")
        else:
            do_menu=1
            continue=open("continue.agsl","w")
            continue.write(0)
            continue.close()
    else:
        do_menu=1
    if do_menu==1:
        start=0
        submenu=""
        main_menu=1
        while start==0:
            clear()
            print("---")
            print("Welcome to the Adventure Game!")
            print("---")
            print("Menu>"+submenu)
            if main_menu==1:
                print("(H)ow to play")
                print("(A)bout")
                print("(P)lay")
                print("(M)ods")
                print("---")
                option="NONE"
                option=input(">")
                clear()
                if option=="h" or option=="H" or option=="a" or option=="A" or option=="p" or option=="P" or option=="m" or option=="M":
                    main_menu=0
                    if option=="h" or option=="H":
                        submenu="How To Play>"
                    elif option=="a" or option=="A":
                        submenu="About>"
                    elif option=="p" or option=="P":
                        submenu="Play>"
                    else:
                        submenu="Mods>"
            elif submenu=="How To Play>":
                print("(M)ain Menu")
                print("(B)asics")
                print("(C)ombat")
                print("(I)tems")
                print("---")
                option="NONE"
                option=input(">")
                clear()
                if option=="m" or option=="M" or option=="b" or option=="B" or option=="c" or option=="C" or option=="i" or option=="I":
                    if option=="m" or option=="M":
                        submenu=""
                        main_menu=1
                    elif option=="b" or option=="B":
                        submenu="How To Play>Basics>"
                    elif option=="c" or option=="C":
                        submenu="How To Play>Combat>"
                    else:
                        submenu="How To Play>Items>"
            elif submenu=="How To Play>Basics>":
                print("(B)ack")
                print("Basics: everything you need to know to get started")
                print("The Adventure Game is a game where you make choices and they may impact what happens later.")
                print("Sometimes, you enter compat situations.  There you must fight monsters.  More on this in (C)ombat")
                print("All letters in circles are accepted as input.  For example, if a turn said 'Do you go (L)eft or (R)ight, both L and R would be accepted as input.'")
                print("Sometimes you can get items.  More on this in (I)tems")
                print("---")
                option="NONE"
                option=input(">")
                clear()
                if option=="b" or option=="B" or option=="c" or option=="C" or option=="i" or option=="I":
                    if option=="b" or option=="B":
                        submenu="How To Play>"
                    elif option=="c" or option=="C":
                        submenu="How To Play>Combat>"
                    else:
                        submenu="How To Play>Items>"
            elif submenu=="How To Play>Combat>":
                print("(B)ack")
                print("Combat: how to fight")
                print("The Adventure Game has many combat situations.  In each of them, some things are the same and some are different.")
                print("In all combat situations, you can either Kick or Punch.")
                print("Kicking does more reliable damage, while Punching has a chance to do more but also has a chance to do less.")
                print("There are some Items that give you different attacks.  For example, Staff of the Sun allows you to shoot sun rays.")
                print("Read all about these special attacks in (I)tems.")
                print("If you lose all your health, you lose a life.  If you lose all your lives, you lose the game.")
                print("Tournaments are optional to enter.")
                print("They require an investment of Gold.")
                print("If you win, you get a whole pool of prizes.")
                print("If you lose, you don't lose any lives(unlike normal fighting) but don't get your gold back.")
                print("Finally, all enemies you defeat will give you XP.")
                print("This is used to track your progress in the game.")
                print("---")
                option="NONE"
                option=input(">")
                clear()
                if option=="b" or option=="B" or option=="c" or option=="C" or option=="i" or option=="I":
                    if option=="b" or option=="B":
                        submenu="How To Play>"
                    elif option=="c" or option=="C":
                        submenu="How To Play>Combat>"
                    else:
                        submenu="How To Play>Items>"
            elif submenu=="How To Play>Items>":
                print("(B)ack")
                print("Items: 'what's that???'")
                print("The Adventure Game has many items you can get.")
                print("This page lists what they can do.")
                print("If you want a complete list, please view the (L)ist of items.")
                print("Bombs can be used once in combat, dealing a large amount of damage to the enemy.")
                print("Some items, like Chainmail Gloves, give the player armor points, reducing damage done.")
                print("Some items are used for trading, like Diamonds and Gold.")
                print("Finally, some items give you more HP in combat.")
                print("---")
                option="NONE"
                option=input(">")
                clear()
                if option=="b" or option=="B" or option=="l" or option=="L":
                    if option=="b" or option=="B":
                        submenu="How To Play>"
                    else:
                        submenu="How To Play>Items>List of Items>"
            elif submenu=="How To Play>Items>List of Items>":
                print("(B)ack")
                print("List of Items")
                print("Item                |Type      |What it does                  ")
                #20 spaces, 10 spaces, 30 spaces
                #print("                    |          |                              ")
                print("Chainmail Gloves   |Armor     |5 armor points                ")
                print("Diamond             |Trading   |Used for trading              ")
                print("Bomb                |Weapons   |One time use, deals damage     ")
                print("Staff of the Sun    |Weapons   |Shoots sun rays               ")
                print("---")
                option="NONE"
                option=input(">")
                clear()
                if option=="b" or option=="B":
                    submenu="How To Play>Items>"
            elif submenu=="About>":
                print("(M)ain Menu")
                print("Created by Emerson School Coders.")
                print("New Version of Adventure Game.")
                print("---")
                option="NONE"
                option=input(">")
                clear()
                if option=="m" or option=="M":
                    main_menu=1
                    submenu=""
            elif submenu=="Mods>":
                print("(M)ain Menu")
                print("No mods yet!")
                print("---")
                option="NONE"
                option=input(">")
                clear()
                if option=="m" or option=="M":
                    main_menu=1
                    submenu=""
            elif submenu=="Play>":
                print("(M)ain Menu")
                print("Play the Game!")
                print("(P)lay!")
                option="NONE"
                option=input(">")
                clear()
                if option=="m" or option=="M":
                    main_menu=1
                    submenu=""
                elif option=="p" or option=="P":
                    submenu="Play>Choose Version>"
            elif submenu=="Play>Choose Version>":
                print("(M)ain Menu")
                print("(0.0.1v) Vanilla")
                print("(O)ld Game")
                option="NONE"
                option=input(">")
                clear()
                if option=="m" or option=="M":
                    main_menu=1
                    submenu=""
                elif option=="0.0.1v":
                    print("Playing version 0.0.1(vanilla)")
                    runpy.run_path("version-0.0.1v.py")
                elif option=="o" or option=="O":
                    runpy.run_path("old_game.py")
                    print("That's all that the old game was. It was nice but this will be better.")
                    main_menu=1
                    submenu=""