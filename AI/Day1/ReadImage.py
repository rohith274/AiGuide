import cv2

img = cv2.imread("sample1.png")
cv2.imwrite("sample2.png", img)
img2 = cv2.imread("sample2.png")
grayImg = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray", grayImg)

cv2.waitKey(0)
cv2.destroyAllWindows()
