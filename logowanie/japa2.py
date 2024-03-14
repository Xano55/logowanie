import cv2
from cvzone.FaceDetectionModule import FaceDecector
from cvzone.HandTrackingModule import HandDetector
from cvzone.FPS import FPS
import cvzone
import os
import mediapipe

fps = FPS(avgCount=30)
cap = cv2.VideoCapture(0)
cap.set(3, 1024)
hd = HandDetector(detectionCon = 0.6)

overlaylist = []

while True:
    success, img = cap.read()
    fps.update(img, pos = (400, 40), scale = 2, bgColor = (0,255,0))
    hand, imgs = hd.findHands(img)
    if hand:
        lefthand = hand[0]
        bbox = lefthand['bbox']
        lmlist = lefthand['mList']
        handtype = lefthand['type']
        fingersup = hd.fingersUp(lefthand)
        totalfingers = fingersup.count(1)
        cv2.putText(img, str(totalfingers), (45, 175), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 5, (255,0,0), 14)
    
    cv2.imshow("Łapy", img)
    key = cv2.waitKey(1)
    if key == 27:
        break
    
cap.release()
cv2.destroyAllWindows()