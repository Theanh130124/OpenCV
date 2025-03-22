import cv2
import numpy as np

cap = cv2.VideoCapture(0)
#Nếu có nhieu cam thi goi 0 thanh 1 2 3
while True:
    ret , frame = cap.read()
    # print(ret)
    #ret trả ve true , false cho camera
    width = int(cap.get(3))
    height = int(cap.get(4))
    small_frame =cv2.resize(frame,(0,0), fx=0.5 , fy = 0.5 )
    image =np.zeros(frame.shape , np.uint8)

    image[:height//2 , :width//2] = small_frame #trên trái
    image[:height // 2, width // 2:] = small_frame #tren phải
    image[height // 2:, :width // 2] = small_frame # duoi trái
    image[height //2: , width //2:] = small_frame# dưới phải

    #vẽ line
    #image = cv2.line(frame , (0,0) ,(width, height) , (255,255,255) , 0 )  \
    # điểm bắt đầu (0,0), rọng cạo , rgb , độ dày
    #Vẽ circle với rectangle cũng giống line

    cv2.imshow("CUA SO CAMERA", image)
    if cv2.waitKey(1) == ord("q"): #q thoat
        break
cap.release() # giai phong cam
cv2.destroyAllWindows()