#created by Emerson-School-Coders
import runpy
import time
import random

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
        items=save_array_items
        print("items="+str(save_array_items))
#else:
#    pass
