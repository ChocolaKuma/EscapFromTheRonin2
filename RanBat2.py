###################################
##                                #
##ranbat2.py                      #
##Makes random battles for user   #
##                                #
###################################


#########
#Imports#
#########
import time
import random
import form
import inv



items = inv.items

playerName = "???"
#playerName = "???"
#######
#Lists#
#######
moblist = ["Slime", "Goblin", "Hound", "NyaaTrape", "Navi"]
HELP = [("#", "Name", "Description"),
        ("1", "Attack", "Attacks your enemy with equipped weapon")
        ,("2", "Defend", "Use your equipped weapon to defend"),
        ("3", "Heal", "If player has Med_Kit uses it on player"),
        ("3", "Stats", "Prints players stats"),
        ("5", "Finisher", "A secret technique (Has a 50% chance of a insta-kill)"),
        ("6", "HELP", "This comand displays Help")]
mobGenlist = ["He", "She", "It"]
kit = (["Bandages","Potion","MedKit","Vial_of_Yuna's_Love","Rikku_Vysuic_Pnaf"])

##########
#Mob stat#
##########

mobhp = random.randint(10,40)
mobgender = random.choice(mobGenlist)
mobrace = random.choice(moblist)
#print(mobhp,mobgender,mobrace)


#############
#Player Stat#
#############

playerhp = random.randint(20,80)
playerdef = random.randint(25,50)




##################################################
#Function list
##################################################
def deven():
    print("Welcome to RanBat Version 2.0")
    ##print("Whats your name?")
    ##playerName = input()
    global playerName
    #playerName = "Dev"
    print("script will now start enjoy!")
    time.sleep(2)
    ##format.clearscreen()
    ##format.clearscreen()
    print("==========================================================================")
    print("|","Name:",playerName,"|",
          "Mob race:",mobrace,"|",
          "Mob Gender:",mobgender,"|",
          "Mob HP:",mobhp,"|")
    print("==========================================================================")

def name():
    text_file = open("name.txt","r")
    global playerName
    playerName = text_file.read()
    text_file.close()


def main():
    name()
    vofaStart()
##    deven()
    
    
    whileloop()

def shinee():
    global playerName
    global playerhp
    print("*player collapses")
    print("")
    print(".")
    time.sleep(1)
    print("")
    print("..")
    time.sleep(1)
    print("")
    print("...")
    print("")
    time.sleep(2)
    plhp = playerhp
    print("Vofa:",playerName,"Are you okay?")
    print("")
    item = random.choice(kit)
    ##possable items:Bandages,Potion,MedKit,Vial_Yuna's_Love,Rikku's_Vysuic_Pnaf
    def vofaChat1():
        print(playerName,"I found a",item)
        print("")
        time.sleep(2)
        print("Vofa:Ill use it")
        print("")
        time.sleep(2)
        print("Vofa:There you go")
        print("")
        time.sleep(2)
    def vofaChat2():
        print("Vofa:",playerName,"I found a bottle that says",item)
        print("")
        time.sleep(2)
        print("Vofa:Ill use it")
        print("")
        time.sleep(2)
        print("*Vofa uses it")
        print("")
        time.sleep(2)
        print("Vofa:There you go")
        print("")
        time.sleep(2)        
    def vofaChat3():
        print("Vofa:Looks like it is working")
        print("")
        time.sleep(2)
        print("Vofa:Now you have", plhp, "HP", playerName)
        time.sleep(2)
        
    if item == "Bandages":
        print("")
        time.sleep(2)
        print(playerName,"I found some",item)
        print("")
        time.sleep(2)
        print("Ill use them")
        time.sleep(2)
        print("")
        print("There you go")
        time.sleep(2)
        print("")
        plhp = plhp + random.randint(5,15)
        vofaChat3()

    if item == "Potion":
##        print(playerName,"I found some",item)
        vofaChat2()
        plhp = plhp + random.randint(15,25)
        vofaChat3()
        
    if item == "MedKit":
##        print(playerName,"I found a",item)
        print("")
        vofaChat1()
        plhp = plhp + random.randint(25,50)
        vofaChat3()
        
    if item == "Vial_of_Yuna's_Love":
##        print(playerName,"I found some",item)
        vofaChat2()
        plhp = plhp + random.randint(50,80)
        vofaChat3()
        
    if item == "Rikku_Vysuic_Pnaf":
##        print(playerName,"I found some",item)
        print("")
        vofaChat2()
        plhp = plhp + random.randint(80,400)
        vofaChat3()
    batMenDis()

    

def vofaStart():
    time.sleep(1)
    print("Vofa: Oh no whats that!,", playerName, "protect me")
    print("")
    time.sleep(3)
    #print("here 2 ")
    print("You have incountered a wild", mobrace)
    print("")
    time.sleep(3)
    print("Vofa: Looks like", mobgender, "has",mobhp , "HP. Best be careful.")
    print("")
    batMenDis()
    

def whileloop():
    playerchoice = int(input())
    while playerchoice !=None:
        playerchoice = int(input())
        global mobhp
        if mobhp <= 0:
            print("Mob Has been defeted")
            print("Congratulations!~")
            time.sleep(3)
            break
        

        if playerchoice == 0:
            option0()
            break

        if playerchoice == 1:
            option1()
            batMenDis()

        if playerchoice == 2:
            option2()
            batMenDis()

        if playerchoice == 3:
            option3()
            batMenDis()            
            
        if playerchoice == 4:
            print("You have chosen option #4")
            option4()
            batMenDis()
            
        if playerchoice == 5:
            print("You have chosen option #5")
            option5()
            batMenDis()          
            
        if playerchoice == 6:
            print("You have chosen option #6")
            option6()
            batMenDis()
            
            
        if playerchoice == 7:
            print("You have chosen option #7")
            option7()
            batMenDis()

        if playerchoice == 8:
            print("僕コミット切腹")
            opt8()
            
            
        if playerchoice >8:
            print("Vofa: Quit messing around",playerName,"!")
            batMenDis()
            
            


def batMenDis():
    print("")
    print("What are you going to do")
    print("")
    print("1 = Attack")
    print("2 = Defend")
    print("3 = Heal")
    print("4 = Print current Stats")
    print("5 = Finisher (50% chance of working)")
    print("6 = HELP")

def option0():
    #print("here 2")
    print("You have chosen option number 0")
    print("Program Now Exiting")
    time.sleep(2)
    print("Good Bye. Have a nice day! hope to fight with you again")

def option1():
    print("You have chosen option number 1")
    time.sleep(1)
    print("You attept an attack")
    time.sleep(2)
    cointoss = random.randint(1,2)
    global mobhp
    global playerhp
    if cointoss == 1:
        print("Attack successfull!")
        playerDam = random.randint(10,60)
        newmobhp = mobhp - playerDam
        print("You did",playerDam,"Damage")
        mobhp = newmobhp
        if mobhp <=0:
            mobhp = 0
        print("Updated mob HP")
        print(mobhp)
    if cointoss == 2:
        print("You missed")
        mobDam = random.randint(10,30)
        nphp = playerhp - mobDam
        print("Vofa: Oh no you took damage")
        if nphp <= 0:
            shinee()
        playerhp = nphp
    

def option2():
    #defend
    print("You have chosen option #2 Defend")
    print("You brace for impact")
    global playerhp
    php = playerhp
    coin = random.randint(1,3)
    global playerdef
    pld = playerdef
    md = random.randint(20,40)
    if coin == 1:
        print("You where sucessful")
        nphp = (php + pld) - md
        print("No damage was taken")
    if coin == 2:
        print("You where unsucessful")
        nphp = php - md
        print(nphp)
    if coin == 3:
        print("You where partialy sucessful")
        nphp = (php + 44)- md
        print(nphp)
    php = nphp
    playerhp = php 
    if playerhp <= 0:
        shinee()

def option3():
    #Heal
    global items
    global playerhp
    print("You have chossen option #3 heal")
    ##inv.items.append(entry)
    print("What would you like to use")
    print("(Make sure to spell corectly)")
    print("Items:",items)
    item = input()
    plhp = playerhp
    if item == "Cookie":
        rnr = random.randint(1,5)
        print("you gained", rnr ,"HP")
        plhp = plhp + rnr
    if item == "Bandages":
        rnr = random.randint(5,15)
        print("you gained", rnr ,"HP")
        plhp = plhp + rnr
    if item == "Potion":
        rnr = random.randint(15,25)
        print("you gained", rnr ,"HP")
        plhp = plhp + rnr        
    if item == "MedKit":
        rnr = random.randint(25,50)
        print("you gained", rnr ,"HP")
        plhp = plhp + rnr        
    if item == "Vial_of_Yuna's_Love":
        print("you gained", rnr ,"HP")
        rnr = random.randint(50,80)
        plhp = plhp + rnr        
    if item == "Rikku_Vysuic_Pnaf":
        print("you gained", rnr ,"HP")
        rnr = random.randint(80,400)
        plhp = plhp + rnr
    else:
        ("Vofa:You cant use what you dont have!")
        plhp = plhp + 0
    playerhp = plhp
    entry = item
    items.remove(entry)
    print(items)
    print("Current HP:", playerhp)

def option4():
    #stats
    global playerName
    global playerhp
    global playerdef
    global mobrace
    global mobhp
    global mobgender
    print("Vofa:Give me a sec, Let me look at you")
    print("")
    print("=========================================")
    print("=            Player Stats               =")
    print("=========================================")
    print("Player Name:",playerName)
    print("Player Health:",playerhp)
    print("Player Defence:",playerdef)
    print("=========================================")    
    print("")
    print("")
    print("")
    print("=========================================")
    print("=            Mob Stats                  =")
    print("=========================================")
    print("Mob Race:",mobrace)
    print("Mob Health:",mobhp)
    print("Mob Gender:",mobgender)
    print("=========================================")


#\ return

def option5():
    #Finisher
    global mobhp
    coin = 1#random.randint(1,2)
    if coin == 1:
        print("It worked")
        mobhp = 0
    if coin ==2:
        print("It failed")

def option6():
    #HELP
    global HELP
    print(HELP)
def option7():
    #HELP
    print("Currently Unused Function")

        
def opt8():
    #kill player
    print("Boku-wa comito harakiri")
    time.sleep(2)
    print("")
    print("")
    playerhp = 0
    format.clearscreen()
    format.clearscreen()
    print("player HP", playerhp)
    print("")
    print("国の為 重き努を 果し得で 矢弾尽き果て 散るぞ悲しき")
    print("仇討たで 野辺には朽ちじ 吾は又 七度生れて 矛を執らむぞ")
    print("醜草の 島に蔓る 其の時の 皇国の行手 一途に思ふ")
    time.sleep(5)
    print(".")
    time.sleep(1)
    print("")
    print("..")
    time.sleep(1)
    print("")
    print("...")
    format.clearscreen()
    format.clearscreen()
    time.sleep(1)
    shinee()


        
##############################################    
#start                                       #
##############################################

##main()


##############################################
#Notes                                       #
##############################################

##
##main commented out so it wont run automatically
##
##
##
##
##
##
##

























