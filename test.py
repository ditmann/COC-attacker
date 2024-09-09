import pyautogui


x,y = pyautogui.locateCenterOnScreen("attack.png", confidence=0.4)
pyautogui.click(x,y)
 
