# Chương trình Python giải thích phương thức cv2.putText()
import cv2

path = r'G:\Foxconn.AI\AI_Libs\Vision\output\0.jpg'
# Đọc một hình ảnh ở chế độ mặc định
image = cv2.imread(path)
# --------------------------------------------------------------------------
# Bài này chỉ cần nhớ cv2.putText để viết chữ lên ảnh là được.
# Viết 1 xâu:
font        = cv2.FONT_HERSHEY_SIMPLEX
Toa_Do      = (10, 50)
Co_Chu      = 1
Mau_Sac     = (255, 0, 255)
Kich_Co     = 2
Kieu_Net_Ve = 2
cv2.putText(image,'Hello World!', Toa_Do, font, Co_Chu, Mau_Sac, Kich_Co, Kieu_Net_Ve)
# --------------------------------------------------------------------------
cv2.putText(image,'Day la noi dung', (300, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2, 2)
# --------------------------------------------------------------------------
cv2.imshow('window_name', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
