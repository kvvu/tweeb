import os, sys, tty, termios
import threading, signal, time
import tweepy, pyfiglet, keyboard
from termcolor import colored
from colorama import init
from colorama import Fore, Back, Style
from keys import *
## from pyfiglet import Figlet

print('\033c')

def signal_handler(signal, frame):
    print(Fore.RED + 'You pressed Ctrl+C! Closing Script')
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)


# FIGLETS & texts
clear = "\033c"
close = pyfiglet.figlet_format("THX", font = "isometric1" )
title = pyfiglet.figlet_format("Tweeb", font = "isometric1" )
ctitle = colored(title, 'blue')
stitle = Fore.CYAN + " TWEEB - Twitter for anything\n   Ctrl+C+Enter = Exit "

print (clear)

# tweeb

print (ctitle)
print (stitle + '\n')
auth = tweepy.OAuthHandler(apikey, apikey_secret)
auth.set_access_token(token, token_secret)
api = tweepy.API(auth)
print (Fore.BLUE + "Write a tweet!")
tweet = input(Style.RESET_ALL + "⟩⟩ ")
## api.update_with_media(media, tweet)

# Y/N FUNCTION
def getch():
    """Read single character from standard input without echo."""
    
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def yes_or_no(question):
    c = ""
    print(question + " (Y/N): ", end = "", flush = True)
    while c not in ("y", "n"):
        c = getch().lower()
    return c == 'y'

if __name__ == "__main__":
    if not yes_or_no(Fore.YELLOW + "Are you sure?"):
        print(Fore.RED + "No") # ...or echo nothing and just provide newline
        print(clear)
        print(ctitle)
        print (" ")
        print(Style.RESET_ALL + "Your tweet input was :")
        print(Fore.BLUE + "[  " + tweet + "  ]" )
        print(" ")
        time.sleep(1)
        os._exit(0)
    
    else:
        print(Fore.GREEN + "Yes")
        print(Fore.BLUE + "Tweeting...")
        api.update_status(status =(tweet))
        print (clear)
print (Fore.GREEN + title)
print (stitle + '\n')
print (Style.RESET_ALL + " ")
print (Fore.GREEN + "Done! , you tweeted : ")
print (Fore.BLUE + "[  "  + tweet +"  ]" )
print ("\n" + "\n")
time.sleep (2)
print (clear)
print (Fore.RED + title)
print ("\n" + "\n")
print (Fore.RED + "This script will close in a couple of seconds")
time.sleep (3)
print (Style.RESET_ALL + "\n")
print (clear)
print (Fore.CYAN + close)
print (stitle)
print (Style.RESET_ALL + "\n")
print (Fore.GREEN + "Script CLosed, Your Tweet was : ")
print (Fore.BLUE + "[  "  + tweet +"  ]" )


forever = threading.Event()
forever.wait()
os._exit(0)
