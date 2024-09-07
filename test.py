import pyautogui


x,y = pyautogui.locateCenterOnScreen("caMidten.png", confidence=0.7)
pyautogui.moveTo(x,y)
pyautogui.dragTo(x,y+600,2)

