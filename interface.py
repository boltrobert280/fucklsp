
# CLI interface
# By suaminyafreya<3

def print_process(context, stat):

    status = ("[\033[31mError\033[0m]",      #  <- 0
              "[\033[32mSuccess\033[0m]",    #  <- 1
              "[\033[33mWriting\033[0m]",    #  <- 2
              "[\033[33mErasing\033[0m]",    #  <- 3
              "[\033[33mCopying\033[0m]",    #  <- 4
              "[\033[33mMaking\033[0m]",     #  <- 5
              "[\033[33mProcessing\033[0m]", #  <- 6
              "[\033[33mChecking\033[0m]",   #  <- 7
              "[\033[33mWarning\033[0m]",    #  <- 8
              "",                            #  <- 9 (Empty string) 
              "[\033[31m <3 \033[0m]")       #  <- 10 (Magic)

    print(f"{status[stat]} {context}")

def fancy_input(context):

    print(f"\n{context}")
    usin = input("\033[32m->\033[0m : ")
    print('')

    return usin

def clear_cli():

    import os
    import subprocess

    if(os.name == 'nt'):
        subprocess.run('cls', shell=True)
    else:
        subprocess.run('clear', shell=True)

def timer(context, stat, time):
    
    import time as timing
    import sys
    i = 0

    status = ("[\033[31mError\033[0m]", 
              "[\033[32mSuccess\033[0m]", 
              "[\033[33mChecking\033[0m]", 
              "[\033[31mWarning\033[0m]")

    while(True):

        sys.stdout.write(f"{status[stat]} {context} {time - i}\r")
        if(i == time):
            break
        i += 1
        timing.sleep(1)

def print_asciiart():

    print("\033[31m_______________ ____________  ____  __.____       ___________________")
    print("\\_   _____/    |   \\_   ___ \\|    |/ _|    |     /   _____/\\______   \\  ")
    print(" |    __) |    |   /    \\  \\/|      < |    |     \\_____  \\  |     ___/   ")
    print(" |     \\  |    |  /\\     \\___|    |  \\|    |___  /        \\ |    |      ")
    print(" \\___  /  |______/  \\______  /____|__ \\_______ \\/_______  / |____|       ")
    print("     \\/                    \\/        \\/       \\/        \\/       \033[0m")
    
    print("\nCredit to 'suaminyafreyajkt48 \033[31m<3\033[0m' as creator\n")
    print("Dukung creator dengan mendoakan creator supaya berjodoh dengan freyajkt48\n\n")

def magic():

    for x in range(0, 100):
        print_process(context="Doain guys", stat=10)
    
    print_process(context="Please pengen banget jadi suaminya freyajkt48", stat=10)
    print_process(context="Tolong doanya dong :)", stat=10)
    print_process(context="Semakin banyak yang berdoa maka semakin manjur", stat=10)

def timer_no_out(time):
    
    import time as timing
    import sys
    i = 0

    status = ("[\033[31mError\033[0m]", 
              "[\033[32mSuccess\033[0m]", 
              "[\033[33mChecking\033[0m]", 
              "[\033[31mWarning\033[0m]")

    while(True):

        if(i == time):
            break
        i += 1
        timing.sleep(1)