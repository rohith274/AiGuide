# import cv2
# import time # used to time delay and sleep etc..,

# cam = cv2.VideoCapture(1)  # 0 - primary camera, 1,2,3 - no of cameras respectively
# time.sleep(1)
# _,img = cam.read()#_, used beacuse cam return 2 values. 1-> flga value true/false 2-> capture so, we use that for capture
# cv2.imwrite("Photo.jpg",img)
# cam.release()
# ^^ uncomment above for  single frame capture
#video cam
import cv2
import time # used to time delay and sleep etc..,

cam = cv2.VideoCapture(1)  # 0 - primary camera, 1,2,3 - no of cameras respectively
time.sleep(1)
while True:
   _,img = cam.read()#_, used beacuse cam return 2 values. 1-> flga value true/false 2-> capture so, we use that for capture
   cv2.imshow("cameraFeed",img)
   key = cv2.waitKey(1)&0xFF
   if key == ord("q"):
       break
cam.release()
cv2.destroyAllWindows
