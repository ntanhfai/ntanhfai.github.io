import os
import cv2

# xác định đối tượng quay video
vid = cv2.VideoCapture(0)
cnt = 0
while True:
    # Chụp từng khung hình video
    ret, frame = vid.read()

    # Hiển thị khung kết quả
    cv2.imshow('frame', frame)

    # phím 'q' được đặt làm phím thoát bạn có thể sử dụng bất kỳ phím mong muốn nào
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

    if key == 32: # Nhấn dấu cách để lưu ảnh
        os.makedirs('output', exist_ok=True)
        fn = f'output/{cnt}.jpg'
        cv2.imwrite(fn, frame)
        print('Anh duoc luu tai:', fn)
        cnt += 1

# Sau vòng lặp, giải phóng đối tượng nắp
vid.release()
# Phá hủy tất cả các cửa sổ
cv2.destroyAllWindows()
