#Johnathan Hinebrook 9-24-14 -- 10-14-14
#mainprog.py
#This program calls all created mdels and plays the in order
################################################
##Imports
################################################
import time      #for timeing
import stry      #holds story and most text
import mov2      #holds map and movement 
import inv       #hold players invatory
import form      #holds formatting options
import RanBat2   #hold Random battle genorator
import namelog   #Makes a name file for mods to read
import restart   #save mode feature


################################################
##Globals
################################################
playerName = "???"


################################################
##Functions
################################################

def askname():
    global playerName
    text_file = open("name.txt", "w+")
    ins = input()
    if ins == "":
        ins = "Hazel"
        print('I couldnt be bothered to put a name so call me Hazel')
    text_file.write(ins)
    text_file.close()
    text_file = open("name.txt","r")
    playerName = text_file.read()
    print('')
    print('The girls closes her eyes like she is trying to keep it in memory')
    print('')
    time.sleep(2)
    print('Girl: Nice to meet you',playerName)
    print('Girl: My name is Vofasakai but every one calls me Vofa')
    print(playerName,': Nice to meet you Vofa')
    print(playerName,': Lets get going before the astroid storm')



def renren():
    text_file = open("renren.txt","r+")
    renren = text_file.read()
    text_file.close()
    print(renren)
    if renren == "1":
       ##load play name from last save
        text_file = open("curmov.txt","r")
        curmov = int(text_file.read())
        while curmov <= 9999:
            if curmov <=33:
                mov2.main()
                time.sleep(2)
                RanBat2.main()
            if curmov >= 34:
                form.clear()
                print('You have Won!!!~')
                break
        
    if renren == "0":
        ##adds playername and starts from begining
        stry.intro()
        stry.gnam()
        askname()
        stry.pt1()
        RanBat2.main()
        stry.pt2()
        time.sleep(7)
        print('Vofa :Okay lets go.')
        text_file = open("curmov.txt","r")
        curmov = int(text_file.read())
        while curmov <= 9999:
            if curmov <=33:
                mov2.main()
                time.sleep(2)
                RanBat2.main()
            if curmov >= 34:
                form.clear()
                print("Congrats you escaped")
                print('You have Won!!!~')
                break        

def layout():
    """Basic layout of game"""
    print('Rember to break after your selection')
    restart.main()
    renren()
    stry.pt3()
##    
    

        
        
        




 

##################################################
##Main Function
##################################################
def main():
    layout()

##################################################
##start  
##################################################
main()

##################################################


