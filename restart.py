#restart
print('')


def introduc():
    print('Is this a restart?')
    print('or a load')


def menu():
    print('(0)to quit(1)Restart (2)Load')

def loopy():
    pl = input()
    while pl !=None:
        pl = input()
        if pl == "":
            print("Quit trying to break things")

        if pl == "0":
            print('Breaking')
            break
        
        if pl == "1":
            """Restarts program writes defalts
                    into save slot previous save deleted"""
            print('you have chosen to restart')
            import time
            print('')
            print('Rewriting pervious save')
            print('Restarting now')
            text_file = open("name.txt", "w+")
            text_file.write(".")
            text_file.close()            
            text_file = open("curmov.txt", "w+")
            text_file.write("0")
            text_file.close()
            time.sleep(3)
            print('Restart complete')
            print('Enjoy!')
            text_file = open("renren.txt", "w+")
            text_file.write("1")
            text_file.close()             
        if pl == "2":
            print('you have chosen to load previous save')
            import time
            print('loading data')
            time.sleep(3)
            print('load complete')
            text_file = open("renren.txt", "w+")
            text_file.write("0")
            text_file.close()  
            print('Enjoy!')
            

##        if pl == 42:
##            print('The meaning og life')
##            menu()
##        if pl == 666:
##            print('"Is the number of the beast~~~!"')
##            menu()
##        def breaki():
##                print('Quit trying to break things')
##                menu()
##        if pl
        

def main():
  introduc()
  menu()
  loopy()
##introduc()
##menu()            
##loopy()
##main()
