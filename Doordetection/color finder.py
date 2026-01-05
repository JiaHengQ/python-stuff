import cv2
import time


# Input position here
a, b = 1770, 720
# Input position here
rlist = []
glist = []
blist = []
for i in range (30):
    cap = cv2.VideoCapture(0)
    time.sleep(1)
    cap.set(cv2.CAP_PROP_AUTO_EXPOSURE, 1) 
    cap.set(cv2.CAP_PROP_EXPOSURE, 50) 
    cap.set(cv2.CAP_PROP_GAIN, 0)
    
    ret, pic = cap.read()
    xflippic = pic[:, ::-1]
    size = pic.shape

    cv2.circle(pic, (a, b), 1, (0,0,255), 1)
    color = pic[715, 1645]
    r,g,b = int(color[0]), int(color[1]), int(color[2])
    rlist.append(r)
    glist.append(g)
    blist.append(b)
    
    
r0 = 0
g0 = 0
b0 = 0
for i in rlist:
    r0 += i
for i in glist:
    g0 += i
for i in blist:
    b0 += i
a,b,c = r0//len(rlist), g0//len(glist),b0//len(blist)
print(f'{a}, {b}, {c}')