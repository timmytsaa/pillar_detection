import numpy as np
import cv2 as cv
from math import sqrt
import time,glob,os

cap = cv.VideoCapture(0) #0 is camera by default
ret,frame = cap.read()
cap.release() #taking a shot and close camera

if ret:
    filename = f"photo_{int(time.time())}.jpg"
    cv.imwrite(filename,frame)
    print("photo is saved as: {filename}")
    
    latest_img = max(glob.glob("photo_*.jpg"),key = os.path.getctime)
    img = cv.imread(latest_img)
    if img is None:
        print("Fail to read the photo")
    else:
        cv.imshow("Latest Image",img)
        cv.waitkey(0)
        cv.destroyAllWindows()
else:
    print("Fail to take shot")
        

img = cv.medianBlur(img, 5)
cv.imshow("tt",img)
cv.waitKey(0)


#test1
x1=200;y1=480
x2=580;y2=730
x3=200;y3=980
'''
#test2
x1=200;y1=430
x2=560;y2=700
x3=190;y3=950
'''
'''
#test3
x1=195;y1=335
x2=595;y2=600
x3=200;y3=860
'''
w=80;h=100
img1 = img[y1:y1+h,x1:x1+w]
img2 = img[y2:y2+h,x2:x2+w]
img3 = img[y3:y3+h,x3:x3+w]

img1 = cv.resize(img1,(300,400))
img2 = cv.resize(img2,(300,400))
img3 = cv.resize(img3,(300,400))
cv.imshow("tt",img3)
cv.waitKey(0)

#img1
cimg1 = cv.cvtColor(img1, cv.COLOR_GRAY2BGR)
circles_img1_1 = cv.HoughCircles(img1,cv.HOUGH_GRADIENT, 2, 10,
                          param1=30,param2=50,minRadius =70,maxRadius=80)

circles_img1_2 = cv.HoughCircles(img1,cv.HOUGH_GRADIENT, 2, 10,
                          param1=30,param2=50,minRadius =25,maxRadius=40)
assert circles_img1_1 is not None,"WRONG,there isn't any detection @circles_img1_1"
assert circles_img1_2 is not None,"WRONG,there isn't any detection @circles_img1_2"

circles_img1_1 = np.uint16(np.around(circles_img1_1))
circles_img1_2 = np.uint16(np.around(circles_img1_2))

cv.circle(cimg1, (circles_img1_1[0,0,0],circles_img1_1[0,0,1]),circles_img1_1[0,0,2],(0,255,0),2)
cv.circle(cimg1, (circles_img1_1[0,0,0],circles_img1_1[0,0,1]),2,(0,0,255),3)

cv.circle(cimg1, (circles_img1_2[0,0,0],circles_img1_2[0,0,1]),circles_img1_2[0,0,2],(0,255,0),2)
cv.circle(cimg1, (circles_img1_2[0,0,0],circles_img1_2[0,0,1]),2,(0,0,255),3)

#center-distance of img1
dx_img1 = int(circles_img1_1[0,0,0])-int(circles_img1_2[0,0,0])
dy_img1 = int(circles_img1_1[0,0,1])-int(circles_img1_2[0,0,1])
cen_dist_img1 = sqrt(pow(dx_img1,2)+pow(dy_img1,2))


if cen_dist_img1 >= circles_img1_2[0,0,2]:
    print('pillar1 is fail')
elif cen_dist_img1 + circles_img1_2[0,0,2] >= circles_img1_1[0,0,2] >= cen_dist_img1 + circles_img1_2[0,0,2] - 1:
    print('pillar1 is fail')
else:
    print('pillar1 is pass')

cv.imshow('detect circles',cimg1)
cv.waitKey(0)
cv.destroyAllWindows()

#img2
cimg2 = cv.cvtColor(img2, cv.COLOR_GRAY2BGR)
circles_img2_1 = cv.HoughCircles(img2,cv.HOUGH_GRADIENT, 2, 10,
                          param1=30,param2=50,minRadius =70,maxRadius=80)

circles_img2_2 = cv.HoughCircles(img2,cv.HOUGH_GRADIENT, 2, 10,
                          param1=30,param2=50,minRadius =25,maxRadius=40)
assert circles_img2_1 is not None,"WRONG,there isn't any detection @circles_img2_1"
assert circles_img2_2 is not None,"WRONG,there isn't any detection @circles_img2_2"

circles_img2_1 = np.uint16(np.around(circles_img2_1))
circles_img2_2 = np.uint16(np.around(circles_img2_2))

cv.circle(cimg2, (circles_img2_1[0,0,0],circles_img2_1[0,0,1]),circles_img2_1[0,0,2],(0,255,0),2)
cv.circle(cimg2, (circles_img2_1[0,0,0],circles_img2_1[0,0,1]),2,(0,0,255),3)

cv.circle(cimg2, (circles_img2_2[0,0,0],circles_img2_2[0,0,1]),circles_img2_2[0,0,2],(0,255,0),2)
cv.circle(cimg2, (circles_img2_2[0,0,0],circles_img2_2[0,0,1]),2,(0,0,255),3)

#center-distance of img2
dx_img2 = int(circles_img2_1[0,0,0])-int(circles_img2_2[0,0,0])
dy_img2 = int(circles_img2_1[0,0,1])-int(circles_img2_2[0,0,1])
cen_dist_img2 = sqrt(pow(dx_img2,2)+pow(dy_img2,2))

if cen_dist_img2 >= circles_img2_2[0,0,2]:
    print('pillar2 is fail')
elif cen_dist_img2 + circles_img2_2[0,0,2] >= circles_img2_1[0,0,2] >= cen_dist_img2 + circles_img2_2[0,0,2] - 1:
    print('pillar2 is fail')
else:
    print('pillar2 is pass')

cv.imshow('detect circles',cimg2)
cv.waitKey(0)
cv.destroyAllWindows()

#img3
cimg3 = cv.cvtColor(img3, cv.COLOR_GRAY2BGR)
circles_img3_1 = cv.HoughCircles(img3,cv.HOUGH_GRADIENT, 2, 10,
                          param1=30,param2=50,minRadius =70,maxRadius=80)

circles_img3_2 = cv.HoughCircles(img3,cv.HOUGH_GRADIENT, 2, 10,
                          param1=30,param2=50,minRadius =1,maxRadius=30)
assert circles_img3_1 is not None,"WRONG,there isn't any detection @circles_img3_1"
assert circles_img3_2 is not None,"WRONG,there isn't any detection @circles_img3_2"

circles_img3_1 = np.uint16(np.around(circles_img3_1))
circles_img3_2 = np.uint16(np.around(circles_img3_2))

cv.circle(cimg3, (circles_img3_1[0,0,0],circles_img3_1[0,0,1]),circles_img3_1[0,0,2],(0,255,0),2)
cv.circle(cimg3, (circles_img3_1[0,0,0],circles_img3_1[0,0,1]),2,(0,0,255),3)

cv.circle(cimg3, (circles_img3_2[0,0,0],circles_img3_2[0,0,1]),circles_img3_2[0,0,2],(0,255,0),2)
cv.circle(cimg3, (circles_img3_2[0,0,0],circles_img3_2[0,0,1]),2,(0,0,255),3)

#center-distance of img3
dx_img3 = int(circles_img3_1[0,0,0])-int(circles_img3_2[0,0,0])
dy_img3 = int(circles_img3_1[0,0,1])-int(circles_img3_2[0,0,1])
cen_dist_img3 = sqrt(pow(dx_img3,2)+pow(dy_img3,2))

if cen_dist_img3 >= circles_img3_2[0,0,2]:
    print('pillar3 is fail')
elif cen_dist_img3 + circles_img3_2[0,0,2] >= circles_img3_1[0,0,2] >= cen_dist_img3 + circles_img3_2[0,0,2] - 1:
    print('pillar3 is fail')
else:
    print('pillar3 is pass')

cv.imshow('detect circles',cimg3)
cv.waitKey(0)
cv.destroyAllWindows()