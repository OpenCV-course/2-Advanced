import cv2 as cv
import numpy as np 


img = cv.imread('./photos/park.jpg')
cv.imshow('Park', img)

blank = np.zeros(img.shape[:2], dtype = "uint8")


b,g,r = cv.split(img)
'''
cv.imshow("Blue", b)
cv.imshow("Red", r)
cv.imshow("Green", g)
'''
print(img.shape)
print(b.shape)
print(r.shape)
print(g.shape)

merged = cv.merge([b,g,r])
cv.imshow("Merged", merged)

blue = cv.merge([b, blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])

cv.imshow("Blue", blue)
cv.imshow("Red", red)
cv.imshow("Green", green)





cv.waitKey(0)