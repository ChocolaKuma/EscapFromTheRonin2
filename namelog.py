##
##Namelog.py
##
##
##uses list to load name
##
playerName = "???"


def nameWrite():
    text_file = open("name.txt", "w+")
    print('Girl: What was your name?')
    ins = input()
    if ins == "":
        ins = "Hazel"
        print('I couldnt be bothered to put a name so call me Hazel')
    text_file.write(ins)
    text_file.close()
    
def nameRead():
    text_file = open("name.txt","r")
    global playerName
    playerName = text_file.read()
##        print ("This is the output in file:",text_file.read())
##        global playerName
##        playerName = text_file.read()
    text_file.close()
    
##nameWrite()
##nameRead()
##print("You name is now:",playerName)
##
##print('End File')
##    
