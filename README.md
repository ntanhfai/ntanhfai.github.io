# Các nội dung quan trọng

## 1. Make_Iso_folders

### Giới thiệu:

Chương trình tạo toàn bộ các folder của thư mục này thành file ISO tự động Chương trình sẽ tự download các file cần thiết về rồi sẽ tạo file create_iso.bat, chạy file bat đó để tạo file iso

Download [tại đây](https://github.com/ntanhfai/Make_Iso_folders/releases)

## Tools for Deeplearning

### Hướng dẫn chung

Các chương trình của Tuấn Anh hầu hết có thể chạy trong Command Line, lệnh help mặc định sẽ là `ntanh`, gõ trực tiếp trong CMD nó sẽ hiển thị hướng dẫn.

### ntanh:
  - ntanh là một thư viện các nhiệm vụ hàng ngày sử dụng, hay dùng nhưng không khó, mất thời gian code cho các dự án lẻ tẻ.
    -  Help: CMD: `ntanh`
    -  `ParamsBase`, dùng trong Python để lưu tham số.
    -   Image Augmentation: CMD: `ntanh_aug`
    -   Image dupplicate remover: CMD: `ntanh_img_del`
  - Hướng dẫn và cài đặt tại đây: [https://pypi.org/project/ntanh](https://pypi.org/project/ntanh)
  - Cài nhanh: `pip install ntanh`

### AI_yolo_label_checker:
  - Chương trình này để kiểm tra yolo label
  - Hướng dẫn và cài đặt tại đây: [https://pypi.org/project/AI-yolo-label-checker](https://pypi.org/project/AI-yolo-label-checker)
  - Cài nhanh: `pip install AI-yolo-label-checker`
  - Chạy chương trình: mở Command tại thư mục cần check, gõ lệnh `AI_check` hoặc `AI_yolo_label_checker`
  
### FoxLabel
  - Chương trình đánh nhãn cho Object Detection nhanh, thông minh, đa dụng. Hướng dẫn sử dụng phần mềm sẽ được in lên CMD khi chạy Foxlabel.
  - Hướng dẫn và cài đặt tại đây: [https://pypi.org/project/FoxLabel](https://pypi.org/project/FoxLabel)
  - Install:  `pip install FoxLabel`
  - Chạy chương trình: `FoxLabel` hoặc `ntanh_foxlabel`

## Tính năng
Các tools hỗ trợ tăng tốc độ và độ chính xác của dự án AI Vision: Các tools hỗ trợ tăng tốc độ và độ chính xác của dự án AI Vision:

### 1. [OK] Đánh nhãn ảnh nhanh FoxLabel

    Cách dùng [CMD]: `FoxLabel`

### 2. [OK] Augmentation ảnh

    Cách dùng: [CMD] `ntanh_aug`

### 3. [OK] Xóa ảnh giống nhau trong DB

    Cách dùng: [CMD]: `ntanh_img_del`

### 4. [OK] Thư viện ntanh

Bao gồm: 
- `tactParametters`: BaseParams dung cho lưu cấu hình
- `fnFIS`: Quét toàn bộ các file có đuôi xác định trong thư mục
- `ta_print_log`: Lưu thông tin vào log và in ra màn hình, có đầy đủ đặc tính của lệnh print.
- `get_Home_Dir`: lấy thư mục gốc của kho ứng dung để lưu cấu hình, thư mục này độc lập với thư mục code.

Cách dùng:
  
```python
from ntanh.ParamsBase import tactParametters
APP_NAME='TACT_Main'
class Parameters(tactParametters):
    def __init__(self, ModuleName="TACT"):
        super().__init__(saveParam_onlyThis_APP_NAME=False)
        self.AppName = APP_NAME
        # self.Ready_to_run = False # Nếu bắt buộc phải config thì đặt cái này = False, khi nào user chỉnh sang True thì mới cho chạy
        self.HD = {
            "Mô tả": "Chương trình này nhằm xây dựng tham số cho các chương trình khác",            
        }         
        self.load_then_save_to_yaml(file_path=f"{APP_NAME}.yml", ModuleName=ModuleName)
        # ===================================================================================================
        self.in_var=1
mParams = Parameters("TACT_Module")
  ```

4. [OK]







