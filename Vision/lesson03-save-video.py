import os
import cv2

vid = cv2.VideoCapture(0) # có thể thay = path của file video

ret, frame = vid.read()
ChieuCao, ChieuRong, SoKenh = frame.shape

os.makedirs('output', exist_ok=True)
fn = 'output/video.avi'
fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
Ghi_Video = cv2.VideoWriter(fn, fourcc, 20.0, (ChieuRong, ChieuCao))

nFrame = 200
cnt = 0

while True:
    ret, frame = vid.read()
    cv2.imshow('frame', frame)
    # .........................................

    # .........................................
    key = cv2.waitKey(1)
    if key & 0xFF == ord('q'):
        break

    if cnt < nFrame:
        Ghi_Video.write(frame)
        cnt += 1
    else:
        break

print('Video duoc luu tai:', fn)
vid.release()
cv2.destroyAllWindows()
