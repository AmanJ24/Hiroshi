import pyautogui
import time


time.sleep(4)
i = 1
while i < 1000:
    pyautogui.typewrite(f"Hey...{i}")
    pyautogui.press("enter")
    i += 1

