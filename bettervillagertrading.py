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
wantedenc = ['ending', 'Unbreaking', 'Im']

py.PAUSE = 0
on_off_1 = False
pyt.pytesseract.tesseract_cmd = r'/opt/homebrew/bin/tesseract'
#add on_off_2 for second marco
gstartingx, gstartingy = 611, 43
gwidth, gheight = 217, 51
gmonitor = {"top": gstartingy, "left": gstartingx, "width": gwidth, "height": gheight}
bstartingx, bstartingy = 573, 275
bwidth, bheight = 300, 90
bmonitor = {"top": bstartingy, "left": bstartingx, "width": bwidth, "height": bheight}
b1startingx, b1startingy = 595, 337
b1width, b1height = 360, 86
b1monitor = {"top": b1startingy, "left": b1startingx, "width": b1width, "height": b1height}
tsp = 'tsp.png'
gtext = 'ee'
btext = None
countdowntimer = 0
latteraction = True
#---------------
key1 = None
key2 = None
key3 = None
key4 = None
key5 = None
#---------------

def the_code():
    global on_off_1
    global countdowntimer
    global latteraction
    while True:
        if on_off_1 == True:
            global gtext
            global btext
            time.sleep(0.1)
            py.keyDown('.')
            time.sleep(0.1)
            py.keyUp('.')
            
            py.keyDown('d')
            time.sleep(0.5)
            py.keyUp('d')
            # detect when accept job
            gtext = 'ee'
            while 'brar' not in gtext:
                with mss.mss() as sct:
                    gcaptureimage = sct.grab(gmonitor)
                    mss.tools.to_png(gcaptureimage.rgb, gcaptureimage.size, output = tsp)
                pngread = cv2.imread(tsp, cv2.IMREAD_COLOR)
                greypngread = cv2.cvtColor(pngread, cv2.COLOR_BGR2GRAY)
                _, binarypngread = cv2.threshold(greypngread, 100 ,255, cv2.THRESH_BINARY_INV)
                gtext = pyt.image_to_string(binarypngread)
                time.sleep(0.1)
                countdowntimer += 1
            time.sleep(0.5)
            py.press('.')
            time.sleep(0.5)
            countdowntimer = 0
            
            py.moveTo(563, 330)
            time.sleep(0.2)
            with mss.mss() as sct:
                bcaptureimage = sct.grab(bmonitor)
            mss.tools.to_png(bcaptureimage.rgb, bcaptureimage.size, output = tsp)
            pngread = cv2.imread(tsp, cv2.IMREAD_COLOR)
            greypngread = cv2.cvtColor(pngread, cv2.COLOR_BGR2GRAY)
            _, binarypngread = cv2.threshold(greypngread, 100 ,255, cv2.THRESH_BINARY_INV)
            btext = pyt.image_to_string(binarypngread)
            time.sleep(0.1)
            for i in wantedenc:
                if i in btext:
                    py.click()
                    py.moveTo(1001, 383)
                    py.press('q')
                    time.sleep(0.1)
                    py.press('esc')
                    time.sleep(0.1)
                    py.keyDown('s')
                    time.sleep(1.5)
                    py.keyUp('s')
                    time.sleep(5)
                    py.keyDown('w')
                    time.sleep(1.5)
                    py.keyUp('w')
                    latteraction = False
                    
            time.sleep(0.1)
            
            
            py.moveTo(566, 389)
            time.sleep(0.2)
            with mss.mss() as sct:
                b1captureimage = sct.grab(b1monitor)
            mss.tools.to_png(b1captureimage.rgb, b1captureimage.size, output = tsp)
            pngread = cv2.imread(tsp, cv2.IMREAD_COLOR)
            greypngread = cv2.cvtColor(pngread, cv2.COLOR_BGR2GRAY)
            _, binarypngread = cv2.threshold(greypngread, 100 ,255, cv2.THRESH_BINARY_INV)
            btext = pyt.image_to_string(binarypngread)
            time.sleep(0.1)
            for i in wantedenc:
                if i in btext:
                    py.click()
                    py.moveTo(1001, 383)
                    py.press('q')
                    time.sleep(0.1)
                    py.press('esc')
                    time.sleep(0.1)
                    py.keyDown('s')
                    time.sleep(1.5)
                    py.keyUp('s')
                    time.sleep(8)
                    py.keyDown('w')
                    time.sleep(1.5)
                    py.keyUp('w')
                    
            time.sleep(0.1)

            if latteraction == True:
                py.press('esc')
                time.sleep(0.1)
            latteraction = True
            
            py.keyDown('a')
            time.sleep(0.7)
            py.keyUp('a')

            py.keyDown(',')
            time.sleep(0.5)
            py.keyUp(',')
            
            pass
def countdown():
    global countdowntimer
    if countdowntimer > 20:

        py.keyDown('a')
        time.sleep(1)
        py.keyUp('a')
        
        py.keyDown(',')
        time.sleep(0.5)
        py.keyUp(',')
        
        time.sleep(0.2)
        py.press('.')
        
        time.sleep(0.2)
        py.keyDown('d')
def turn_on():
    global on_off_1
    on_off_1 = True

def turn_off():
    global on_off_1
    on_off_1 = False
#copy paste turn_on turn_off for second marcro, change on_off_1 to on_off_2
hotkeys = {"o+p": turn_on, "i": turn_off}
#add second hotkey set if second macro
    
if __name__ == "__main__":

    click_thread = threading.Thread(target=the_code)
    click_thread.daemon = True
    click_thread.start()

    click_thread = threading.Thread(target=countdown)
    click_thread.daemon = True
    click_thread.start()
    with kb.GlobalHotKeys(hotkeys) as hotkey:
        hotkey.join()
        
        