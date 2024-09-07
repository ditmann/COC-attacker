import pyautogui
import time
import random


#søker etter bilde og klikker
def finnBilde(navn):
    x,y = pyautogui.locateCenterOnScreen(navn, confidence=0.8)
    pyautogui.click(x,y)


#prøver å klikke over troppene for å plassere
def plyndring(navn):
    finnBilde(navn)
    x,y = pyautogui.position()
    pyautogui.click(x,y-50,clicks=6,interval=random.randrange(0,5,1))


#ser etter EndBattle så tar deg tilbake til landsby
def EndComabat():
    try:
        pyautogui.locateOnScreen("Surrender.png",confidence=0.8)
        time.sleep(7)
        EndComabat()
    except:
        finnBilde("EndBattle.png")
        time.sleep(1)
        finnBilde("Okey.png")
        time.sleep(1)
        finnBilde("Home.png")



#starter runde     
finnBilde("attack.png")
time.sleep(2)
finnBilde("Find now.png")
time.sleep(5)


#combat
plyndring("drage1.png")

#avslutter combat
EndComabat()








