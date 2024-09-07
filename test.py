import pyautogui


while True:
    try:

        gaming = pyautogui.locateOnScreen("attack.png", confidence=0.7)
        print("online")

    

    except:
        print("offline")


#if gaming != pyautogui.ImageNotFoundException:
#        print("Nei")
#else:
#        print("ja")


