import random
import time
curmov = 0
curmovpt = "."


def mapupdate():
    global curmov
    global curmovpt
    if curmov == 0:
        curmovpt = "|x*******0|3"
    if curmov == 1:
        curmovpt = "|x*******1|3"
    if curmov == 2:
        curmovpt = "|*x******2|3"
    if curmov == 3:
        curmovpt = "|**x*****3|3"
    if curmov == 4:
        curmovpt = "|***x****4|3"
    if curmov == 5:
        curmovpt = "|****x***5|3"
    if curmov == 6:
        curmovpt = "|*****x**6|3"
    if curmov == 7:
        curmovpt = "|******x*7|3"
    if curmov == 8:
        curmovpt = "|*******x8|3"
    if curmov >= 9:
        curmovpt = "|********9|3"
    ###############################
    if curmov == 10:
        curmovpt = "|x********|3"
    if curmov == 11:
        curmovpt = "|x********|3"
    if curmov == 12:
        curmovpt = "|*x*******|3"
    if curmov == 13:
        curmovpt = "|**x******|3"
    if curmov == 14:
        curmovpt = "|***x*****|3"
    if curmov == 15:
        curmovpt = "|****x****|3"
    if curmov == 16:
        curmovpt = "|*****x***|3"
    if curmov == 17:
        curmovpt = "|******x**|3"
    if curmov == 18:
        curmovpt = "|*******x*|3"
    if curmov >= 19:
        curmovpt = "|*********|3"
    if curmov == 20:
        curmovpt = "|***< >****|3"
    if curmov == 21:
        curmovpt = "|x**< >****|3"
    if curmov == 22:
        curmovpt = "|*x*< >****|3"
        
    if curmov == 23:
        curmovpt = "|**x< >****|3"
    if curmov == 24:
        curmovpt = "|***x >****|3"

    ################################

    if curmov == 25:
        curmovpt = "|***<x>****|3"
    if curmov == 26:
        curmovpt = "|***< x****|3"
    if curmov == 27:
        curmovpt = "|***< >x***|3"
    if curmov == 28:
        curmovpt = "|***< >*x**|3"
    if curmov == 29:
        curmovpt = "|***< >**x*|3"
    if curmov == 30:
        curmovpt = "|***< >***x|3"
    if curmov > 30:
        curmovpt = "|***< >***x|3"
def mapNow():
    print('Current map')
    global curmov
    if 1 <= curmov <= 9:
        map1()

    if 10 <= curmov <= 19:
        map2()

    if 20 <= curmov <= 32:
        map3()

    if 33 <= curmov < 99999:
        print('You win')
        
    
##    if curmov <=9:
##        mapNow = map1()
##    elif curmov (10,24):
##        mapNow = map2()
##    elif curmov (25,30):
##        mapNow = map3()



def map1():#print map 1
    global curmovpt
    print("map 1")
    print("===========1")
    print("|DDDDDDDDD|2")
    print(curmovpt)
    print("|DDDDDDDDD|4")
    print("===========5")
    print(" 1234567891 ")
    print("          0 ")
    
def map2():
    global curmovpt
    print("map 2")
    print("===========1")
    print("|[][][][]D|2")
    print(curmovpt)
    print("|[][][][]D|4")
    print("===========5")
    print(" 1234567891 ")
    print("          0 ")
    
def map3():
    global curmovpt
    print("map 3")
    print("===========1")
    print("|<><><><><>|2")
    print(curmovpt)
    print("|<><><><><>|4")
    print("===========5")
    print(" 1234567891 ")
    print("          0 ")

def diceroll():#Dice roll
    global curmov
    print("curmov:",curmov)
    diceRoll = random.randint(1,6)
    print("diceroll:",diceRoll)
    newmov = curmov + diceRoll
    curmov = newmov
    print("curmov:",curmov)

def readmov():#Reads last mov
    global curmov
    text_file = open("curmov.txt", "r")
    NewMov = int(text_file.read())
    print(NewMov)
    curmov = NewMov
    print(curmov)
    
def writemov():#writes last mov
    global curmov
    text_file = open("curmov.txt", "w+")
    stcurmov = str(curmov)
    text_file.write(stcurmov)
    text_file.close()  

def main():
    readmov()      #Reads last/first move from curmov.txt.Updates curmov
    mapupdate()    #Updates map w/ current position
    diceroll()     #Rolls movement dice
    mapupdate()    #Updates map w/ current position
    writemov()     #writes resalt of diceroll() to cur mov


    mapNow()
##    map1()         #Prints current ASCII map
    

##main()
