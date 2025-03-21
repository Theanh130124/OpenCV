import cv2
import time
import os
import mediapipe as mp
import hand as htm
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)  # Độ rộng của frame
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)  # Độ cao của frame

FolderPath = "Fingers"
lst = os.listdir(FolderPath) # lấy tên các ảnh trong dnah mục Fingers
lst_2 = []
pTime = 0 
for i in lst:
    image = cv2.imread(f"{FolderPath}/{i}")
    print(f"{FolderPath}/{i}")
    lst_2.append(image) #-> 6 ma trận ảnh
print(lst_2[0].shape)

finger_id = [4,8,12,16,20] # đầu ngón tay

detector = htm.HandDetector(detectionCon=0.55) #Nhận diện tay trái
while True:
    ret , frame = cap.read()
    frame = detector.findHands(frame)
    lmList = detector.findPosition(frame,draw=False)#Phát hiện vị trí đẩy ra 20 điểm là cái đốt tay
    # print(lmList)
    songontay=0
    #Kiểm tra ngón dài ( trừ ngón trỏ ) thì nó sẽ so sánh cy -> càng xuống cy càng tăng
    if len(lmList) != 0:

        fingers  = []
        #Viết cho ngón cái ( điểm 4 nằm bên trái hay phải điểm 3) -> cột 1 cx , -1 thôi vì cách nhau 1 thôi là gập r
        if lmList[finger_id[0]][1] < lmList[finger_id[0] - 1 ][1]:
            fingers.append(1)
        else:
            fingers.append(0)



        for id in range(1,5): # chạy 8 , 12 ,16, 20 -> chạy index 1-> 4
            if lmList[finger_id[id]][2] < lmList[finger_id[id] - 2 ][2]: #[2] là cột cy
                fingers.append(1) # mở thì thêm 1 vào mảng 1
            else:
                fingers.append(0) # đóng thì thêm 0 vào
        print(fingers)
        songontay = fingers.count(1)


    h,w,c = lst_2[songontay-1].shape # c kênh màu -> c=3 là rgb -> c = 4, tương ứng với RGBA

    #vẽ hình chử nhật đem ngón tay
    cv2.rectangle(frame,(0,200) , (150,400) , (0,255,0) , -1)
    cv2.putText(frame,str(songontay),(30,370), cv2.FONT_HERSHEY_PLAIN,10,(255,0,0),3)

    frame[0:h,0:w] = lst_2[songontay-1]
    cTime = time.time() # trả về giấy từ 0:00:0000 1/1/1970 theo giờ tuc

    fps = 1/(cTime-pTime) # số khung hình mỗi giây
    pTime =cTime # thời gian trước đó
    #show fps lên màn hình

    cv2.putText(frame,f'FPS: {int(fps)}',(150,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0))
    # cv2.namedWindow("CUA SO CAMERA", cv2.WND_PROP_FULLSCREEN)
    # cv2.setWindowProperty("CUA SO CAMERA", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.imshow("CUA SO CAMERA", frame)
    if cv2.waitKey(1) == ord("q"):  # q thoat
        break

cap.release()  # giai phong cam
cv2.destroyAllWindows()