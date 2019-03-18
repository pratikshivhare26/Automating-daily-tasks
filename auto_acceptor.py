
#install this libraries before performing in your python3
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
    #the value of pixel below is as per the position of accept button on linkedIn as per mac 13inch model.
    #hope this wont change change or affect for any similar size model
    #just in case it does not click at 'accept button' then ping me to know how to see the pixel position in your pc.
    pyautogui.click(882,416)
    time.sleep(1.1)
    i+=1


