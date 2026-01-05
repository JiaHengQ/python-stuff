import cv2
import time



cap = cv2.VideoCapture(0)

time.sleep(1)
cap.set(cv2.CAP_PROP_AUTO_EXPOSURE, 1) 
    
# 2. Set Exposure to a fixed value (e.g., 50. Adjust this if the image is too dark or bright)
cap.set(cv2.CAP_PROP_EXPOSURE, 50) 



# 4. Disable Auto Gain (set to a fixed value)
cap.set(cv2.CAP_PROP_GAIN, 0)
ret, pic = cap.read()
xflippic = pic[:, ::-1]
size = pic.shape

#960
#540

for x in range (0, 300, 30):
    for y in range (0, 240, 30):
        cv2.circle(pic, (1560 + x, 540 + y), 5, (0,0,255), 2)
        
color = pic[715, 1645]
r,g,b = color[0], color[1], color[2]
print(r,g,b)
cv2.imshow('pic', pic)

cv2.waitKey(10000)

