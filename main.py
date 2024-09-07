import pyautogui
import time
import random


#søker etter bilde og klikker
def finnBilde(navn):
    try:
        x,y = pyautogui.locateCenterOnScreen(navn,confidence=0.8)
        pyautogui.click(x,y)
    except:
        finnBilde(navn)


#prøver å klikke over troppene for å plassere
def plyndring(navn):
    finnBilde(navn)
    x,y = pyautogui.position()
    pyautogui.click(x,y-55,clicks=6,interval=float(0.2))


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

#ett helt angrep
def EnRunde(): 
    #starter runde  
    finnBilde("attack.png")
    finnBilde("Find now.png")


    #combat
    plyndring("drage1.png")

    #avslutter combat
    EndComabat()

EnRunde()
EnRunde()