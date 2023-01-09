import pyautogui
import time


time.sleep(4)
i = 1
while i < 1000:
    pyautogui.typewrite(f"Oh you will regret it now....{i}")
    pyautogui.press("enter")
    i += 1

