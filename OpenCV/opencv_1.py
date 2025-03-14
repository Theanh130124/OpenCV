import cv2
img = cv2.imread("images/A.jpg",1) #path , flag
img  = cv2.resize(img,(400,200)) # rong dài
#flag
# 1 (hoặc cv2.IMREAD_COLOR): Đọc ảnh ở chế độ màu BGR (bỏ qua kênh alpha nếu có).
# 0 (hoặc cv2.IMREAD_GRAYSCALE): Đọc ảnh ở chế độ xám (grayscale).
# -1 (hoặc cv2.IMREAD_UNCHANGED): Đọc ảnh bao gồm cả kênh alpha (nếu có)

#Xoay ảnh
img = cv2.rotate(img,cv2.ROTATE_180)

cv2.imshow("Hien thi anh",img)
# Đợi người dùng nhấn phím bất kỳ để đóng cửa sổ


cv2.waitKey(0) #milisecond -> 3000 -> 3s
#nếu khong truyền phim (cv2.waitKey())  vào thì nó sẽ in ra phim được nhấn theo mã
#ASCII
cv2.destroyAllWindows()
