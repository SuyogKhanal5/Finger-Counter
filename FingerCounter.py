import cv2
import mediapipe as mp
import time
import HandTrackingModule as htm

wCam, hCam = 640, 480

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

prevTime = 0

detector = htm.handDetector(detectionCon=0.75)

tipIds = [4,8,12,16,20]

while True:
        success, img = cap.read()
        img = detector.findHands(img)

        lmList = detector.findPosition(img, draw=False)

        fingers = 0

        if len(lmList) > 0:
            if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
                fingers += 1

            # 4 fingers
            for id in range(1,5):
                if lmList[tipIds[id]][2] < lmList[tipIds[id]-2][2]:
                    fingers += 1

        print("You have " + str(fingers) + " fingers open" )
                    
        currTime = time.time()
        fps = 1 / (currTime - prevTime)
        prevTime = currTime

        cv2.putText(img, str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 2) 

        cv2.imshow("Image", img) 
        cv2.waitKey(1) 


