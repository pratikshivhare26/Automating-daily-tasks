import pyautogui
import webbrowser
import time

new =2
url='https://www.linkedin.com/mynetwork/invitation-manager/?filterCriteria=ALL'

webbrowser.open(url, new=new)
time.sleep(3)
i=0

#keep the value of i according to the number of request we want to accept.

while(i<8):
    pyautogui.click(882,416)
    time.sleep(1)
    i+=1


