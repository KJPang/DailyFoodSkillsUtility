"""
#KJPang 2020
"""

import numpy

#import canteen skills in a sensical format
cats = open("cat_skill.cat_skill", "r")
catsArray = numpy.fromfile(cats, dtype=numpy.uint8)

#lists of phrases
skillnum = [*range(1,30,1)]
activeSkills = 0
isActive = ["Enabled ", "Disabled"]
errorList = ["\nAt least one food skill must be enabled", "\nInput not recognized"]
foodSkills = ["Felyne Carver(Lo)", "Felyne Defender(Hi)", "Felyne Defender(Lo)", "Felyne Deflector",
              "Felyne Escape Artist", "Felyne Sprinter", "Felynebacker", "Felyne Weakener",
              "Felyne Riser(Lo)", "Felyne Temper", "Felyne Cliffhanger", "Felyne Gripper",
              "Felyne Lander", "Felyne Bulldozer", "Felyne Foodie", "Felyne Dungmaster", 
              "Felyne Fur Coating", "Felyne Trainer", "Felyne Booster", "Felyne Fisher",
              "Cool Cat", "Felyne Insurance", "Felyne Provoker", "Felyne Parting Gift",
              "Felyne Researcher", "Felyne Weathercat", "Felyne Biologist", "Felyne Macrozoologist",
              "Felyne Microzoologist"]
foodStarts = [82, 162, 178, 242, 258, 274, 290, 306, 354, 370, 386, 402, 434, 450, 466, 
              546, 578, 626, 642, 674, 690, 706, 722, 738, 754, 770, 882, 898, 914]
foodEnds = [86, 166, 182, 246, 262, 278, 294, 310, 358, 374, 390, 406, 438, 454, 470, 
            550, 582, 630, 646, 678, 694, 710, 726, 742, 758, 774, 886, 902, 918]
foodSpaces = [7, 5, 5, 8, 4, 9, 12, 9, 8, 11,
              6, 10, 11, 8, 11, 7, 6, 10, 10, 11,
              16, 8, 9, 5, 7, 7, 8, 3, 3]  
#didn't want to write something up to generate this, so prewritten array
foodLazy = ["\n[01] ", "[02] ", "[03] ", "[04] ", "[05] ", "[06] ", "[07] ", "[08] ", "[09] ", "[10] ",
             "[11] ", "[12] ", "[13] ", "[14] ", "[15] ", "[16] ", "[17] ", "[18] ", "[19] ", "[20] ",
              "[21] ", "[22] ", "[23] ", "[24] ", "[25] ", "[26] ", "[27] ", "[28] ", "[29] "]
foodActive = []

#check to see which foods are active and display them nicely
def checkFood():
    global totalfood
    totalfood = 0
    foodActive = []
    drawPos = 1
    
    for i in range(len(foodStarts)):
        if catsArray[foodStarts[i]] == 255:
            foodActive.append(isActive[0]) ; totalfood += 1
        else: foodActive.append(isActive[1])
        if drawPos%2 == 1:
            print (foodLazy[i] + foodSkills[i] + " "*int(foodSpaces[i]) + foodActive[i] + "    " , end = "")
        else: print (foodLazy[i] + foodSkills[i] + " "*int(foodSpaces[i]) + foodActive[i])
        drawPos +=1 
    print ("     Total Active: " + str(totalfood) + " / 29\n")
    #print (foodActive) 

#help command
def commands():
    print ("\nList of Commands:\n\nfood - Display the status of all daily food skills\nhelp - See this list of commands")
    print ("delp - Read detailed instructions on how to use the utility\nsave - Create a shiny new 'cat_skillMOD.cat_skill' file")
    print ("exit - Close the utility\n")
    print ("bout - See basic utility and author information\n")
    print ("1-29 - Toggle the daily food skill associated with the input\n")
    print ("dall - Disable all daily skills besides Felyne Booster")
    print ("eall - Enable all daily skills\n")
    
#detailed help command    
def detailedHelp():
    print ("\nType a number to toggle the associated food skill.\ne.g. '1' will enable or disable Felyne Carver(Lo) from the daily rotation.")
    print ("Once the desired skill setup is reached, type 'save' to create a cat_skillMOD.cat_skill file in the working folder\nAny exising file with the same name will be overwritten.")
    print ("Move this file to nativePC/common/equip and rename to cat_skill.cat_skill, as with the original unmodified file.")
    print ("As with most similar mods, Stracker's Loader is required for these changes to be reflected in-game.\n")

#author info command    
def authHelp():
    print ("\nDaily Food Skills Utility v1.1.0 - KJPang 2020")
    print ("Written in python3.7 (python.org) and packaged via pyinstaller (pyinstaller.org)\n")
    print ("pyinstaller packages scripts with an entire python environment, hence the hefty file\n")

#save command
def saveFood():
    conv = catsArray.tobytes()
    newFile = open("cat_skillMOD.cat_skill", "wb")
    newFile.write(conv)
    newFile.close()
    print ("\ncat_skillMOD.cat_skill saved.  \nEnter 'delp' if you don't know what to do with this file.\n")
    
#disable everything but booster
def allDsab():
    catsArray[82:86] = 0 ; catsArray[162:166] = 0 ; catsArray[178:182] = 0 ; catsArray[242:246] = 0 ; 
    catsArray[258:262] = 0 ; catsArray[274:278] = 0 ; catsArray[290:294] = 0 ; catsArray[306:310] = 0 ; 
    catsArray[354:358] = 0 ; catsArray[370:374] = 0 ; catsArray[386:390] = 0 ; catsArray[402:406] = 0 ; 
    catsArray[434:438] = 0 ; catsArray[450:454] = 0 ; catsArray[466:470] = 0 ; catsArray[546:550] = 0 ; 
    catsArray[578:582] = 0 ; catsArray[626:630] = 0 ; catsArray[674:678] = 0 ; catsArray[690:694] = 0 ; 
    catsArray[706:710] = 0 ; catsArray[722:726] = 0 ; catsArray[738:742] = 0 ; catsArray[754:758] = 0 ; 
    catsArray[770:774] = 0 ; catsArray[882:886] = 0 ; catsArray[898:902] = 0 ; catsArray[914:918] = 0 ;
    catsArray[642:646] = 255
    print ("\nDisabled all daily skills besides Felyne Booster\n")
    global totalfood
    totalfood = 1
    
#enable everything
def allEnab():
    catsArray[82:86] = 255 ; catsArray[162:166] = 255 ; catsArray[178:182] = 255 ; catsArray[242:246] = 255 ; 
    catsArray[258:262] = 255 ; catsArray[274:278] = 255 ; catsArray[290:294] = 255 ; catsArray[306:310] = 255 ; 
    catsArray[354:358] = 255 ; catsArray[370:374] = 255 ; catsArray[386:390] = 255 ; catsArray[402:406] = 255 ; 
    catsArray[434:438] = 255 ; catsArray[450:454] = 255 ; catsArray[466:470] = 255 ; catsArray[546:550] = 255 ; 
    catsArray[578:582] = 255 ; catsArray[626:630] = 255 ; catsArray[674:678] = 255 ; catsArray[690:694] = 255 ; 
    catsArray[706:710] = 255 ; catsArray[722:726] = 255 ; catsArray[738:742] = 255 ; catsArray[754:758] = 255 ; 
    catsArray[770:774] = 255 ; catsArray[882:886] = 255 ; catsArray[898:902] = 255 ; catsArray[914:918] = 255 ;
    catsArray[642:646] = 255
    print ("\nEnabled all daily skills\n")
    global totalfood
    totalfood = 29
    
print ("\nWelcome to the Daily Food Skills Utility\n")
commands()
input("Press ENTER to begin\n\n>")
checkFood()

#take inputs and run linked function
waiting = input(">")
while waiting != "exit":
    if waiting == "help":
        commands()
    elif waiting == "delp":
        detailedHelp()
    elif waiting == "food":
        checkFood()
    elif waiting == "save":
        saveFood()
    elif waiting == "bout":
        authHelp()
    elif waiting == "dall":
        allDsab()
    elif waiting == "eall":
        allEnab()
    elif waiting == "":
        activeSkills = 1
    #check number input and toggle skill
    elif (waiting) in str(skillnum):
        holdSkill = (skillnum.index(int(waiting)))
        if catsArray[foodStarts[holdSkill]] == 255:
            if totalfood != 1:
                catsArray[foodStarts[holdSkill]:foodEnds[holdSkill]] = 0
                totalfood -= 1 ; activeSkills = 1
                print ("\n" + foodSkills[holdSkill] + " is now " + isActive[1] + "\n")
        else: 
            catsArray[foodStarts[holdSkill]:foodEnds[holdSkill]] = 255
            totalfood += 1 ; activeSkills = 1
            print ("\n" + foodSkills[holdSkill] + " is now " + isActive[0] + "\n")
        if activeSkills == 0:
            print (errorList[0] + "\n")
    else: print (errorList[1] + "\n")
    activeSkills = 0
    waiting = input(">")

raise SystemExit()



    
    