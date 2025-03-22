import math

import cv2
import mediapipe as mp
import time

import numpy as np

import CountFingers.hand as htm
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
cap = cv2.VideoCapture(0)
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)  # Độ rộng của frame
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)  # Độ cao của frame
pTime = 0

detector = htm.HandDetector(detectionCon=0.7) #Nhận diện tay trái


devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = interface.QueryInterface(IAudioEndpointVolume)
# volume.GetMute()
# volume.GetMasterVolumeLevel()
volRange = volume.GetVolumeRange() #phạm vi âm lượng -> dãy âm lượng chạy bao nhiêu tới bao nhiêu

print(volRange) #(-96.0, 0.0, 0.125) -96 đến  0

minVol = volRange[0]
maxVol = volRange[1]



while True:
    ret , frame = cap.read()
    frame = detector.findHands(frame)
    lmList = detector.findPosition(frame, draw=False)  # Phát hiện vị trí đẩy ra 20 điểm là cái đốt tay

    if len(lmList) != 0:
        x1,y1 = lmList[4][1] , lmList[4][2] # đầu ngón trỏ
        x2, y2 = lmList[8][1], lmList[8][2] # đầu ngón cai


        #vẽ hinh tron dau cac ngón

        cv2.circle(frame,(x1,y1),15,(255,0,255),-1)
        cv2.circle(frame, (x2, y2), 15, (255, 0, 255), -1)

        #đg nói 2 ngon
        cv2.line(frame,(x1,y1),(x2,y2),(255,0,255),3)
        # // là chia nguyen
        cx,cy = (x1+x2)//2, (y1+y2)//2
        #dg tron giua
        cv2.circle(frame, (cx,cy), 15, (255, 0, 255), -1)
        #hypot tính sqrt x binh + y binh với x = x1-x2 = =y2-y1
        length = math.hypot(x2-x1,y2-y1)
        # print(length)  # in ra kc giữa 2 ngón để từ đó mình tính min và max
        #chuẩn hóa về 1 dàng  -> interp  -> ép 7 -> 250 cũng 0 -> 1 với cã min và max vol
        vol = np.interp(length,[7,250] ,[minVol,maxVol])
        volBar = np.interp(length,[7,250],[400,150]) # thay đổi volBar
        vol_tyle = np.interp(length,[7,250],[0,100]) # tu 0 den 100 %
        #in ra thấy ngón tay co nhất la 7 max la 250

        #dãi âm lượng từ (-96.0, 0.0)
        volume.SetMasterVolumeLevel(vol, None) # sẽ set âm thanh vào -20 nếu truyền -20
        if length < 7 : #min thì cho màu xanh thôi
            cv2.circle(frame, (cx, cy), 15, (0, 255, 0), -1)
        cv2.rectangle(frame,(50,150),(100,400),(0,255,0),3)

        cv2.rectangle(frame, (50, int(volBar)), (100, 400), (0, 255, 0), -1) # -1 sẽ lắp đầy

        cv2.putText(frame, f' {int(vol_tyle)} %', (40, 240), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0))
    cTime = time.time() # trả về giấy từ 0:00:0000 1/1/1970 theo giờ tuc

    fps = 1/(cTime-pTime) # số khung hình mỗi giây
    pTime =cTime # thời gian trước đó
    #show fps lên màn hình

    cv2.putText(frame,f'FPS: {int(fps)}',(150,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0))
    cv2.imshow("CUA SO CAMERA",frame)
    if cv2.waitKey(1) == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
