import cv2 as cv
import numpy as np 


img = cv.imread('./photos/cats.jpg')
cv.imshow('cats', img)


gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#simple thresholding

threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow("Simple thresholding", thresh)

#simple thresholding inv

threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
#cv.imshow("Simple thresholding Inv", thresh_inv)

#Adaptive Thersholding
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,3)
cv.imshow("Adaptive thresholding", adaptive_thresh)

cv.waitKey(0)