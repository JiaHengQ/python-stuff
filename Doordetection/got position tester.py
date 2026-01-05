import cv2
import time



cap = cv2.VideoCapture(0)
time.sleep(1)
cap.set(cv2.CAP_PROP_AUTO_EXPOSURE, 1) 
cap.set(cv2.CAP_PROP_EXPOSURE, 50) 
cap.set(cv2.CAP_PROP_GAIN, 0)

ret, pic = cap.read()
xflippic = pic[:, ::-1]
size = pic.shape



# change these 2 value for number of circles there are
circlenumber1, circlenumber2 = 8, 7
# change these 2 value for number of circles there are




cv2.circle(pic, (1560 + (circlenumber1 * 30) - 30, 540 + (circlenumber2 * 30 - 30)), 5, (0,0,255), 2)
color = pic[715, 1645]
r,g,b = color[0], color[1], color[2]
cv2.imshow('pic', pic)

cv2.waitKey(3000)

a = 1560 + (circlenumber1 * 30) - 30
b = 540 + (circlenumber2 * 30) - 30
print(f'{a}, {b}')