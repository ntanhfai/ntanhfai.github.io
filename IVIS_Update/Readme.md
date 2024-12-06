# IVIS Update

# Nguyên tắc lấy DL
- Lấy n frame: 30 OK - 30 Thừa sáng - 30 thiếu sáng
- Liệt kê tất cả các trường hợp OK:
  + Góc nghiêng (xoay), ánh sáng, tốc độ di chuyển (nếu có), độ cao của CAM, vị trí các thành phần trong bản cần lấy
  + Lấy DL cho từng TH một
  + Lấy nhiều DL ở 1 trạng thái tĩnh mà thay đổi AS
  + Nếu ảnh chuyển động không khác ảnh tĩnh nhiều, thì lấy ảnh tĩnh thay đổi ánh sáng
  
- Liệt kê các trường hợp NG:
  + Tạo NG cho các trường hợp (nhãn NG này là phải tạo ra, bịa ra, có thể có các trường hợp nào thì phải làm hết)
  + Ghi hình lại, cùng cách thức của lấy DL OK (Tĩnh đối tượng, thay đổi AS)
  + Có thể có:
    + Thêm nhãn, bớt nhãn, xoay nhãn, lật nhãn, di dịch vị trí, xoay hộp (các trường hợp không được phép => NG),...
    + 
  
- Liệt kê các trường hợp không đủ điều kiện đánh nhãn:
  + không nhìn thấy hết đối tượng, trường hợp này chưa biết là OK hay NG thì không đánh nhãn được, nhưng vẫn phải xuất hiện trong data
  
- Lấy tối thiểu trên 30 video khác nhau, trong đó số lượng OK chiếm khoảng 30%-50%, mỗi video tối thiểu 100 frames
- Trong mỗi 1 video, 30% đầu tiên là ánh sáng chuẩn, đặc biệt là những frame đầu tiên, để dễ nhìn. 
  70% còn lại là thay đổi ánh sáng (không được làm thay đổi bản chất của đối tượng: đang OK ==> NG hoặc đang NG => OK). Trong đó:
  - Thừa sáng 30% chứa tất cả các loại thừa sáng có thể xảy ra
  - Thiếu sáng 30% chứa tất cả các loại thiếu sáng có thể xảy ra

# Đánh nhãn
Khâu này sau khi có dữ liệu:
- Xác định chính xác thế nào là OK (có đánh nhãn, đủ những nhãn này => OK)
- Những trường hợp nào là NG (có đánh nhãn: có xuất hiện nhãn này => NG)
- Những trường hợp nào chưa thể quyết định (không đánh nhãn)



# Nguyên tắc set tham số:
- ROIname__quantity__DetectStep__SN__Note: 
  + Mẫu chuẩn:
    *   -1: nếu key là -1, thì bên này là gì không quan trọng, bỏ hết
    *   0: 1, step1  , false , Tản nhiệt xanh
    *   1: 2, step1  , false , Viền vàng
    *   2: 5, step1  , false , Tản hồng
    *   3: 0, step1&2, false, nếu quantity==0: bỏ qua luôn, 1 obj có thể trong nhiều step bởi dấu &

- Standard_ROIs_Position: cái này sẽ có dạng như này:
  + Standard_ROIs_Position:
      ```
      Step1: '{"1": [[6, 58, 2], [9, 89, 2], [20, 140, 2], [24, 16, 2]], "2": [[77,
        127, 2]], "3": [[35, 76, 3], [190, 52, 2]], "4": [[79, 18, 5]], "5": [[80,
        70, 6]], "ImageNotRotatable": 1, "TotalRoisDistanceErr": 20, "bottom": 373,
        "left": 250, "right": 450, "top": 222}'
      ```
  + Tạo ra bằng cách chọn Params > Standard Data Sampling. Nó sẽ tạo ROI name và Roi Pos luôn.
  + Nếu không muốn dùng ROI position thì xoá nó đi, nếu không xoá nó sẽ NG.



# Nguyên tắc cấu hình SFIS:
![](images%2FSFIS%2Fimg.png)

![](images%2FSFIS%2Fimg_1.png)

![](images%2FSFIS%2Fimg_2.png)


# What's News:

![All_Version_Statics.png](images/VesionStatis/All_Version_Statics.png)

## IVIS Ver 31.x
- First Release Date: 2024-01-13 17:00
- Thêm model `Sony_Dusty`, nhận dạng bụi bẩn trên thành IC.  
- ![Sony_Dusty_help.jpg](Data_Standard%2FSony_Dusty%2FSony_Dusty_help.jpg)
- Version31.1: MTK:
  - Bổ sung thêm function đọc QR code của Duy
- Version31.x: Tapping:
  - Fixbug: Fail reading sai do không detect được mã DTMX trong vùng Top-Bottom => nó tự xóa SN vừa đọc => sai
  - Fixbug: Cho hủy hiển thị ảnh đang predict
  - Fixbug: chỉ so sánh lỗi laserprinted khi cả 2 box not None
  - V31.33: Thêm: Menu Test Detect và QR cho Tapping.
  - V31.34: Fixbug: Ngược chip, thêm tham số NguocChip_Epsilon, để chỉnh sai số dx và dy (% sai số của khoảng cách DTMX đến cạnh của chip đó)
- 
## IVIS Ver 30.x
- First Release Date: 2024-01-11 11:00
- Thêm model `Nokia_MTK`, nhận dạng ốc vít, nút bấm, ổ cắm dây mạng và đọc QR  
- ![Nokia_MTK_help.jpg](Data_Standard%2FNokia_MTK%2FNokia_MTK_help.jpg)

## IVIS Ver 29.x
- First Release Date: 2023-11-22 16:00
- Thêm model `UI_Tan_Nhiet_PLC`, model này dùng giao tiếp COM (SFIS) để truyền thông với PLC, nhận dạng đối tượng
  - Để PLC truyền thông tin cho IVIS Process một kết quả mới, thì cần thống nhất với bên PLC là truyền `Process_Message_to_IVIS: Process` (mặc định là Process) sang cổng COM SFIS của IVIS.
  - Sau khi process xong, nó sẽ trả kết quả là xâu truyền bình thường lên SFIS. Bên PLC chỉ cần phân tích dữ liệu nhận về đó là được.
- Thêm camera Basler, phải chọn `Read_method__0direct_1class_2Basler: 2` thì mới dùng basler, trong list CAM, chọn 1 cái bất kỳ
- Tối ưu Tapping
  - Tự động nhận dạng chip ngược chiều trong `nChipFirst_No_Error: 2` (mặc định đặt =2 chip)
  - Tự động nhận dạng vị trí đọc được mã DTMX, nó sẽ đọc trong `nChipFirst_No_Error` mã, sau đó nó mở rộng vùng đọc mã ra `TopBot_limit_expand_n_times_DTMX_height: 2.3` lần chiều cao DTMX
  - Chuẩn hóa lại cái số lượng chip đã chạy, theo như danh sách hiển thị bên phải
  - Mỗi lần bấm `cancel process`, nó sẽ không tính lỗi trùng mã trong `nChipFirst_No_Error` mã. (Lúc này phải chắc chắn là đúng rồi).
- Ver 29.1:
  - Fixbug camera Basler không config được.
  - 
- Ver 29.2:
  - Fixbug `NIC|Thermal_Pad_OCR`: 
    - cũ: nếu OD chạy OK thì Total-OK sẽ bị đếm thừa 1 do cả OD, cả OCR cùng đếm.
    - Mới: Nếu OD OK thì trừ đi 1 Total-OK
  - Fixbug: loại bỏ hoàn toàn phím ENTER khi scan bằng máy sảo tay. Nếu không bấm gì sau 2" thì bấm ENTER mới có tác dụng. 
- Ver 29.3:
  - Fix bug: đọc không được ký tự sau dấu gạch dưới (thay lõi đọc easy_OCR thành PaddleOCR)
  - Đã Fix lại bug thay mới code, bỏ đi phần so sánh model bản dưới IVIS. 
- Ver 29.4, Tapping:
  - Fix lỗi liên tục báo DupplicateSN khi hết số chip cần học tập (`nChipFirst_No_Error`)
  - Fix lỗi ngược chip, chuyển về thuật toán đơn giản hơn: chỉ xét X1, đúng vùng cột đó thì không báo lỗi ngược chip
- Ver 29.5: Tapping:
  - Fixbug sau khi stop camera, bấm tiếp start camera, các thông số không được cập nhật. Bản chất là nó chưa xóa dữ liệu cũ, nên nó không hiển thị SN mới.
  - Fixbug hiển thị khi lỗi thì cả OK và NG đều tăng lên 1.
- Ver 29.8
  - model `Thermal_Pad_OCR` chỉnh sửa có thêm MAC gộp, kiểu `1234567890, 123456789012, 1231231231234,12345678`, mình phải cắt lọc ra, lấy thông tin cái nào có 12 ký tự thôi, nếu có nhiều cái có độ dài 12 ký tự thì lấy cái đầu tiên.
  - Model này thêm tham số `MAC_Min_Len: 100` là độ dài tối thiểu xâu nhập vào MAC, `MAC_Min_Len__this_model: 12` là độ dài cần trích xuất
- Ver 29.9
  - Thêm phần detect `LaserPrinted` vào `Tapping`. Mục tiêu là detect xem chữ được in trên chip có bị mất hay không.
  - Thuật toán: khi nào chip nằm giữa màn ảnh thì sẽ mang đi tính toán. 
  - Thuật toán so sánh: làm mờ ảnh, nhị phân OTSU rồi max-pooling thành 100 phần, so sánh 2 array 100 phần tử đó, sai số bao nhiêu thì tính là lỗi được cài đặt trong file config.
- Ver 29.9
    - Thêm tham số `Nmaxpool` vào `LaserPrinted` trong file config
    - 29.92: fix bug: Maxpool size
- Ver 29.10:
  - Học mất chữ chỉ học 1 chip thôi
  - Thêm 3 phương pháp binary ảnh để có thể linh động cấu hình.
  ```
  LaserPrinted:    
    Method1_C: -6,   <<== số càng nhỏ, nó sẽ trừ nhiễu càng nhiều, trừ nhiều quá thì mất nét
    Method1_block_size: 11, <<== Kích thước Block của ảnh dùng để adaptive 
    Method3_min_thresh: 70,  <<== Nếu dùng Method 3: cv2.threshold(gray1, Method3_min_thresh, 255, cv2.THRESH_BINARY) 
    Methods_binary123: 1, <<== Chọn phương án binary nào, khuyên dùng = 1
    Nmaxpool: 10,  <<== số ô cần chia để so sánh
    'comment: M1: adaptiveThreshold, M2: cv2.THRESH_BINARY + cv2.THRESH_OTSU, M3:cv2.THRESH_BINARY': 0,
    epsilon_difference_2_images_percent: 10,  <<== sai số so sánh
    epsilon_filterBoxes: 10: <<= Số lượng chip detect được ở giữa màn hình, càng nhỏ detect càng ít lần/1 chip
         
  ```
- Ver 29.11:
  - Cải thiện SFIS cho model 99
- Ver 29.12: cải thiện `Tapping`:
  - Thêm so sánh Laser printed bằng Object Detection. Dùng thêm 1 model mới, chuyên cho detect các vị trí logo, chữ.
  - Thay đổi cấu trúc so sánh box, dùng IoU xác định chính xác vị trí, không quan tâm đến tên nhãn
  - TODO: thay thế so sánh vị trí và số lượng Boxes bằng thuật toán mới tại `aiLibs/So_Sanh_Vi_Tri.py`
  - 
## IVIS Ver 28.x
- First Release Date: 2023-11-2 14:00
- Thêm `Object Detection` cho model `NIC|Thermal_Pad_OCR`: check vị trí của các ốc có đúng vị trí hay không.
- Thêm khái niệm thứ tự camera cái nào check cho loại nào (OD hay OCR), có thể thay đổi trong file config bằng tham số `cameraOder`
- v28.4: thêm chức năng: có hay không xét tính năng NG khi thừa nhãn, chỉnh qua tham số `Thua_lieu_khong_NG=False`, nếu bằng True thì không xét thừa liệu.
- Tapping:
  - Thay đổi phương thức xét ngược chip, không nhận dạng nữa, mà so sánh khoảng cách và góc quay của DTMX với tâm chip
  - Huấn luyện lại mô hình dùng 3 nhãn: 0: DTMX, 1 thiếu chip và 2 là chip.
  - Tối ưu hệ thống
  - Thêm tham số vào cho quá trình tính toán vị trí
  - Tự động nhận dạng vị trí trong 10 con chip đầu tiên (sắp xếp, bỏ 2 kích thước đầu và cuối của Distance và Angle của DTMX và Chip)
  - loại bỏ phím ENTER nếu model là Tapping.
  - 
- v28.6: 2023-11-15
  - OCR: 
    + tăng gấp 3 lần độ phân giải của ảnh gốc
    + Detect tọa độ, nới rộng tọa độ theo hướng đáy chữ 10% (chỉnh tham số), lấy vùng nới rộng này mang ra OCR, kết quả tốt hơn phương pháp cũ (để nguyên)
    + Phương pháp so sánh vị trí bằng cách xác định vùng overlap đã được áp dụng, thay cho giải pháp so sánh vị trí cố định như trước.
    + Tự động khớp vị trí có dùng thêm tham số IOU_Threshold trong level3, mặc định là 0.7
    + Nếu `cameraOrder` có 1 tham số thì tham số đó sẽ là `OCR`, và sẽ không dùng chức năng detect nữa.
    + Nếu muốn đổi thứ tự cam để OCR/Detection thì đổi số trong `cameraOrder` cho nhau.

## IVIS Ver 27.x
- First Release Date: 2023-10-25 13:00
- Thêm model `UI|UI_Bubble`: Check có hay không các đối tượng (tản nhiệt, anten) ở 2 mặt của 1 tấm bạch in gá đứng
- Cách dùng:
  - Chọn 2 CAMERA
  - Vẽ ROI 1 và 2 (1 cho mặt 1, 2 cho mặt 2)
  - Xoay ảnh sao cho nó giống ảnh mẫu.
  - 

## IVIS Ver 26.x
- First Release Date: 2023-10-23 18:00
- Thêm model `NIC|Thermal_Pad_OCR`: Kiểm tra chữ in trên tấm tản nhiệt có đúng không, model đó có phải dùng loại tản nhiệt này không.
    - Cách chạy:
      - Nhập MAC vào, model sẽ đọc OCR text, sau đó lấy list của text đó (trong config), nếu có chứa MAC thì OK, không thì NG
    - Thêm roi 0 vào model, model sẽ đoán dựa theo ROI 0.
- Fixed bug chỉnh góc quay của các camera, có thể lưu góc quay cho từng camera hoặc tất cả các cam đang được chọn.
- Thêm mỗi lần chọn một camera thì nó sẽ hiện góc quay đang chạy lên đó.
## IVIS Ver 25.x
- First Release Date: 2023-10-20 11:00
- Thêm model `UBEE|UBEE_TrayOBA`: Kiểm tra ngược module chip, vỏ hộp 
- Sửa lại khung màu, nếu nhãn là lẻ thì hiển thị màu xanh, chẵn thì màu đỏ. vì vậy từ nay nhãn sẽ quy ước là Lẻ là OK, chẵn là NG của nó
- 
## IVIS Ver 24.x
- First Release Date: 2023-10-16 4:50
- Thêm model `All_CFTs|VIIE_2023`: Kiểm tra thiếu ốc và thanh gá của card quang
- Tham số mặc định:

```
VIIE = {
            'Input_images_dir': 'c:/VIIE/images_to_AI',
            'Output_images_dir': 'c:/VIIE/output_from_AI',
            'Input_phase_lock_filename': 'lock.txt',
            'Output_phase_lock_filename': 'lock.txt',
            'remove_imput_image_after_read': True,
        }
```

* Đặc điểm:
  * Proj này không có camera, mà đọc ảnh từ folder, do bên AT gửi sang.
  * Folder mặc định AT=>AI: gọi là `Input_images_dir`, mặc định: `c:/VIIE/images_to_AI`, có thể thay đổi nếu muốn
  * Folder mặc định AI=>AT: gọi là `Output_images_dir`, mặc định: `c:/VIIE/output_from_AI`, có thể thay đổi nếu muốn
  * `Input_phase_lock_filename` là tên file khóa, khi IVIS thấy có file này thì sẽ không đọc data trong thư mục đó
  * `Output_phase_lock_filename` khi AT thấy file này thì đừng có đọc data vội, vì đang ghi dở.
- Phương thức giao tiếp của folder: 
  * Thư mục ghi data của AT: `Input_images_dir`:
    - AT đọc ảnh từ CAM 
    - AT tạo file `Input_phase_lock_filename` (chính là `lock.txt` )
    - AT Lưu ảnh 
    - AT Xóa file `Input_phase_lock_filename` (chính là `lock.txt` ): kết thúc quá trình gửi ảnh
  * IVIS trả kết quả: ở thư mục `Output_images_dir`:
    - IVIS tạo file `Output_phase_lock_filename` (chính là `lock.txt` )
    - IVIS Lưu ảnh: `predicted_image.jpg`
    - IVIS lưu file kết quả vào file `predicted_result.yaml`, file này là 1 file text, có cấu trúc của yaml kết quả ở dạng (key:value)
    - IVIS Xóa file `Output_phase_lock_filename` (chính là `lock.txt`): kết thúc quá trình trả kết quả
  * AT đọc kết quả xong thì xóa hết file ở thư mục `Output_images_dir` đi
  * AI đọc ảnh đầu vào xong cũng xóa hết file ở thư mục `Input_images_dir` đi để chờ ảnh mới.
  
  
## IVIS Ver 23.x
- First Release Date: 2023-10-11 4:20
- Thêm model `Solder_Checking`: kiểm tra thừa thiếu thiếc trong linh kiện mạch in
- 
## IVIS Ver 22.x
- First Release Date: 2023-09-12 11:11
- Thêm model Nokia|Tapping
  - Tích hợp code vào IVIS.
  - Xử lý xung đột Port đã mở từ IVIS và Tapping
  - Nâng cấp giao diện để phù hợp với việc chạy thêm Tapping Model 
  - Xử lý tuần tự nút bấm: cho phép bấm nút StartCamera trước, xong rồi mới dc bấm các nút khác
  - Xử lý sai khác database
  - Xử lý sai khác tổng số dữ liệu đã chạy
  - Có rất nhiều các tính năng dành riêng cho Tapping:
    - ### Tracking:
      - Ban đầu chưa có gì
      - Khi nhận được mDict (trạng thái predict của frame đang xly)
      - Nếu đã có mã DTMX, thì loại bỏ ảnh ROI DTMX => cập nhật mã DTMX vào 1 danh sách (có thể là imROIs)
      - Nếu chưa có mã DTMX: giữ lại => pha sau sẽ đọc DTMX của ảnh này
      - Đọc xong cập nhật lại mDict
    - ### Giao thức truyền nhận với SFIS:
      1. Format xác nhận yêu cầu gửi lên IT :
          - AI - IT :  "V1013922{Spaces:7}EMPEND"
              + V1013922 : Là mã thẻ của người phát triển chương trình. Theo yêu cầu của IT thì nếu thay đổi mã thẻ trên thì phải gửi yêu cầu cho IT để họ xác nhận.
          - IT - AI : Chuỗi AI gửi lên kèm theo "PASS" or "ERRO"
          - Format này theo yêu cầu của IT . Hiện tại trước khi đóng 1 tray hàng thì cần gửi chuỗi này lên để IT xác nhận.
      2. Format gửi giá trị SN (mã Dtmx):
          - AI - IT : "{TRAY:12}{Spaces:3}{SN:15}TRAYMACEND\r\n"
              + TRAY : Đây là mã của 1 Tray. 1 Tray sẽ bao gồm các con hàng cần đóng.
              + SN : Đây là mã SN của 1 con hàng.
          - IT - AI : chuỗi AI gửi lên kèm theo "PASS" or "ERRO"
          - VD :
              + AI - IT : 111111111111 355649260042150TRAYMACEND
              + IT - AI : 111111111111 355649260042150PASS
      3. Format reset tray:
          - AI - IT : "{TRAY:12}{Spaces:3}RESETTRAYEND\r\n"
          - IT - AI : Chuỗi AI gửi lên kèm theo "PASS" or "ERRO"
          - Bắt đầu đóng 1 Tray mới
          - Chức năng này dùng để reset lại 1 tray trong trường hợp đang đóng dở 1 tray mà muốn đóng lại từ đầu.
          - Lấy thông tin Tray lần đầu chạy, hoặc làm lại Tray đó từ đầu:
            - AI => IT: `"{TRAY:12}{Spaces:3}RESETTRAYEND\r\n"`
            - IT => AI: `"{TRAY:12}{Spaces:3}RESETTRAYEND##ModelName#Quantity#PASS\r\n"`
            - Ví dụ:
              - AI => IT: `"TrayMAC12345          RESETTRAYEND\r\n" `    
              - IT = >AI: `"TrayMAC12345          RESETTRAYEND#ModelName#Quantity#PASS\r\n"  // ModelName, Quantity & PASS`
    - ### Giao thức giao tiếp với Hardware:
      - `{cnt}` là biến đếm số có thể lên đến 10 chữ số và dấu trừ, ví dụ: loại `DDMM-HHMMSS`, dữ liệu gửi đi `0825-102531`, tăng dần, cái này không quan trọng, chỉ cần kiểm tra có xâu sau nó trong truyền thông thì thực hiện lệnh.
          - Ưu điểm của cách này, là khi lưu log, sẽ biết chính xác thời gian gửi lệnh nào đi.
      - `RUN.\n`: chạy chuyền
      - `STOP.\n`: dừng chuyền
      - `LAMP:XYZT.\n`: thay đổi trạng thái 4 đèn X, Y, Z, T = 0/1: 0: tắt đèn, 1: bật đèn. Ví dụ khi format xâu:  `LAMP:0110.\n`, khi Hardware nhận được: `LAMP:0110.\n`
      - `WDT:N.\n`: Thời gian max = N, Khi biến `wdt_cnt>=N` thì tự động dừng chuyền. Ví dụ: `WDT:135.\n`
      - `CLEAR_WDT.\n`: Xóa bộ đếm tăng wdt_cnt: `wdt_cnt=0`. Ví dụ: `CLEAR_WDT.\n`
      - `NG.\n`: Có lỗi xảy ra, báo còi đèn. Ví dụ: `NG.\n`
      - `OK.\n`: đã xử lý xong lỗi, tắt còi đèn đi. Ví dụ: `OK.\n`
  - Cải thiện tốc độ xử lý của mô hình:
    - Chuyển mô hình về ảnh 320x320, tốc độ tăng từ 12FPS lên 20FPS (có thêm delay 10ms trong vòng loop)
    - Giảm số % CPU sử dụng từ 100% xuống còn 30%
  - Thay đổi phương pháp đọc mã DTMX:
    - Thêm các tham số đọc mã thành tham số config:
    - dtmxSetings:
      - DTMX_debug: true    # Bật chế độ lưu ảnh DTMX,  boxRectArea trước và sau khi decode + tracking
      - resize_to_percent0_1: 1.0  # Resize ảnh DTMX, nếu cần thì thay đổi
      - threshold: 50  # Tham số của hàm đọc DTMX
      - timeout_ms: 150 # Tham số của hàm đọc DTMX
    - Thay đổi giá trị mặc định của đọc mã DTMX: timeout từ 100 lên 150,  
  - Thêm chức năng:
    - Hiển thị form thứ 2 lên trên form 1, từ 1 hàm trong form1 gọi form 2: `app = VideoPlayer.VideoPlayer(self.parent)`
    - Thêm tính năng cho phần đọc DTMX:
      - `DTMX_Code_Length`: Đọc DTMX đúng độ dài quy định mới chấp nhận giá trị, mặc định là 15. Xếp cái này trong `This_time_Running_cfg`.
      - Thêm tham số: `Convert_img_to_gray` để kỹ sư có thể cấu hình cho phép chuyển sang ảnh xám trước khi đọc DTMX hay không
      - `DTMX_debug`: cho phép in ra các tham số liên quan đến DTMX (ảnh, tham số boxRecArea in vào log)
      - `Expand_DTMX_Area_Percent`: cho phép mở rộng vùng DTMX, tránh bị mất vùng trắng, lẹm vào DTMX
      - `resize_to_percent0_1`: resize ảnh DTMX cần đọc 
      - `timeout_ms`: set thời gian tối đa cho đọc mã DTMX
      - `threshold`: Ngưỡng theo ý nghĩa của hàm.
    - Thêm tham số `dupplicate_ignore_n_frames_passed_from_New_label`: là số nguyên, sau mỗi lần detect new label, 
      `n_frames_passed=0`, mỗi lần detect new label ảnh mới, `n_frames_passed++`, nếu `n_frames_passed >= dupplicate_ignore_n_frames_passed_from_New_label` thì mới bắt đầu tính dupplicate SN. 
       Việc này để tránh hiện tượng vừa predict được ảnh mới, 1 lúc sau nó lại lặp lại chính ảnh đó thành SN mới do máy tính yếu, 
       không Tracking được. Giá trị này không được để quá lớn, chỉ cần = số lượng frame 1 DTMX chạy trên FOV của Cam là đẹp. 
       Mặc định =-1 để luôn luôn bắt lỗi dupplicate.   
    - 
  - Fixbugs:
    - không đọc được DTMX, bị lỗi ảnh dtmx dẫn đến die chương trình.
    - 
  - Tapping Help:
  ![img.png](images/help_imgs/img_1.png)

  - Tapping:
    - Thêm chức năng Chỉ đọc mã SN trong vùng màu vàng
    - Thêm: handle_wrong_material: Tự động học mã DTMX di chuyển theo 1 đường thẳng nhất định (mở rộng vùng ra 10%), học từ chíp 2 đến chíp 10, từ đó về sau DTMX sẽ chỉ được chạy trong dải đó thôi, ngoài dải là lỗi `ngược chip`, vùng này sẽ dc xóa khi nhập mới, mã tray (reel)
    - todo: Chỉ detect Yolo trong cột vùng màu vàng

 
## IVIS Ver 21.x
- First Release Date: 2023-09-06 11:11
- Thêm model UI|UI_UVCG5
  -  UI_UVCG5 là model check nhiều nhãn khác nhau, xem hình sau:
  - ![UI_UVCG5.png](images/Versions-Results/UI_UVCG5.png)
- Fix bugs:
  - Tự động nhận dạng tên key và số lượng keys (trước chỉ nhận dạng tên và số lượng = 1)
- Thêm tham số `UsingPositionChecking: false`, mặc định sẽ không dùng check vị trí, nếu `UsingPositionChecking: true` thì mới kiểm tra vị trí.
- 
## IVIS Ver 20.x
- First Release Date: 2023-08-09 14:00
- Thêm tham số lưu độ phân giải ảnh: `SaveImageSizeWH: 460,460`, nếu chỉ nhập 1 thì lỗi, nếu nhập nhỏ quá thì nó tự lên 360x360
- Thêm tham số lưu tên ảnh: `SaveImage_FilenameTimestamp: %y-%m-%d--%H-%M-%S-%f` tham số này sẽ quyết định là ảnh sẽ lưu như nào, nếu bỏ chữ `%f` đi thì sẽ trùng tên theo giây, tức là mỗi giây lưu một lần
- Fixbug: đã fix bug delay khi hiển thị
- Thêm: File mẫu báo cáo test chương trình, để trong `IVIS_data/Resources/Test_Report_Standard.xlsx`

- Thêm model Nokia_TraySIM:
    + Train model
    + Dùng tham số mặc định cho nhận dạng đối tượng (Y8)
- Autolink:
    + Fixbug: Tách biệt SFIS NG và Timeout
    + Fixbug: xoá danh sách hàng đợi nhận tin từ máy SCAN khi nhận đủ 2 mã MAC và SN (Nếu bản chưa vào đủ trong vùng đầu đọc, hàng đợi chỉ đọc dc 1 mã, danh sách này sẽ lưu lại hết đến khi đọc dc hai mã trong các lần đọc khác nhau thì xoá bộ nhớ đệm)
    + Fixbug: Thay đổi thuật nhận diện mã, thay vì nhận diện bằng toạ độ tương đối giữa các mã, thì bây giờ nhận diện mã bằng nội dung cuối của mã đó.
    + Fixbug: khi kết luận timeout thì cũng xoá bộ nhớ đệm lưu trữ danh sách mã.
    + Fixbug: Gửi tín hiệu đi nhiều lần 1 bản (lỗi này phát sinh từ v19.x)
    + Fixbug: Danh sách hàng đã gửi chỉ được tăng thêm nếu mã là OK, nghĩa là sau khi đọc mã xong, gửi lên SFIS, SFIS báo OK thì mới cập nhật vào danh sách chống trùng lặp bản, điều này cho phép công nhân sửa sai nếu máy không đọc được.
    + IVIS_V20.2, AutoLink_V2.1: release date 2023-08-11 14:50
        * Fixbugs lớn, thay đổi cấu trúc chương trình, loại bỏ lỗi nhận data và giải mã ra  sCM_MAC, sMAC_PCB
        * Thay đổi tư duy timeout, timein, loại bỏ tình trạng đọc được 1 mã xong không nhận tiếp được dữ liệu nữa.
        * Chuẩn hoá lại cái time out
        * Fix lại bug in lên ảnh mã nào thiếu nếu NG thông qua nhiều lần nhận dữ liệu khác nhau
        * In thêm thông tin version và datetime lên ảnh để dễ check log.
- UBEE911:
    + Fixbug: chuyển đổi thông tin gọi hàm bằng class, nhằm fix lỗi dùng proj này nhưng vẫn load proj khác
    + Thay đổi thông tin lưu ảnh bằng cách chỉnh thời gian trên file lưu, nếu trùng tên nó sẽ thôi không lưu nữa.
- Train mới data cho UI6W:
    + Data: (Kỹ sư mới)
        * Lấy thêm data mới
        * Đánh nhãn cho data mới, 
        * Đánh nhãn lại cho data cũ
    + Kiểm tra tính đúng đắn của data
    + Train mới mô hình với YoloV5 (Chạy trên IVIS v9.x)
- Todo:
    + Thêm License khi thêm mới mỗi model

2023-08-12 08:39:
- Trained model `Y8n_Nokia_TraySIM_V20.2.onnx` 
- Collect more data for UBEE911:
    + Nguyên nhân: trong quá trình test 140 bản, có 2 trường hợp FP
    + Thêm: vị trí 




## IVIS Version 20.x - Scientifically Explained Dev Log

**Release Information:**
- Initial Release Date: 2023-08-09 at 14:00

**Enhancements:**

1. **Image Resolution Parameter:**
   - Added a parameter to save image resolution: `SaveImageSizeWH: 460,460`.
   - If only one value is entered, an error occurs.
   - If dimensions are too small, they are automatically adjusted to 360x360.

2. **Image Naming Parameter:**
   - Added a parameter for image naming: `SaveImage_FilenameTimestamp: %y-%m-%d--%H-%M-%S-%f`.
   - This parameter determines how images are saved.
   - Removing `%f` ensures second-based unique naming, saving once per second.

3. **Bug Fixes:**
   - Resolved bug causing display delays.

4. **Test Report Template:**
   - Included a sample program test report file at `IVIS_data/Resources/Test_Report_Standard.xlsx`.

5. **Nokia_TraySIM Model:**
   - Introduced the Nokia_TraySIM model.
     - Trained the model.
     - Utilized default parameters for object recognition (Y8).

6. **Autolink Module:**
   - Bug Fixes:
     - Separated SFIS NG (Not Good) from Timeout cases.
     - Cleared queue of received messages from SCAN machine after obtaining 2 MAC and SN codes.
     - Changed code recognition method to focus on code content rather than relative coordinates.
     - Cleared memory storing code list upon timeout conclusion.
     - Resolved issue of sending signals multiple times (a bug carried over from v19.x).
     - Queue for sent items updated only for OK codes, enabling corrections if codes couldn't be read.
     - IVIS_V20.2, AutoLink_V2.1 released on 2023-08-11 at 14:50.
       - Major bug fixes and structural changes.
       - Eliminated errors in data reception and decoding into sCM_MAC, sMAC_PCB.
       - Rethought timeout logic, eliminating situations where data reception halts after reading one code.
       - Standardized timeout settings.
       - Fixed bug causing missing code images in case of multiple data receptions.
       - Added version and datetime info to images for easier log checking.

7. **UBEE911 Module:**
   - Bug Fixes:
     - Implemented class-based function calls to prevent unintended loading of other projects.
     - Altered image storage method by using file timestamp; avoids saving if names match.

8. **UI6W Data Training:**
   - Data Preparation (New Engineer):
     - Collected new data.
     - Labeled new data.
     - Re-labeled existing data.
   - Data Integrity Check.
   - Trained model using YoloV5 (Executed on IVIS v9.x).

**To-Do:**
- Include Licensing Process for Each New Model.

 
## IVIS Ver 19.x
- First Release Date: 2023-08-04 10:20
- Thêm một predict quan trọng: Predict Cho tất cả các Thêm model đơn thuần, gọi là `Detector`
    + `Detector`: có `Predict_Type_0123_n: 99`
    + Các tính năng khác đủ cho tất cả các trường hợp predict model chung.

- Fixbug: Thay đổi thuật toán delay khi OK/NG, thay vì dùng biến và trực tiếp so sánh thời gian thì bây giờ dùng một class riêng, chuyên để xử lý việc `timein` và `timeout`
- Fixbug: Thay đổi phương pháp xử lý hiển thị lết luận mỗi lần xử lý xong, thay vì lần nào xử lý xong cũng hiển thị, thì bây giờ chỉ xử lý hiển thị khi nào kết quả báo `OK/NG`, hoặc `OK_Stepx`
- Fixbug: chuyển việc hiển thị status về cuối tiến trình chính, nhằm mục đích dễ theo dõi toàn bộ quá trình cập nhật hệ thống, dễ debug hơn, bên cạnh đó, cũng đã loại bỏ dấu xuống dòng trong hiển thị thanh status.
- Fixbug: xử lý lại phần `SFIS_Connection_timeouted`, cho phép trả lại kết quả theo lời gọi hàm chứ không dùng biến toàn cục, giảm bộ nhớ khi chạy các dự án khác.

- Nokia_Telit: Train a dev model using YoloV8 small for the first time
- Nokia_Telit: Code a draft version of the project, only have class and funcs structures
- Nokia_Telit: Documentation

- Thêm Model: Train model Nokia_TraySIM

- TrainYolo_V8: Thêm: Tự động tạo data validation, cái này sẽ tự tạo 10% ảnh cho val.
- TrainYolo_V8: Thêm: Tự động tạo file dataset khi train
- TrainYolo_V8: Thêm: Lưu trữ file dataset mỗi lần train (trong vòng 1 phút thì ghi đè) vào một thư mục chung, để sau này tiện tra cứu lại đã train cái gì
- TrainYolo_V8: Thêm: Tự động resize ảnh đầu vào thành cao 640, vì đằng nào cũng phải resize ảnh về 640x640. nên trong quá trình lấy data, nên resize về gần kích thước này nhất để giảm không gian lưu trữ. Có thể resize cứng trên camera hoặc resize mềm trên cấu hình. Việc này không làm thay đổi chất lượng file weight đầu ra.
- TrainYolo_V8: Thêm: có thể cấu hình tham số trích xuất ảnh là ghi đè hay ghi bổ sung thông qua tham số trước khi train model.
- TrainYolo_V8: Thêm: Từ nay có thể cấu hình train data chỉ có tập train (tự trích val) hoặc cả train cả val

- AutoLink: 
    + Thêm cổng COM để điều khiển còi khi NG. Thông tin cổng COM và dữ liệu gửi đi sẽ config qua tham số.
    + Nếu nhận được data: xử lý
    + Nếu nhận dc 2 mã đều khác rỗng, reset timer, nếu đã xử lý rồi: bỏ qua; nếu chưa xử lý thì gửi lên SFIS bình thường
    + nếu chỉ nhận được 1 mã: 
        * Thêm tham số: `sData_Process_NG_if_read_not_enough_2code: true` nếu `=False` thì bỏ qua nếu chỉ đọc được 1 mã.
        * Thêm tham số timeout (`sData_need_full_2code_timeout_in_seconds: 3.0`):
            - Nếu lần đầu nhận được 1 mã thì khởi tạo bộ timeout, nếu là lần sau nhận được mã thì kiểm tra xem timeout chưa.
            - nếu đã timeout: báo NG
    + Thêm phần hiển thị thông tin kết luận của mỗi lần predict lên ảnh.
    + Thay đổi phần lưu trữ dữ liệu, lưu vào database các trường cần thiết.

- UBEE911:
    + Thêm class timeout cho dự án để giới hạn thời gian 
    + Thêm tính năng giới hạn thời gian predict nếu đã phát hiện OK, thuật toán:
        * Cho chạy lần đầu tiên `self.NeedFirst_Run=True`
        * Chạy đến khi có kết quả OK thì coi như chạy xong lần đầu tiên => Huỷ chạy lần đầu: `self.NeedFirst_Run=False`, khởi động timer OK để chờ
        * Vẫn chưa xong phần này!

- Todo:
  - Thêm tham số để tránh việc lưu quá nhiều ảnh / 1 con hàng (hàng của UBEE911)
    - Nếu hàng không có SN:
      - dùng tracking 
      - dùng vùng ROI
    - Nếu hàng có SN:
      - Chỉ xly khi SN chưa được xử lý
  - Thêm License khi thêm mới mỗi model
  - Fixbug TimeoutHandler, gắn vào UBEE911
 
### IVIS Ver 19.x Statistics
- First Release Date: 2023-08-04 10:20

**Features Added:**
- Introduced a significant prediction feature: Predict for all standalone models, referred to as `Detector`.
    + `Detector`: Contains `Predict_Type_0123_n: 99`.
    + Other necessary functionalities for unified model prediction.

- Fixed a bug: Changed the delay algorithm for OK/NG determination by implementing a separate class for handling `timein` and `timeout` processes.
- Fixed a bug: Altered the method of displaying conclusions after each processing round, now showing only when results are `OK/NG` or `OK_Stepx`.
- Fixed a bug: Reorganized status display towards the end of the main process for improved tracking, debugging, and eliminated unnecessary line breaks in the status bar.
- Fixed a bug: Reworked `SFIS_Connection_timeouted` part, allowing result return through function calls rather than using global variables, saving memory in various project runs.

**Tasks Accomplished:**
- Nokia_Telit: Trained a developmental model using YoloV8 small for the first time.
- Nokia_Telit: Coded a preliminary version of the project, focusing on class and function structures.
- Nokia_Telit: Documentation.

**Added:**
- Train model Nokia_TraySIM.

- TrainYolo_V8: Added automatic validation data creation, generating 10% of images for validation.
- TrainYolo_V8: Introduced automatic dataset file creation during training.
- TrainYolo_V8: Included dataset file storage after each training iteration (overwriting within 1 minute) in a common directory for future reference.
- TrainYolo_V8: Enabled automatic resizing of input images to a height of 640 pixels, aligning with the requirement of 640x640 dimensions. This saves storage space during data collection.
- TrainYolo_V8: Added parameter for configurable image extraction method, either overwrite or append, before model training.
- TrainYolo_V8: Provided the option to configure training data to only contain the training set (automatic validation extraction) or both training and validation data.

- AutoLink:
    + Added COM port for controlling a horn when an `NG` occurs. COM port information and sent data will be configured through parameters.
    + If data is received, process it.
    + If two different non-empty codes are received, reset the timer. If already processed, skip; if not yet processed, send to SFIS as usual.
    + If only one code is received:
        * Added parameter: `sData_Process_NG_if_read_not_enough_2code: true`. If `=False`, skip processing if only one code is read.
        * Added timeout parameter (`sData_need_full_2code_timeout_in_seconds: 3.0`):
            - If first time receiving one code, initialize a timeout mechanism. If received again, check if timeout has occurred.
            - If timeout has occurred: flag as `NG`.
    + Added part to display conclusion information of each prediction on images.
    + Changed data storage method, saving necessary fields into a database.

- UBEE911:
    + Added a timeout class for the project to manage time constraints.
    + Implemented a feature to limit prediction time once `OK` is detected. Algorithm:
        * Run with `self.NeedFirst_Run=True`.
        * Continue until `OK` result is achieved, considering the first run complete. Set `self.NeedFirst_Run=False`, initiate a timer for the `OK` phase.
        * This part is still in progress.

**To-Do:**
- Add parameters to prevent excessive image saving per item (item of UBEE911).
    - If the item has no serial number:
      - Use tracking.
      - Use ROI area.
    - If the item has a serial number:
      - Process only when the serial number is not yet processed.
- Include License addition when adding new models.
- Fixbug TimeoutHandler and integrate it into UBEE911.

## IVIS Ver 18.x
- Release date: 2023-07-28 5PM
- Thêm model UBEE911: predict nhãn trong hộp trôi trên chuyền
- Thêm: Thay đổi lớn nhất của Version này là chuyển sang predict bằng ONNXRuntime, thay cho DNN của OpenCV, điều này làm cho tốc độ xử lý nhanh hơn đáng kể (từ 0.6s xuống còn 0.2s). Nếu dùng Yolo trực tiếp (đã hỗ trợ, tuy nhiên chưa dùng vì đóng gói quá nặng) thì thời gian giảm còn 0.1s
- Tối ưu hoá code, giảm thiểu triệt để các tác vụ lưu file trung gian để tăng tốc độ xử lý
- Loại bỏ các đoạn code không thực sự cần thiết, hoặc chuyển nó vào vùng hoạt động có điều kiện để tăng tốc độ xử lý chung.
- Chuyển cấu trúc code từ file, functions sang thành class để tăng khả năng linh hoạt và lưu trữ dữ liệu của biến cục bộ, giảm sử dụng biến toàn cục
- Chuyển đổi cấu trúc Predict chương trình để tác vụ predict sẽ trở thành tác vụ dễ hiểu, đơn giản hơn trong quá trình triển khai dự án mới
- Thêm: __StillPredict_WhenPreviewing__, tính năng predict trong quá trình Preview, cũ không có, cũ là đã preview thì thôi không predict mới
- Thêm: tính năng resize ảnh mềm, nghĩa là ảnh từ camera có độ phân giải gốc (cái này có thể thay đổi được), ảnh xử lý sẽ resize sang kích thước khác, tất cả đều cấu hình được bằng tham số, điều này làm tăng tốc độ xử lý mà vẫn giữ được khung hình rộng của ảnh
- Thêm: Phân biệt nhiều step ở ROIname__quantity__DetectStep__SN__Note rõ ràng, điều này sẽ giúp cho việc tự động nhận dạng mẫu được đơn giản hơn.
- Fixbug: thêm Total_Product_OK, Total_Product_NG vào Predict ở Yolov8
- Thay đổi thông tin bản quyền, thông tin bản quyền sẽ được cấp từ bộ phận AI, tính cho mỗi phần cứng, chứ không phải bằng Password như trước nữa, nhằm tránh tình trạng copy phần mềm trái trép.
- Cập nhật: http://aisolutions.vn/fai/
- Cập nhật: http://aisolutions.vn/fai/ivis/index.php: thêm thông tin tên trạm, tên dự án
- Thêm file logs khi tạo keys: http://aisolutions.vn/fai/ivis/logs.html
- Thêm module chuyển đổi Markdown sang HTML giữ nguyên được hình ảnh, có định dạng bootstrap
- Thêm tính năng hiển thị Help>SOP
- Thêm chức năng in ra ảnh đồ thị các thông tin liên quan đến số lượng update/bugs_fixed. 
- Fix bugs: Thu thập lại data, đánh lại nhãn toàn bộ lần thứ 3 cho dự án UBEE911, lý do: bên khách hàng yêu cầu có thêm trạng thái NG của bản khi hàng chạy qua chuyền.
- Todo: thêm chức năng cảnh báo bằng đèn, còi khi có tín hiệu NG.


### IVIS V18 Chi tiết
- Thêm model UBEE911: predict nhãn trong hộp trôi trên chuyền:
	- Tạo model UBEE911 sử dụng mô hình AI object detection như YOLOv3, SSD, Faster R-CNN hoặc RetinaNet.
	- Tích hợp model UBEE911 vào phần mềm để sử dụng dự đoán (predict) trên ảnh đầu vào.
	- Đảm bảo khả năng chạy nhanh và ổn định của model UBEE911 trên nền tảng Python và Tkinter.
- Thêm tính năng predict bằng ONNXRuntime thay thế DNN của OpenCV:
	- Chuyển đổi model UBEE911 thành định dạng ONNX để sử dụng trên ONNXRuntime.
	- Tích hợp ONNXRuntime vào phần mềm để thực hiện predict thay cho DNN của OpenCV.
	- Kiểm tra tính chính xác và độ ổn định của predict bằng ONNXRuntime so với DNN của OpenCV.
- Tối ưu hoá code và giảm thiểu triệt để tác vụ lưu file trung gian:
	- Điều chỉnh cấu trúc mã nguồn để giảm số lần lưu file trung gian và giải phóng tài nguyên lưu trữ.
	- Sử dụng các phương pháp lưu trữ dữ liệu tạm thời trong bộ nhớ RAM để tăng tốc độ xử lý.
- Loại bỏ các đoạn code không thực sự cần thiết, hoặc chuyển nó vào vùng hoạt động có điều kiện:
	- Kiểm tra mã nguồn và xác định các đoạn code không liên quan hoặc không cần thiết trong tác vụ predict.
	- Tối ưu cấu trúc mã nguồn để giảm thiểu việc thực thi các đoạn code không cần thiết.
- Chuyển cấu trúc code từ file, functions sang thành class:
	- Tạo các class mới để quản lý các thành phần và tính năng riêng biệt của phần mềm.
	- Thực hiện việc chuyển đổi cấu trúc mã nguồn từ functions sang class để tăng tính linh hoạt và sử dụng biến cục bộ.
- Chuyển đổi cấu trúc Predict chương trình để tác vụ predict dễ hiểu, đơn giản hơn:
	- Tối ưu cấu trúc Predict để đảm bảo tính dễ hiểu và tối giản các tác vụ predict.
	- Cung cấp giao diện đơn giản và dễ sử dụng cho việc predict trên các ảnh đầu vào.
- Thêm tính năng predict trong quá trình Preview:
	- Xây dựng tính năng StillPredict_WhenPreviewing để thực hiện predict ngay khi đang xem trước ảnh.
	- Đảm bảo tính năng này không ảnh hưởng đến quá trình Preview và tăng tính tương tác của người dùng.
- Thêm tính năng resize ảnh mềm:
	- Định nghĩa các tham số cấu hình cho việc resize ảnh mềm trong quá trình predict.
	- Thực hiện việc resize ảnh mềm để tăng tốc độ xử lý mà vẫn giữ được khung hình rộng của ảnh.
- Thêm tính năng phân biệt nhiều step ở ROIname__quantity__DetectStep__SN__Note:
	- Mở rộng cấu trúc dữ liệu và giao diện để hỗ trợ thông tin về nhiều step trong quá trình predict.
	- Xử lý dữ liệu và hiển thị thông tin phân biệt step để đơn giản hóa việc nhận dạng mẫu.
- Fixbug: thêm Total_Product_OK, Total_Product_NG vào Predict ở Yolov8:
	- Điều chỉnh mã nguồn của Yolov8 để thêm tính năng Total_Product_OK và Total_Product_NG trong quá trình predict.
	- Xác định và sửa lỗi liên quan đến việc thêm thông tin Total_Product_OK và Total_Product_NG.
- Thay đổi thông tin bản quyền:
	- Thêm tính năng cấp thông tin bản quyền từ bộ phận AI và tích hợp thông tin này vào phần mềm.
	- Điều chỉnh cấu trúc giao diện để hiển thị thông tin bản quyền cho người dùng.
- Cập nhật: http://aisolutions.vn/fai/
- Cập nhật: http://aisolutions.vn/fai/ivis/index.php: thêm thông tin tên trạm, tên dự án
- Thêm file logs khi tạo keys: http://aisolutions.vn/fai/ivis/logs.html
- Thêm module chuyển đổi Markdown sang HTML giữ nguyên được hình ảnh, có định dạng bootstrap
- Thêm tính năng hiển thị Help>SOP
- Thêm chức năng in ra ảnh đồ thị các thông tin liên quan đến số lượng update/bugs_fixed. 
- Fix bugs: Thu thập lại data, đánh lại nhãn toàn bộ lần thứ 3 cho dự án UBEE911, lý do: bên khách hàng yêu cầu có thêm trạng thái NG của bản khi hàng chạy qua chuyền.
- Todo: thêm chức năng cảnh báo bằng đèn, còi khi có tín hiệu NG.

## IVIS Ver 17.x
- Update: V17.0 2023-07-20 19:21
- Thêm Model Nokia_TanNhiet
  + Thêm tính năng gộp các ảnh của nhiều Cams vào 1 để predict, đề phòng trường hợp nhiều cam cùng detect obj, cái này cấu hình bởi tham số: `Combine_all_images_to_predict_if_more_than_1_Camera` trong level3, mặc định là False
- Thêm chức năng: nếu chế độ menu Params > *"Standard Data Sampling"* được chọn, check đối tượng + vị trí của các đối tượng đó
- Thêm chức năng Tự động gán vị trí đối tượng chuẩn, ví dụ:
  + '{"1": \[\[15, 52, 2], \[27, 135, 2], \[29, 15, 2]], "2":
      \[\[10, 83, 2], \[83, 119, 2]], "3": \[\[42, 69, 3], \[198, 44, 3]], "4": \[\[85, 17,
      5]], "5": \[\[86, 66, 6]], "bottom": 375, "left": 242, "right": 451, "top": 227}'
  + Trong đó: key đầu tiên là stt/tên của ROI, list \[15, 52, 2] là vị trí trung tâm của ROI, lần lượt xc, yc, delta (sai số cho phép theo pixel, sai số này được tính mặc định là 15% của x2-x1, nghĩa là dán lệch đi 15% thì cho là OK, min là 2)
- Tự động tính `ROIname__quantity__DetectStep__SN__Note` theo bản mẫu đang được nhận dạng, nếu chế độ `Standard Data Sampling` được chọn
- Nếu có  key __Standard_ROIs_Position__ trong level2 thì phải so sánh vị trí của ROIs, nếu không có thì không so sánh, (nếu chưa từng chạy menu `Standard Data Sampling` thì cũng không so sánh vì k có dữ kiện. Nếu so sánh rồi mà NG thì đổi kết quả thông báo, nếu đang ở bước trung gian thì Stepx-NG, nếu bước cuối cùng thì báo "NG", kết quả này ảnh hưởng đến kết quả trung cuộc.
- Thêm tham số `Result_when__OK_NG_OKNG`, để Process kết quả báo về SFIS, giá trị chỉ nhận là một trong số: OK, NG, OKNG
- Phương pháp so sánh vị trí của ROIs:
  + Nếu ảnh được gá lên khung cố định => chiều quay của ảnh là không đổi => `"ImageNotRotatable": 1` => So sánh theo toạ độ xc, yc của ảnh mẫu với ảnh hiện tại `|xc1-xc2|>delta1` thì NG, trong đó xc1 là x mẫu, xc2 là x của ROI hiện tại, delta1 là dao động cho phép của toạ độ x1, tương tự cho yc và các ROI khác
  + Nếu vật chạy động, hoặc không có khung giữ => ảnh có thể xoay => `"ImageNotRotatable": 0` => tính tổng các khoảng cách giữa các tâm của các ROIs = D => nếu `|D1 - D2| > "TotalRoisDistanceErr"` thì NG. `D1 = TotalRoisDistanceErr`
- V17.1:
  + Fixbug: Autolink khai báo tham số làm ảnh hưởng đến các model khác
  + Fixbug: autolink nhận dữ liệu không được
  + Thêm: autolink chỉ cho phép truyền dữ liệu đi lên SFIS 1 lần thôi. Truyền nhiều lần quá sẽ bị căn trên SFIS.
- V17.3:
  + Thay đổi kết cấu của phần mềm. Tất cả OD cho chung vào 1 hàm, thống nhất quy trình như nhau, hiển thị như nhau, riêng SFIS thì cấu hình riêng trong communication khi code.
  + Hiển thị rất nhiều thông tin lên ảnh khi predict xong.
  + Cải thiện tốc độ predict, hiện tại đang đạt được 0.6s/frame xử lý toàn bộ thông tin.
### Chi tiết:

*   Update: V17.0 2023-07-20 19:21:
    
    *   Cập nhật phiên bản V17.0 và thời gian phát hành.
*   Thêm Model Nokia\_TanNhiet:
    
    *   Tạo model Nokia\_TanNhiet để thực hiện các tính năng như gộp các ảnh của nhiều cameras vào 1 để predict, và kiểm tra các đối tượng và vị trí của các đối tượng đó.
    *   Thêm tính năng tự động gán vị trí đối tượng chuẩn.
*   Thêm tính năng Tự động gán vị trí đối tượng chuẩn:
    
    *   Thêm tính năng cho phép tự động gán vị trí đối tượng chuẩn dựa trên thông tin từ các cameras và dữ liệu được cấu hình.
*   Thêm tính năng tự động tính `ROIname__quantity__DetectStep__SN__Note`:
    
    *   Tích hợp tính năng tự động tính toán `ROIname__quantity__DetectStep__SN__Note` dựa trên bản mẫu đang được nhận dạng và các cấu hình được chọn.
*   Thêm tính năng phân biệt nhiều step ở ROIname\_\_quantity\_\_DetectStep\_\_SN\_\_Note:
    
    *   Thêm tính năng cho phép phân biệt nhiều step ở `ROIname__quantity__DetectStep__SN__Note`, giúp việc nhận dạng mẫu được đơn giản hơn.
*   Thêm tính năng fixbug: thêm Total\_Product\_OK, Total\_Product\_NG vào Predict ở Yolov8:
    
    *   Thêm tính năng fixbug cho việc thêm `Total_Product_OK` và `Total_Product_NG` vào Predict ở Yolov8.
*   Thay đổi thông tin bản quyền:
    
    *   Thay đổi thông tin bản quyền và cách cấp bản quyền từ bộ phận AI.
*   Thêm tính năng autolink:
    
    *   Thêm tính năng autolink khai báo tham số làm ảnh hưởng đến các model khác.
    *   Thêm tính năng autolink nhận dữ liệu không được.
    *   Thêm tính năng autolink chỉ cho phép truyền dữ liệu đi lên SFIS 1 lần.
*   Thêm tính năng autolink chỉ cho phép truyền dữ liệu đi lên SFIS 1 lần:
    
    *   Thêm tính năng cho phép truyền dữ liệu đi lên SFIS 1 lần duy nhất để đảm bảo tính chính xác và hiệu quả trong việc truyền dữ liệu.
*   Thêm tính năng autolink chỉ cho phép truyền dữ liệu đi lên SFIS 1 hoặc 2 lần:
    
    *   Thêm tính năng cho phép truyền dữ liệu đi lên SFIS 1 hoặc 2 lần tùy chọn.
*   Thêm tính năng tự động tính `ROIname__quantity__DetectStep__SN__Note` theo bản mẫu đang được nhận dạng:
    
    *   Thêm tính năng cho phép tự động tính toán `ROIname__quantity__DetectStep__SN__Note` dựa trên bản mẫu đang được nhận dạng.
*   Thêm tính năng tự động tính `ROIname__quantity__DetectStep__SN__Note` theo bản mẫu đang được nhận dạng, nếu chế độ `Standard Data Sampling` được chọn:
    
    *   Thêm tính năng cho phép tự động tính toán `ROIname__quantity__DetectStep__SN__Note` dựa trên bản mẫu đang được nhận dạng, và chế độ `Standard Data Sampling` được chọn.
*   Nếu có key `Standard_ROIs_Position` trong level2 thì phải so sánh vị trí của ROIs, nếu không có thì không so sánh:
    
    *   Thêm tính năng cho phép so sánh vị trí của ROIs nếu có thông tin `Standard_ROIs_Position` trong level2, và không so sánh nếu không có thông tin này.
*   Thêm tính năng `Result_when__OK_NG_OKNG`:
    
    *   Thêm tính năng cho phép cấu hình kết quả báo về SFIS dựa trên giá trị `OK`, `NG`, hoặc `OKNG`.
*   Phương pháp so sánh vị trí của ROIs:
    
    *   Thêm tính năng cho phép so sánh vị trí của ROIs dựa trên các thông số như `ImageNotRotatable`, `xc1`, `xc2`, `yc1`, `yc2`, và `TotalRoisDistanceErr`.
*   V17.1:
    
    *   Cập nhật phiên bản V17.1 và thời gian phát hành.
    *   Fixbug: Autolink khai báo tham số làm ảnh hưởng đến các model khác.
    *   Fixbug: autolink nhận dữ liệu không được.
    *   Thêm tính năng autolink chỉ cho phép truyền dữ liệu đi lên SFIS 1 lần thôi.
    *   Truyền nhiều lần quá sẽ bị căn trên SFIS.
*   V17.3:
    
    *   Cập nhật phiên bản V17.3 và thời gian phát hành.
    *   Thay đổi cấu trúc của phần mềm để thống nhất quy trình và hiển thị thông tin như nhau cho tất cả các OD.
    *   Hiển thị rất nhiều thông tin lên ảnh khi predict xong.
    *   Cải thiện tốc độ predict đạt được 0.6s/frame xử lý toàn bộ thông tin.

## Ver 16.x
- Thêm model AutoLink: 
  + đọc 2 barcode trong dải các barcode chạy trên chuyền. 
  + Không dùng CAM vì barcode có 2 tầng độ cao khác nhau, mà dùng đầu đọc mã Keyence.
  + Cấu hình không dùng CAM: Config > cameras > default > UsingCameras: false
  + Khi không có gì từ hệ thống, thì message trả về là Com của đầu đọc là mở được hay không: COMx Open/Closed
- Thêm: tham số điều chỉnh độ rộng giao diện level0: Windows_Width, Windows_Height
- Thêm: tính năng không sử dụng CAM trong chương trình, mặc định là có dùng, cái này sẽ chỉnh trong default của tham số cameras ở level0
- Fixbug: Chỉnh sửa chỗ hiển thị thông tin hệ thống System và SFIS
- Fixbug: Đổi tính năng hiển thị cập nhật trạng thái đang chạy khi pause màn hình để nhìn, nghĩa là nó vẫn chạy, vẫn xử lý, nhưng riêng hiển thị ảnh thì giữ đến hết thời gian chờ.
- Fixbug: No Camera error in taCams
- Thêm lastImagePredicted trong phần tham số trả về, để nó có thể xử lý thoải mái, và app quyết định lưu ảnh lastImagePredicted khi nào, nếu không có tham số này trong lúc trả kết quả thì mặc định là cứ Process xong nghĩa là lastImagePredicted.
- Change: đổi pass cài đặt sang ngày-chục\*2
### Chi tiết:

*   Thêm model AutoLink:
    
    *   Tạo model AutoLink để đọc 2 mã barcode trong dải các barcode chạy trên chuyền sản xuất.
    *   Tích hợp model AutoLink vào phần mềm để sử dụng predict trên các ảnh đầu vào.
*   Thêm tính năng thay đổi kích thước giao diện level0:
    
    *   Thêm tính năng cho phép điều chỉnh độ rộng và chiều cao của giao diện level0.
    *   Đảm bảo giao diện phù hợp và dễ sử dụng trên các kích thước màn hình khác nhau.
*   Thêm tính năng không sử dụng CAM trong chương trình:
    
    *   Thêm tính năng cho phép người dùng tắt sử dụng camera trong chương trình.
    *   Tích hợp tính năng cấu hình các thông số của camera từ file cấu hình.
*   Fixbug: Chỉnh sửa chỗ hiển thị thông tin hệ thống System và SFIS:
    
    *   Sửa lỗi liên quan đến hiển thị thông tin hệ thống và hệ thống SFIS để đảm bảo tính chính xác của thông tin.
*   Fixbug: Đổi tính năng hiển thị cập nhật trạng thái đang chạy khi pause màn hình:
    
    *   Sửa lỗi liên quan đến tính năng hiển thị trạng thái đang chạy khi tạm dừng màn hình để nhìn, đảm bảo tính chính xác và đáng tin cậy.
*   Fixbug: No Camera error in taCams:
    
    *   Sửa lỗi liên quan đến thông báo lỗi No Camera trong phần mềm để đảm bảo tính chính xác và đáng tin cậy của tính năng.
*   Thêm tham số `lastImagePredicted` trong phần trả về:
    
    *   Thêm tính năng lưu trữ thông tin về ảnh được predict cuối cùng vào phần trả về.
    *   Xử lý và quản lý thông tin về ảnh được predict để sử dụng và xử lý tiếp.
*   Change: đổi pass cài đặt sang ngày-chục\*2:
    
    *   Thay đổi cách cài đặt mật khẩu trên phần mềm.


## Ver 15.0
- Update: Thêm nút `Refresh Cameras`, để phần mềm tự đọc các cam đang cắm vào máy, bấm nút này xong thì tắt App đi bật lại mới nhận.
- Update: Menu `File/Decode Barcode`, vừa Decode xong, thì tự lưu ảnh lại vào `Predict_Save_Data/Barcode_decode`, tên đặt theo thời gian, nửa trên là ảnh mới decode, nửa dưới là ảnh gốc, nhìn cho rõ.
- Thêm: Hiển thị thông tin của ảnh lên trực tiếp trên ảnh gốc, vì là nhiều CAM nên mỗi CAM có ánh sáng và focus khác nhau, vị trí này được để sát mép dưới ảnh, không ảnh hưởng đến chất lượng
- Fixbug: Đa ngôn ngữ, nếu câu ngắn thì hiển thị cả tiếng Anh lẫn ngôn ngữ đích, nếu câu dài thì chỉ hiển thị câu đích.
- Fixbug: Stop Multi-Camera, đảm bảo hoạt động chính xác hơn, có hiển thị các lỗi khi Exception.
- Fixbug: Thông báo lỗi khi không mở được COM ở đoạn gọi dữ liệu chờ
- Thêm Model `BarcodeReader`
  - Code: thêm dict lưu trữ ảnh dự đoán `self.wcam_images_results`, từ nay về sau, có bao nhiêu CAM xử  lý bấy nhiêu. Cái này chưa đưa vào hiển thị.  
  - Check liên 1 lần hoặc AutoProcess (sẽ check liên tục)
  - Cho phép truyền nhận SFIS hay không: `Need2Send_to_SFIS`=1: Có truyền nhận
  - Cho phép cấu hình gửi dữ liệu 1 lần hoặc nhiều lần lên SFIS đối với các MAC giống nhau: `Sent_each_Barcode_1time=1`: chỉ truyền lên SFIS nếu chưa truyền lên, muốn truyền lại lên dc thì cho =0 hoặc Stop/Start lại Camera
  - Cho phép truyền nhận lên SFIS 1 hoặc 2 lần: `SFIS_Comm_2_times=1`: Truyền nhận 2 lần, nhận lần 2 là có đuôi PASS/FAIL
  - TODO:
    - Quyết định chính xác đâu là mã MAC cần gửi, hiện tại mới gửi 1 mã đọc được đầu tiên
### Chi tiết:

*   Thêm tính năng Refresh Cameras:
    
    *   Thêm tính năng Refresh Cameras để tự động đọc và tải lại thông tin từ các camera được cắm vào máy.
    *   Đảm bảo tính năng này hoạt động chính xác và đáng tin cậy.
*   Update: Menu `File/Decode Barcode`:
    
    *   Cải tiến tính năng Decode Barcode để lưu ảnh được decode và ảnh gốc vào thư mục `Predict_Save_Data/Barcode_decode`.
*   Thêm: Hiển thị thông tin của ảnh lên trực tiếp trên ảnh gốc:
    
    *   Xây dựng tính năng cho phép hiển thị thông tin về ảnh lên trực tiếp trên ảnh gốc.
    *   Cải thiện khả năng quan sát và hiểu rõ hơn về thông tin từ các camera.
*   Fixbug: Đa ngôn ngữ:
    
    *   Sửa lỗi liên quan đến việc hiển thị câu ngắn hoặc dài ở các ngôn ngữ khác nhau.
*   Fixbug: Stop Multi-Camera:
    
    *   Sửa lỗi liên quan đến tính năng Stop Multi-Camera để đảm bảo hoạt động chính xác hơn.
*   Fixbug: No Camera error in taCams:
    
    *   Sửa lỗi liên quan đến thông báo lỗi No Camera trong phần mềm.
*   Thêm Model `BarcodeReader`:
    
    *   Tạo model BarcodeReader để đọc 2 mã barcode trong dải các barcode chạy trên chuyền sản xuất.
    *   Thêm các tính năng liên quan đến việc truyền và nhận dữ liệu với hệ thống SFIS (Shop Floor Information System).
*   Thêm tính năng truyền và nhận dữ liệu với hệ thống SFIS:
    
    *   Thêm tính năng cho phép truyền và nhận dữ liệu với hệ thống SFIS theo chuẩn được quy định.
*   Thêm tính năng tự động truyền dữ liệu lên SFIS:
    
    *   Tích hợp tính năng tự động truyền dữ liệu lên SFIS một lần duy nhất hoặc nhiều lần tùy chọn.
*   Thêm tính năng quyết định chính xác mã MAC cần gửi:
    
    *   Đảm bảo việc xác định chính xác mã MAC cần gửi dữ liệu lên SFIS để đảm bảo tính chính xác và đáng tin cậy trong việc gửi dữ liệu.


## Ver 14.0
- Thêm Model `RaditorChecking`:
  - Thêm: predict vào app
  - Thêm: init beforun vào app => các thông số riêng có thể chạy được riêng app
  - Thêm: thư viện các lib dành riêng cho predict
  - Thêm: truyền thông 2 cấp cho model nếu cần
  - Thêm: Các chức năng truyền thông theo chuẩn
  - Thêm: Data được phép cấu hình khi truyền thông
  - Thêm: lưu trữ được phép cấu hình khi truyền thông
  
### Chi tiết:
*   Thêm model `RaditorChecking`:
    
    *   Xây dựng mô hình AI object detection đối với việc nhận dạng Raditor (tấm tản nhiệt).
    *   Thêm chức năng predict vào phần mềm và tích hợp mô hình `RaditorChecking` vào quá trình predict.
*   Thêm tính năng init beforun và thư viện các lib dành riêng cho predict:
    
    *   Xây dựng tính năng `init beforun` để thiết lập và chuẩn bị các thư viện cần thiết trước khi thực hiện predict.
    *   Tạo các thư viện riêng cho việc predict để đảm bảo tính riêng biệt và dễ quản lý.
*   Thêm tính năng truyền thông 2 cấp cho model:
    
    *   Thêm tính năng truyền thông 2 cấp cho model AI object detection, cho phép predict từng cấp độ dữ liệu riêng biệt.
*   Thêm tính năng cấu hình dữ liệu khi truyền thông:
    
    *   Thêm tính năng cấu hình dữ liệu khi truyền thông cho phép định dạng và kiểm soát dữ liệu được truyền tải giữa các cấp độ.
*   Thêm tính năng lưu trữ dữ liệu khi truyền thông:
    
    *   Tích hợp tính năng lưu trữ dữ liệu khi truyền thông để quản lý và sử dụng lại thông tin truyền tải giữa các cấp độ.


## Ver 13
- Thay đổi cấu trúc hệ thống: 
  - Thêm tính năng chạy nhiều cam cùng lúc.
  - Thêm tính năng gộp các cam lại thành 1 ảnh
  - Thêm tính năng resize ảnh tổng thể để predict gộp 1 lần
  - Thêm tính năng tự động cấu hình CAM
  - Thêm: cam default (để lưu cấu hình các tham số mặc định cho tất cả các Cam)
  - Thêm: Hiển thị lựa chọn Cam trên phần mềm
  - Thêm: biểu diễn các thông số của các CAM trên giao diện
  - Thêm: Save => các thông số trong giao diện của cam sẽ được ghi lại vào file config => không cần vào file config để cấu hình
  - Thêm: Tự tạo lại Cam khi tham số cameras trong file config bị xoá đi
### Chi tiết:
*   Thêm tính năng chạy nhiều cam cùng lúc:
    
    *   Thay đổi giao diện và cấu trúc phần mềm để hỗ trợ chạy đồng thời nhiều camera cùng một lúc.
    *   Xử lý dữ liệu từ các camera khác nhau và tích hợp vào quá trình predict.
*   Thêm tính năng gộp các cam lại thành 1 ảnh:
    
    *   Xây dựng tính năng cho phép gộp các ảnh từ nhiều camera thành một ảnh duy nhất để thực hiện predict.
    *   Tối ưu hóa mã nguồn để xử lý các ảnh được gộp lại và đảm bảo tính chính xác của predict.
*   Thêm tính năng resize ảnh tổng thể để predict gộp 1 lần:
    
    *   Định nghĩa các tham số cấu hình cho việc resize ảnh tổng thể trong quá trình predict.
    *   Xử lý và điều chỉnh kích thước ảnh tổng thể trước khi thực hiện predict để tối ưu hóa hiệu suất.
*   Thêm tính năng tự động cấu hình CAM:
    
    *   Xây dựng chức năng tự động cấu hình các camera sử dụng thông tin từ hệ thống và tùy chọn của người dùng.
    *   Đảm bảo tính linh hoạt và dễ sử dụng trong việc cấu hình các camera.
*   Thêm: cam default và hiển thị lựa chọn Cam trên phần mềm:
    
    *   Tạo cam default để lưu cấu hình các tham số mặc định cho tất cả các camera.
    *   Hiển thị lựa chọn Camera trên giao diện để người dùng có thể chọn và cấu hình các thông số riêng cho từng camera.
*   Thêm tính năng Save và lưu trữ cấu hình Cam:
    
    *   Tích hợp tính năng lưu trữ cấu hình của Camera vào phần mềm.
    *   Tự động tạo lại Camera nếu cấu hình bị mất.

## Ver 12.1
- Release date: 2023-05-18 10:26
- OWL|SmartSpeaker: 
  - Fixbug truyền thông. 
  - hỗ trợ truyền nhận với:
    - timeout, 
    - chuỗi kết thúc là 1 hoặc nhiều ký tự, 
    - khắc phục tình trạng chờ hết timeout mới hiện kết quả SFIS

# Sagecom - HDD

# Nokia - Telit
### HDSD:
- Khởi động phần mềm
- Bấm start Camera
- Tích chọn Auto Process (bên dưới nút bấm Process)

Truyền thông:
![Comm.png](Data_Standard%2FTelit%2FComm.png)
![Comm1.png](Data_Standard%2FTelit%2FComm1.png)

in ZPL:
copy ta.zpl \\localhost\ZDesignerZT610_600dpiZPL


# Cài đặt:

https://stackoverflow.com/questions/76379293/how-can-i-fix-the-error-in-pymupdf-when-installing-paddleocr-with-pip
```
pip install "paddleocr>=2.0.1" --upgrade PyMuPDF==1.21.1  
```


