import pyautogui
import keyboard
import time



pyautogui.alert('')

keyboard.press_and_release('Alt + Tab')

time.sleep(3)

for i in range(5):
    pyautogui.moveTo(215,400)
    for i in range(300):
        pyautogui.click()
    pyautogui.moveTo(1153,617)
    for i in range(25):
        pyautogui.click()



