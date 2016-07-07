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

#try:
if True:
    save = open("game_save.ags","r")
    save.close()
    save_array = []
    with open('game_save.ags', 'r') as f:
        save_array.append(f.readline().strip())
    print("Continue Save: " + save_array[0] + "?")
    continue_save = "INVALID"
    while continue_save != "Y" and continue_save != "y" and continue_save != "N" and continue_save != "n":
        continue_save=input("Y/n?")
#except:
#    pass
