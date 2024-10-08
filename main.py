import pyautogui
import time
import random

#det tar 8 runder å tømme eleksir
tidEleksir = int(2)



#søker etter bilde og klikker
def klikkBilde(navn):
    try:
        x,y = pyautogui.locateCenterOnScreen(navn,confidence=0.8)
        pyautogui.click(x,y)
    except:
        klikkBilde(navn)


#prøver å klikke over troppene for å plassere
def plyndring(navn):
    klikkBilde(navn)
    x,y = pyautogui.position()
    pyautogui.click(x,y-25,clicks=7, interval=random.randint(1,5))
    



#ser etter EndBattle så tar deg tilbake til landsby
def EndComabat():
    try:
        pyautogui.locateOnScreen("HPSurrender.png",confidence=0.8)
        time.sleep(7)
        EndComabat()
    except:
        klikkBilde("HPEndBattle.png")
        klikkBilde("HPOkey.png")
        klikkBilde("HPHome.png")

#ett helt angrep
def enRunde(): 
    #starter runde  
    klikkBilde("HPattack.png")
    klikkBilde("HPFind now.png")


    #combat
    plyndring("HPtroop.png")

    #avslutter combat
    EndComabat()


#samle eleksir
def samling():
    try:    
        x,y = pyautogui.locateCenterOnScreen("HPcaMidten.png", confidence=0.7)
        pyautogui.moveTo(x,y)
        pyautogui.dragTo(x,y+600,2)
        klikkBilde("HPeleksirCart.png")
        klikkBilde("HPCollect.png")
        klikkBilde("HPX.png")
    except:
        samling()


while 1 == 1:

    while tidEleksir > 0:
        enRunde()
        tidEleksir = tidEleksir - 1

    samling()
    tidEleksir = 7
