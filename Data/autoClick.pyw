import pyautogui # for the click function
import keyboard # for the keyboard.is_pressed function


# is a autoclicker
while(True): #runs forever unless specific key is clicked
    pyautogui.click()
    if keyboard.is_pressed('Home'): # specified key is home key but can be changed
        break
        '''does about 10 clicks per
            second so about average human speed minus stamina speed loss'''
           
