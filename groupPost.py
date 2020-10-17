#script to write make some post on defined facebook pages

## we call the module pyautogui (a piece of code already programend)
import pyautogui
## make the same with time
import time

#we define a list to a variable. this numbers are the ids of the facebook pages we are going to post.
groups = ['251123409000385','843804142348443','900389246658181']

#make pause of 5 seconds to focus on the window of the browser with facebook page opened
time.sleep(5)

#the following simulate key presses (control+t and the releases it), that combination makes a new tab to open
pyautogui.keyDown('ctrl')
pyautogui.keyDown('t')
pyautogui.keyUp('t')
pyautogui.keyUp('ctrl')

#here comes the action
##a loop to the end of the script

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



