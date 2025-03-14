import cv2
img = cv2.imread("images/A.jpg",1)

# print(img) # hình ảnh sẽ được biển diễn bởi ma trận điểm
# print(type(img)) #numpy -> tối ưu khi hoạt động ới mảng
# print(img.shape) # Chiều cao ,(dòng ma trận) chiều rộng  , chanel (cột ma trận)



#Vung mà học máy chọn của ảnh


#0:100 -> chiều cao từ 0 đến 100
#500:700 -> chiều rộng từ 500 đến 700
vungchon = img[0:100,500:700]

cv2.imshow("Anh",img)
cv2.waitKey()