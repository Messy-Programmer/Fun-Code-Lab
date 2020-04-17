import pyautogui
import time

groups = ['251123409000385','843804142348443','900389246658181']

time.sleep(5)

pyautogui.keyDown('ctrl')
pyautogui.keyDown('t')
pyautogui.keyUp('t')
pyautogui.keyUp('ctrl')

for i in range(len(groups)):
    link = 'https://facebook.com/groups/'+groups[i]
    pyautogui.typewrite(link)
    pyautogui.typewrite('\n')

    print("Waiting for 45 seconds\n")
    time.sleep(45)

    pyautogui.typewrite('p')
    time.sleep(2)
    print("Writing post\n")
    pyautogui.typewrite("Hello there, it's a testing post from messy programmers")
    time.sleep(4)

    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('enter')
    pyautogui.keyUp('enter')
    pyautogui.keyUp('ctrl')

    time.sleep(3)

    pyautogui.write(['f6'])
    time.sleep(1)



