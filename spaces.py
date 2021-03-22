import cv2 as cv
import matplotlib.pyplot as plt 

img = cv.imread("./photos/park.jpg")
cv.imshow("Park", img)

#BGR to Gray
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

#BGR to hsv
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow("HSV", hsv)

#BGR to l+a+b
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow("Lab", lab)


# lab to BGR
lab_bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
cv.imshow('LAB --> BGR', lab_bgr)





cv.waitKey(0)