
from time import *


def countdown(t):
    while t:
        
        mins, sec = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, sec)
        t -= 1
        sleep(1)
        print(timer, end="\r")


    print("time up")

try:
    t = int(input("inter number : "))
    countdown(t)
except ValueError:
    print ("please type number")


