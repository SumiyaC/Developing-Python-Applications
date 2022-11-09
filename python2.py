import time
from playsound import playsound

def countdown(t):
    x=input("Type Click when you want to click the start button / start the timer: ")
    if x=='Click':

        lst = y.split(sep=':')
        totalSeconds = (int(lst[0]) * 60) + int(lst[1])
        while totalSeconds:
            min = totalSeconds // 60
            sec = totalSeconds % 60
            timer = "{}:{}".format(min,sec)
            print('\r',timer, end="")
            time.sleep(1)
            totalSeconds -= 1

        playsound('projectAudio.mp3')

print("Enter Time in this way (MM:SS)-")
y=input()
countdown(y)