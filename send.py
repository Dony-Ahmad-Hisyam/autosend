import pyautogui
import time

pyautogui.moveTo(1714,1027)
pyautogui.click()

for i in range(100):
    pyautogui.write("Ini Spam")
    time.sleep(0.1)
    pyautogui.press("Enter")