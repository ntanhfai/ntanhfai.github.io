"""
Viết hàm cho các bài toán sau:
1. Xoay ảnh:
- Type1: Xoay ảnh giữ nguyên kích thước ban đầu, có thể mất góc cạnh
- Type2: Xoay ảnh giữ nguyên nội dung, thay đổi kích thước ảnh, phần thiếu thì bù nền đen vào

Mẫu:
def fnRotateImage_type1(image, angle):
    # ...
    return image
def fnRotateImage_type2(image, angle):
    # ...
    return image

2. Crop ảnh:
Nhập vào tọa độ x1,y1,x2,y2 trả về image trong vùng ảnh đó
Mẫu:
def fnCrop(image, x1,y1,x2,y2):
    imgCrop=
    return imgCrop

3. Tách màu, chuyển hệ màu
Viết hàm chuyển màu từ hệ màu BRG sang HSL, đầu vào là image, đầu ra là 3 kênh màu của ảnh đó: H, S, L
Mẫu:
def fnBRG_2HSL(image):

    return H,S,L
"""
import cv2


def fnRotateImage_type1(image, angle, a=1):
    # ...
    return image


def fnRotateImage_type2(image, angle):
    # ...
    return image


def fnCrop(image, x1, y1, x2, y2):
    imgCrop = image[y1:y2, x1:x2]
    return imgCrop


def fnBRG_2HSL(imageBGR):
    H, S, L = 1, 1, 1
    return H, S, L


if __name__ == "__main__":
    imPath = '...'
    image = cv2.imread(imPath)
    test = 1
    if test == 1:
        im1 = fnRotateImage_type1(image, angle=30.5)
        cv2.imshow('fnRotateImage_type1', im1)
        cv2.waitkey(0)
    if test == 2:
        im2 = fnCrop(image, x1=30, y1=100, x2=200, y2=300)
        cv2.imshow('fnRotateImage_type1', im1)
        cv2.waitkey(0)
    if test == 3:
        # ...
        
        pass
    if test == 4:
        # ...
        
        pass
    cv2.destroyAllWindows()
    
    # hết hàm mẫu
