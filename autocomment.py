import pyautogui
import time

comments = ["Hi","Just commenting for fun","Checking my python comment bot","Just for fun","I am just checking my python skill","python is awesome","I am a messy programmer"]

time.sleep(5)

for i in range(10):
    pyautogui.typewrite(comments[i%7])
    pyautogui.typewrite("\n")
    time.sleep(2)