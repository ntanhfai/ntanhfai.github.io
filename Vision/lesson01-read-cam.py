import cv2

# xác định đối tượng quay video
vid = cv2.VideoCapture(0)

while True:
    # Chụp từng khung hình video
    ret, frame = vid.read()

    # Hiển thị khung kết quả
    cv2.imshow('frame', frame)

    # phím 'q' được đặt làm phím thoát bạn có thể sử dụng bất kỳ phím mong muốn nào
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Sau vòng lặp, giải phóng đối tượng nắp
vid.release()
# Phá hủy tất cả các cửa sổ
cv2.destroyAllWindows()