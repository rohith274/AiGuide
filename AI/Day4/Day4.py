import cv2
from cv2 import resize
from cv2 import GaussianBlur
from cv2 import threshold
import imutils
img = cv2.imread("sample.jpeg")
resizeImg = imutils.resize(img, width=20)
cv2.imwrite("new1.jpeg", resizeImg)
# Guassian BLUR
GaussianBlurImg = cv2.GaussianBlur(img, (21, 21), 1)
cv2.imwrite("GaussianBlurImg.jpeg", GaussianBlurImg)
# threshold Image - If threshold is
greyImg = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)
# return values are different so we can also mention the values in ARRAYS []
thresholdimg = cv2.threshold(greyImg, 120, 255, cv2.THRESH_BINARY)[1]
cv2.imwrite("ThreshImage.jpeg", thresholdimg)
# Drawing a rectangle
rect = cv2.rectangle(img, (10, 10), (50, 50), (0, 255, 255), 2)
text = cv2.putText(rect, "Rohith", (10, 20),
                   cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 0, 0))
cv2.imwrite("rectangle.jpeg", text)
# finding Contours
cnts = cv2.findContours(rect.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cv2.imwrite("Contours.jpeg", cnts)
