import cv2
from cvzone.HandTrackingModule import  HandDetector
cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)

detector = HandDetector (detectionCon=0.6,maxHands=2)

while True:
    _,img = cap.read()
    hands, img = detector.findHands(img)
    cv2.imshow("smart Camera",img)
    if cv2.waitKey(1) == ord("q"):
        break

from pycparser.ply.yacc import resultlimit

"""
this is handdetector 
"""


