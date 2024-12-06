# Chương trình Python giải thích phương thức cv2.rectangle()
import cv2

path = r'G:\Foxconn.AI\AI_Libs\Vision\output\0.jpg'
# Đọc một hình ảnh ở chế độ mặc định
image = cv2.imread(path)
# --------------------------------------------------------------------------
# Bài này chỉ cần nhớ cv2.rectangle để vẽ hình chữ nhật lên ảnh là được

TrenTrai = (100, 150)  # Tọa độ bắt đầu, ở đây (5, 5) đại diện cho góc trên cùng bên trái của hình chữ nhật
DuoiPhai = (400, 450) # Tọa độ kết thúc, ở đây (400, 450) đại diện cho góc dưới cùng bên phải của hình chữ nhật
Mau_Sac = (255, 0, 0)  # Blue color in BGR
Kich_Co = 2  # Line thickness of 2 px

# Sử dụng phương thức cv2.rectangle()
# Vẽ một hình chữ nhật có đường viền màu xanh lam có độ dày 2 px
image = cv2.rectangle(image, TrenTrai, DuoiPhai, Mau_Sac, Kich_Co)
# --------------------------------------------------------------------------
image = cv2.rectangle(image, (10, 30), (50, 90), (0, 0, 255), 4)
# --------------------------------------------------------------------------
# Hiển thị hình ảnh
cv2.imshow('Ten', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
