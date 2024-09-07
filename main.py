import pyautogui
import time


#søker etter bilde og klikker
def finnBilde(navn):
    x,y = pyautogui.locateCenterOnScreen(navn, confidence=0.8)
    pyautogui.click(x,y)




#starter runde     
finnBilde("attack.png")
time.sleep(2)
finnBilde("Find now.png")
time.sleep(3)
pyautogui.press("1")




