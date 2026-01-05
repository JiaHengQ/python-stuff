import time
import pyautogui as py
from pynput import keyboard as kb
import threading
import mss
import mss.tools
import cv2
import pytesseract as pyt
import numpy as np
import os
py.PAUSE = 0
on_off_1 = False
on_off_2 = False
#add on_off_2 for second marco
pyt.pytesseract.tesseract_cmd = r'/opt/homebrew/bin/tesseract'
#---------------
key1 = None
key2 = None
key3 = None
key4 = None
key5 = None
#---------------

def the_code():
    global on_off_1
    while True:
        if on_off_1 == True:
            startingx, startingy = 1019, 681
            width, height = 439, 200
            monitor = {"top": startingy, "left": startingx, "width": width, "height": height}

            #tempary screen png
            tsp = 'tsp.png'

            with mss.mss() as sct:
                captureimage = sct.grab(monitor)
                screenimage1 = np.array(captureimage) #mss.tools doesnt use np.arrat so its kinda useless
                mss.tools.to_png(captureimage.rgb, captureimage.size, output=tsp)

            screenimage = cv2.imread(tsp, cv2.IMREAD_COLOR)
            greyscreenimage = cv2.cvtColor(screenimage, cv2.COLOR_BGR2GRAY)
            _, binaryscreenimage = cv2.threshold(greyscreenimage, 100, 255, cv2.THRESH_BINARY_INV)#pyt require binary image

            rawtext = pyt.image_to_string(binaryscreenimage) 
            if "Fishing" in rawtext:
                py.press('.')
                time.sleep(3)
                py.press('.')
            else:
                pass
            os.remove(tsp)
            time.sleep(0.1)
            pass

def countdown():
    while True:
        if on_off_2 == True:
            time.sleep(120)
            if on_off_2 == True:
                py.press('1')
                time.sleep(0.1)
                py.press('9')
                time.sleep(0.1)
                py.press('.')

def turn_on():
    global on_off_1, countdownthread
    on_off_1 = True
    on_off_2 = False
    py.press('.')
def turn_off():
    global on_off_1
    on_off_1 = False
    on_off_2 = False
#copy paste turn_on turn_off for second marcro, change on_off_1 to on_off_2
hotkeys = {"o+p": turn_on, "i+o": turn_off}
#add second hotkey set if second macro
    
if __name__ == "__main__":

    click_thread = threading.Thread(target=the_code)
    click_thread.daemon = True
    click_thread.start()
    
    thread = threading.Thread(target=countdown)
    thread.daemon = True
    thread.start()
    
    with kb.GlobalHotKeys(hotkeys) as hotkey:
        hotkey.join()