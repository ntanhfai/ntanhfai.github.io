"""
Desc: resize images in a folder, keeping ratio
nt.anh.fai@gmail.com (12/9/2023 -- 11:25 AM)
"""

from PIL import Image
import os


def resize_images_in_folder(input_folder, output_folder, max_size):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for filename in os.listdir(input_folder):
        img_path = os.path.join(input_folder, filename)
        if os.path.isfile(img_path):
            img = Image.open(img_path)
            img.thumbnail((max_size, max_size), Image.LANCZOS)# .ANTIALIAS)
            
            img_name, img_ext = os.path.splitext(filename)
            output_path = os.path.join(output_folder, f"{img_name}_resized{img_ext}")
            img.save(output_path)


if __name__ == '__main__':
    input_folder = r"E:\Pictures\hoithao"  # Đường dẫn đến thư mục chứa ảnh cần resize
    output_folder = r"E:\Pictures\hoithao\output"  # Đường dẫn đến thư mục output
    maxSize = 1200  # Kích thước tối đa mong muốn
    
    resize_images_in_folder(input_folder, output_folder, maxSize)
