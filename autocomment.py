#first import de modules 

## import puautogui for automation of gui aplications
import pyautogui
## import or call the module time for delay
import time

#here a list of comments you can throw
comments = ["Hi","Just commenting for fun","Checking my python comment bot","Just for fun","I am just checking my python skill","python is awesome","I am a messy programmer"]

#from module `time` which is imported we call the function `sleep` giving it the value "5". 5 would be the seconds focusing on the clock, in our case a delay of 5 secs. 
time.sleep(5)

#here cames a loop 
##it'll go through a element of the list previously defined, as a variable that we called `comments`
for element in range(10):
    pyautogui.typewrite(comments[element%7])
    pyautogui.typewrite("\n")
    #we "wait 2 seconds" until go to the next element
    time.sleep(2)
