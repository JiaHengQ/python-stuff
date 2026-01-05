import cv2
import time
import pyautogui
time.sleep(5)
pyautogui.PAUSE = 0
# change this every time
x, y = 1770, 720
wr, wg, wb = 200, 218, 222
tol = 30

while True:
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_AUTO_EXPOSURE, 1) 
    cap.set(cv2.CAP_PROP_EXPOSURE, 50) 
    cap.set(cv2.CAP_PROP_GAIN, 0)
    
    ret, pic = cap.read()
    xflippic = pic[:, ::-1]
    size = pic.shape

    color = pic[715, 1645]
    r,g,b = color[0], color[1], color[2]
    if wr - tol < r < wr + tol and wg - tol < g < wg + tol and wb -tol < b < wb+tol:
        pyautogui.press('1')
    else:
        pyautogui.press('2')







