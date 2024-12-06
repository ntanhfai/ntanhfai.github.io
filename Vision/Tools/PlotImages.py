"""
Tuấn Anh, nt.anh.fai@gmail.com
Create Date: $
Create Time: $
"""
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


def PlotImages(image_paths, n, m, output_path, final_width = 800, final_height = 600):
    num_images = len(image_paths)
    # if num_images < n * m:
    #     print("Không đủ ảnh để hiển thị.")
    #     return
    
    # Khởi tạo mảng để lưu trữ các ảnh
    images = []
     
    final_image = Image.new('RGB', (final_width, final_height))
    
    # Tính toán kích thước của từng ảnh con trong ô gộp
    image_width = final_width // m
    image_height = final_height // n
    maxImgs=min(len(image_paths),m*n)
    # Đọc và thêm các ảnh vào mảng sau khi resize
    for i in range(maxImgs):
        img = Image.open(image_paths[i])
        img1 = img.resize((image_width, image_height), Image.ANTIALIAS)  # Resize ảnh
        images.append(img1)
    
    # Tạo hình ảnh gộp với các ảnh đã được resize
    for i in range(n):
        for j in range(m):
            index = i * m + j
            if index<len(images):
                final_image.paste(images[index], (j * image_width, i * image_height))
    
    # Hiển thị hoặc lưu ảnh gộp
    final_image.show()
    # final_image.save(output_path)


if __name__ == '__main__':
    # Sử dụng hàm PlotImages
    image_paths = [
        r"E:\DATA-U6_LR_PRO\03_Images\2022-10-17\TEST RANDOM 1710\Predict_org\U6_LR\IP=U6_LR-Time=22-10-17--09-03-04_394517-MAC=.jpg",
        r"E:\DATA-U6_LR_PRO\03_Images\2022-10-17\TEST RANDOM 1710\Predict_org\U6_LR\IP=U6_LR-Time=22-10-17--09-03-46_424265-MAC=.jpg",
        r"E:\DATA-U6_LR_PRO\03_Images\2022-10-17\TEST RANDOM 1710\Predict_org\U6_LR\IP=U6_LR-Time=22-10-17--09-04-00_968218-MAC=.jpg",
        r"E:\DATA-U6_LR_PRO\03_Images\2022-10-17\TEST RANDOM 1710\Predict_org\U6_LR\IP=U6_LR-Time=22-10-17--09-04-12_519529-MAC=.jpg",
        r"E:\DATA-U6_LR_PRO\03_Images\2022-10-17\TEST RANDOM 1710\Predict_org\U6_LR\IP=U6_LR-Time=22-10-17--09-04-17_915447-MAC=.jpg",
        r"E:\DATA-U6_LR_PRO\03_Images\2022-10-17\TEST RANDOM 1710\Predict_org\U6_LR\IP=U6_LR-Time=22-10-17--09-04-25_638488-MAC=.jpg",
        r"E:\DATA-U6_LR_PRO\03_Images\2022-10-17\TEST RANDOM 1710\Predict_org\U6_LR\IP=U6_LR-Time=22-10-17--09-07-21_368959-MAC=.jpg",
        r"E:\DATA-U6_LR_PRO\03_Images\2022-10-17\TEST RANDOM 1710\Predict_org\U6_LR\IP=U6_LR-Time=22-10-17--09-07-36_684015-MAC=.jpg",
        r"E:\DATA-U6_LR_PRO\03_Images\2022-10-17\TEST RANDOM 1710\Predict_org\U6_LR\IP=U6_LR-Time=22-10-17--09-07-51_644710-MAC=.jpg",
        r"E:\DATA-U6_LR_PRO\03_Images\2022-10-17\TEST RANDOM 1710\Predict_org\U6_LR\IP=U6_LR-Time=22-10-17--09-08-04_993788-MAC=.jpg",
        r"E:\DATA-U6_LR_PRO\03_Images\2022-10-17\TEST RANDOM 1710\Predict_org\U6_LR\IP=U6_LR-Time=22-10-17--09-08-47_198452-MAC=.jpg",
        r"E:\DATA-U6_LR_PRO\03_Images\2022-10-17\TEST RANDOM 1710\Predict_org\U6_LR\IP=U6_LR-Time=22-10-17--09-24-16_714891-MAC=.jpg",
        r"E:\DATA-U6_LR_PRO\03_Images\2022-10-17\TEST RANDOM 1710\Predict_org\U6_LR\IP=U6_LR-Time=22-10-17--09-24-49_771723-MAC=.jpg",
        r"E:\DATA-U6_LR_PRO\03_Images\2022-10-17\TEST RANDOM 1710\Predict_org\U6_LR\IP=U6_LR-Time=22-10-17--09-26-32_147710-MAC=.jpg",
        r"E:\DATA-U6_LR_PRO\03_Images\2022-10-17\TEST RANDOM 1710\Predict_org\U6_LR\IP=U6_LR-Time=22-10-17--09-27-05_613467-MAC=.jpg",
        r"E:\DATA-U6_LR_PRO\03_Images\2022-10-17\TEST RANDOM 1710\Predict_org\U6_LR\IP=U6_LR-Time=22-10-17--09-27-38_687059-MAC=.jpg",
    ]
    image_paths1=[
        r"E:\DATA-U6_LR_PRO\03_Images\2022-10-17\TEST RANDOM 1710\Predict_org\U6_LR\IP=U6_LR-Time=22-10-17--08-55-55_502904-MAC=.jpg",
        r"E:\DATA-U6_LR_PRO\03_Images\2022-10-17\TEST RANDOM 1710\Predict_org\U6_LR\IP=U6_LR-Time=22-10-17--08-56-19_198976-MAC=.jpg",
        r"E:\DATA-U6_LR_PRO\03_Images\2022-10-17\TEST RANDOM 1710\Predict_org\U6_LR\IP=U6_LR-Time=22-10-17--08-56-54_035106-MAC=.jpg",
        r"E:\DATA-U6_LR_PRO\03_Images\2022-10-17\TEST RANDOM 1710\Predict_org\U6_LR\IP=U6_LR-Time=22-10-17--08-57-09_776945-MAC=.jpg",
        r"E:\DATA-U6_LR_PRO\03_Images\2022-10-17\TEST RANDOM 1710\Predict_org\U6_LR\IP=U6_LR-Time=22-10-17--08-57-28_695939-MAC=.jpg",
        r"E:\DATA-U6_LR_PRO\03_Images\2022-10-17\TEST RANDOM 1710\Predict_org\U6_LR\IP=U6_LR-Time=22-10-17--08-57-41_285304-MAC=.jpg",
        r"E:\DATA-U6_LR_PRO\03_Images\2022-10-17\TEST RANDOM 1710\Predict_org\U6_LR\IP=U6_LR-Time=22-10-17--08-57-51_031268-MAC=.jpg",
        r"E:\DATA-U6_LR_PRO\03_Images\2022-10-17\TEST RANDOM 1710\Predict_org\U6_LR\IP=U6_LR-Time=22-10-17--08-58-04_953542-MAC=.jpg",
        r"E:\DATA-U6_LR_PRO\03_Images\2022-10-17\TEST RANDOM 1710\Predict_org\U6_LR\IP=U6_LR-Time=22-10-17--08-58-15_309986-MAC=.jpg",
        r"E:\DATA-U6_LR_PRO\03_Images\2022-10-17\TEST RANDOM 1710\Predict_org\U6_LR\IP=U6_LR-Time=22-10-17--08-58-24_505650-MAC=.jpg",
        r"E:\DATA-U6_LR_PRO\03_Images\2022-10-17\TEST RANDOM 1710\Predict_org\U6_LR\IP=U6_LR-Time=22-10-17--08-59-56_345626-MAC=.jpg",
        r"E:\DATA-U6_LR_PRO\03_Images\2022-10-17\TEST RANDOM 1710\Predict_org\U6_LR\IP=U6_LR-Time=22-10-17--09-00-09_855131-MAC=.jpg",
        r"E:\DATA-U6_LR_PRO\03_Images\2022-10-17\TEST RANDOM 1710\Predict_org\U6_LR\IP=U6_LR-Time=22-10-17--09-00-19_225374-MAC=.jpg",
        r"E:\DATA-U6_LR_PRO\03_Images\2022-10-17\TEST RANDOM 1710\Predict_org\U6_LR\IP=U6_LR-Time=22-10-17--09-00-50_893788-MAC=.jpg",
        r"E:\DATA-U6_LR_PRO\03_Images\2022-10-17\TEST RANDOM 1710\Predict_org\U6_LR\IP=U6_LR-Time=22-10-17--09-02-06_631146-MAC=.jpg",
        r"E:\DATA-U6_LR_PRO\03_Images\2022-10-17\TEST RANDOM 1710\Predict_org\U6_LR\IP=U6_LR-Time=22-10-17--09-02-39_490569-MAC=.jpg",
        r"E:\DATA-U6_LR_PRO\03_Images\2022-10-17\TEST RANDOM 1710\Predict_org\U6_LR\IP=U6_LR-Time=22-10-17--09-03-04_394517-MAC=.jpg",
        r"E:\DATA-U6_LR_PRO\03_Images\2022-10-17\TEST RANDOM 1710\Predict_org\U6_LR\IP=U6_LR-Time=22-10-17--09-03-46_424265-MAC=.jpg",
        r"E:\DATA-U6_LR_PRO\03_Images\2022-10-17\TEST RANDOM 1710\Predict_org\U6_LR\IP=U6_LR-Time=22-10-17--09-04-00_968218-MAC=.jpg",
        r"E:\DATA-U6_LR_PRO\03_Images\2022-10-17\TEST RANDOM 1710\Predict_org\U6_LR\IP=U6_LR-Time=22-10-17--09-04-12_519529-MAC=.jpg",
        r"E:\DATA-U6_LR_PRO\03_Images\2022-10-17\TEST RANDOM 1710\Predict_org\U6_LR\IP=U6_LR-Time=22-10-17--09-04-17_915447-MAC=.jpg",
        r"E:\DATA-U6_LR_PRO\03_Images\2022-10-17\TEST RANDOM 1710\Predict_org\U6_LR\IP=U6_LR-Time=22-10-17--09-04-25_638488-MAC=.jpg",
        r"E:\DATA-U6_LR_PRO\03_Images\2022-10-17\TEST RANDOM 1710\Predict_org\U6_LR\IP=U6_LR-Time=22-10-17--09-04-33_221491-MAC=.jpg",
        r"E:\DATA-U6_LR_PRO\03_Images\2022-10-17\TEST RANDOM 1710\Predict_org\U6_LR\IP=U6_LR-Time=22-10-17--09-05-05_908388-MAC=.jpg",
        r"E:\DATA-U6_LR_PRO\03_Images\2022-10-17\TEST RANDOM 1710\Predict_org\U6_LR\IP=U6_LR-Time=22-10-17--09-06-50_498696-MAC=.jpg",
        r"E:\DATA-U6_LR_PRO\03_Images\2022-10-17\TEST RANDOM 1710\Predict_org\U6_LR\IP=U6_LR-Time=22-10-17--09-07-08_433289-MAC=.jpg",
        r"E:\DATA-U6_LR_PRO\03_Images\2022-10-17\TEST RANDOM 1710\Predict_org\U6_LR\IP=U6_LR-Time=22-10-17--09-07-21_368959-MAC=.jpg",
        r"E:\DATA-U6_LR_PRO\03_Images\2022-10-17\TEST RANDOM 1710\Predict_org\U6_LR\IP=U6_LR-Time=22-10-17--09-07-36_684015-MAC=.jpg",
        r"E:\DATA-U6_LR_PRO\03_Images\2022-10-17\TEST RANDOM 1710\Predict_org\U6_LR\IP=U6_LR-Time=22-10-17--09-07-51_644710-MAC=.jpg",
        r"E:\DATA-U6_LR_PRO\03_Images\2022-10-17\TEST RANDOM 1710\Predict_org\U6_LR\IP=U6_LR-Time=22-10-17--09-08-04_993788-MAC=.jpg",
        r"E:\DATA-U6_LR_PRO\03_Images\2022-10-17\TEST RANDOM 1710\Predict_org\U6_LR\IP=U6_LR-Time=22-10-17--09-08-47_198452-MAC=.jpg",
        r"E:\DATA-U6_LR_PRO\03_Images\2022-10-17\TEST RANDOM 1710\Predict_org\U6_LR\IP=U6_LR-Time=22-10-17--09-08-52_978926-MAC=.jpg",
        r"E:\DATA-U6_LR_PRO\03_Images\2022-10-17\TEST RANDOM 1710\Predict_org\U6_LR\IP=U6_LR-Time=22-10-17--09-08-57_961964-MAC=.jpg",
        r"E:\DATA-U6_LR_PRO\03_Images\2022-10-17\TEST RANDOM 1710\Predict_org\U6_LR\IP=U6_LR-Time=22-10-17--09-09-02_375302-MAC=.jpg",
        r"E:\DATA-U6_LR_PRO\03_Images\2022-10-17\TEST RANDOM 1710\Predict_org\U6_LR\IP=U6_LR-Time=22-10-17--09-09-09_150826-MAC=.jpg",
        r"E:\DATA-U6_LR_PRO\03_Images\2022-10-17\TEST RANDOM 1710\Predict_org\U6_LR\IP=U6_LR-Time=22-10-17--09-21-34_354530-MAC=.jpg",
        r"E:\DATA-U6_LR_PRO\03_Images\2022-10-17\TEST RANDOM 1710\Predict_org\U6_LR\IP=U6_LR-Time=22-10-17--09-22-06_616291-MAC=.jpg",
        r"E:\DATA-U6_LR_PRO\03_Images\2022-10-17\TEST RANDOM 1710\Predict_org\U6_LR\IP=U6_LR-Time=22-10-17--09-22-43_684881-MAC=.jpg",
        r"E:\DATA-U6_LR_PRO\03_Images\2022-10-17\TEST RANDOM 1710\Predict_org\U6_LR\IP=U6_LR-Time=22-10-17--09-24-16_714891-MAC=.jpg",
        r"E:\DATA-U6_LR_PRO\03_Images\2022-10-17\TEST RANDOM 1710\Predict_org\U6_LR\IP=U6_LR-Time=22-10-17--09-24-49_771723-MAC=.jpg",
        r"E:\DATA-U6_LR_PRO\03_Images\2022-10-17\TEST RANDOM 1710\Predict_org\U6_LR\IP=U6_LR-Time=22-10-17--09-26-32_147710-MAC=.jpg",
        r"E:\DATA-U6_LR_PRO\03_Images\2022-10-17\TEST RANDOM 1710\Predict_org\U6_LR\IP=U6_LR-Time=22-10-17--09-27-05_613467-MAC=.jpg",
        r"E:\DATA-U6_LR_PRO\03_Images\2022-10-17\TEST RANDOM 1710\Predict_org\U6_LR\IP=U6_LR-Time=22-10-17--09-27-38_687059-MAC=.jpg",
        r"E:\DATA-U6_LR_PRO\03_Images\2022-10-17\TEST RANDOM 1710\Predict_org\U6_LR\IP=U6_LR-Time=22-10-17--09-27-50_462515-MAC=.jpg",
        r"E:\DATA-U6_LR_PRO\03_Images\2022-10-17\TEST RANDOM 1710\Predict_org\U6_LR\IP=U6_LR-Time=22-10-17--09-27-55_602736-MAC=.jpg",
        r"E:\DATA-U6_LR_PRO\03_Images\2022-10-17\TEST RANDOM 1710\Predict_org\U6_LR\IP=U6_LR-Time=22-10-17--09-28-05_198554-MAC=.jpg",
        r"E:\DATA-U6_LR_PRO\03_Images\2022-10-17\TEST RANDOM 1710\Predict_org\U6_LR\IP=U6_LR-Time=22-10-17--09-28-14_368834-MAC=.jpg",
        r"E:\DATA-U6_LR_PRO\03_Images\2022-10-17\TEST RANDOM 1710\Predict_org\U6_LR\IP=U6_LR-Time=22-10-17--09-30-12_408311-MAC=.jpg",
        r"E:\DATA-U6_LR_PRO\03_Images\2022-10-17\TEST RANDOM 1710\Predict_org\U6_LR\IP=U6_LR-Time=22-10-17--09-30-21_003331-MAC=.jpg",
        r"E:\DATA-U6_LR_PRO\03_Images\2022-10-17\TEST RANDOM 1710\Predict_org\U6_LR\IP=U6_LR-Time=22-10-17--09-49-10_909139-MAC=.jpg",
        r"E:\DATA-U6_LR_PRO\03_Images\2022-10-17\TEST RANDOM 1710\Predict_org\U6_LR\IP=U6_LR-Time=22-10-17--09-51-01_858622-MAC=.jpg",
        r"E:\DATA-U6_LR_PRO\03_Images\2022-10-17\TEST RANDOM 1710\Predict_org\U6_LR\IP=U6_LR-Time=22-10-17--09-51-29_583659-MAC=.jpg",
        r"E:\DATA-U6_LR_PRO\03_Images\2022-10-17\TEST RANDOM 1710\Predict_org\U6_LR\IP=U6_LR-Time=22-10-17--09-51-41_518534-MAC=.jpg",
        r"E:\DATA-U6_LR_PRO\03_Images\2022-10-17\TEST RANDOM 1710\Predict_org\U6_LR\IP=U6_LR-Time=22-10-17--09-51-53_285021-MAC=.jpg",
        r"E:\DATA-U6_LR_PRO\03_Images\2022-10-17\TEST RANDOM 1710\Predict_org\U6_LR\IP=U6_LR-Time=22-10-17--09-52-03_042040-MAC=.jpg",
        r"E:\DATA-U6_LR_PRO\03_Images\2022-10-17\TEST RANDOM 1710\Predict_org\U6_LR\IP=U6_LR-Time=22-10-17--09-52-15_161536-MAC=.jpg",
        r"E:\DATA-U6_LR_PRO\03_Images\2022-10-17\TEST RANDOM 1710\Predict_org\U6_LR\IP=U6_LR-Time=22-10-17--09-52-32_919976-MAC=.jpg",
    ]
    image_paths=[
        r"D:\Code\DMS2_0\packing\packing__000004.jpg",
        r"D:\Code\DMS2_0\packing\packing__000008.jpg",
        r"D:\Code\DMS2_0\packing\packing__000012.jpg",
        r"D:\Code\DMS2_0\packing\packing__000016.jpg",
        r"D:\Code\DMS2_0\packing\packing__000020.jpg",
        r"D:\Code\DMS2_0\packing\packing__000024.jpg",
        r"D:\Code\DMS2_0\packing\packing__000028.jpg",
        r"D:\Code\DMS2_0\packing\packing__000032.jpg",
        r"D:\Code\DMS2_0\packing\packing__000036.jpg",
        r"D:\Code\DMS2_0\packing\packing__000040.jpg",
        r"D:\Code\DMS2_0\packing\packing__000044.jpg",
        r"D:\Code\DMS2_0\packing\packing__000048.jpg",
        r"D:\Code\DMS2_0\packing\packing__000052.jpg",
        r"D:\Code\DMS2_0\packing\packing__000056.jpg",
        r"D:\Code\DMS2_0\packing\packing__000060.jpg",
        r"D:\Code\DMS2_0\packing\packing__000064.jpg",
        r"D:\Code\DMS2_0\packing\packing__000068.jpg",
        r"D:\Code\DMS2_0\packing\packing__000072.jpg",
        r"D:\Code\DMS2_0\packing\packing__000076.jpg",
        r"D:\Code\DMS2_0\packing\packing__000080.jpg",
        r"D:\Code\DMS2_0\packing\packing__000084.jpg",
        r"D:\Code\DMS2_0\packing\packing__000088.jpg",
        r"D:\Code\DMS2_0\packing\packing__000092.jpg",
        r"D:\Code\DMS2_0\packing\packing__000096.jpg",
        r"D:\Code\DMS2_0\packing\packing__000100.jpg",
        r"D:\Code\DMS2_0\packing\packing__000104.jpg",
        r"D:\Code\DMS2_0\packing\packing__000108.jpg",
        r"D:\Code\DMS2_0\packing\packing__000112.jpg",
        r"D:\Code\DMS2_0\packing\packing__000116.jpg",
        r"D:\Code\DMS2_0\packing\packing__000120.jpg",
        r"D:\Code\DMS2_0\packing\packing__000124.jpg",
        r"D:\Code\DMS2_0\packing\packing__000128.jpg",
        r"D:\Code\DMS2_0\packing\packing__000132.jpg",
        r"D:\Code\DMS2_0\packing\packing__000136.jpg",
        r"D:\Code\DMS2_0\packing\packing__000140.jpg",
        r"D:\Code\DMS2_0\packing\packing__000144.jpg",
        r"D:\Code\DMS2_0\packing\packing__000148.jpg",
        r"D:\Code\DMS2_0\packing\packing__000152.jpg",
        r"D:\Code\DMS2_0\packing\packing__000156.jpg",
        r"D:\Code\DMS2_0\packing\packing__000160.jpg",
        r"D:\Code\DMS2_0\packing\packing__000164.jpg",
        r"D:\Code\DMS2_0\packing\packing__000168.jpg",
        r"D:\Code\DMS2_0\packing\packing__000172.jpg",
        r"D:\Code\DMS2_0\packing\packing__000176.jpg",
        r"D:\Code\DMS2_0\packing\packing__000180.jpg",
        r"D:\Code\DMS2_0\packing\packing__000184.jpg",
        r"D:\Code\DMS2_0\packing\packing__000188.jpg",
        r"D:\Code\DMS2_0\packing\packing__000192.jpg",
        r"D:\Code\DMS2_0\packing\packing__000196.jpg",
        r"D:\Code\DMS2_0\packing\packing__000200.jpg",
        r"D:\Code\DMS2_0\packing\packing__000204.jpg",
        r"D:\Code\DMS2_0\packing\packing__000208.jpg",
        r"D:\Code\DMS2_0\packing\packing__000212.jpg",
        r"D:\Code\DMS2_0\packing\packing__000216.jpg",
        r"D:\Code\DMS2_0\packing\packing__000220.jpg",
        r"D:\Code\DMS2_0\packing\packing__000224.jpg",
        r"D:\Code\DMS2_0\packing\packing__000228.jpg",
        r"D:\Code\DMS2_0\packing\packing__000232.jpg",
        r"D:\Code\DMS2_0\packing\packing__000236.jpg",
        r"D:\Code\DMS2_0\packing\packing__000240.jpg",
        r"D:\Code\DMS2_0\packing\packing__000244.jpg",
        r"D:\Code\DMS2_0\packing\packing__000248.jpg",
        r"D:\Code\DMS2_0\packing\packing__000252.jpg",
        r"D:\Code\DMS2_0\packing\packing__000256.jpg",
    ]
    print(len(image_paths))
    n = 1  # Số hàng
    m = 4  # Số cột
    output_path = "combined_image.jpg"
    
    PlotImages(image_paths, n, m, output_path)
