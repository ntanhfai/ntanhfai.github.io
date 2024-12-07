---
layout: default
title: Web-System-Tools's Lesson path
---

# Bài học: chuẩn bị cho các bài học tiếp theo.


## Links:
- [Go Home](https://ntanhfai.github.io/)

## Nội dung
Link GitHub của lớp AI-Class: [Tại đây](https://github.com/ntanhfai/ntanhfai.github.io/tree/main/Web-System-Tools). Bạn cần phải theo dõi Github này thường xuyên vì nó có thể liên tục được cập nhật 

##    1. Cài đặt môi trường
- Cách 1: Cài Anaconda: Môi trường tự động cài mọi thứ cần thiết, tuy nhiên cài nhiều quá sẽ gây nặng máy, khuyên dùng cho người mới
  + Trên Ubuntu/Mac: [tham khảo tại đây](https://www.ikkaro.com/vi/anaconda/)
  + Trên Windows:  [tham khảo tại đây](https://websitehcm.com/cai-dat-thu-vien-keras-trong-anaconda/)

  Tài liệu ngắn gọn về cách sử dụng anaconda: 
   [Xem tại đây](https://docs.conda.io/projects/conda/en/4.6.0/_downloads/52a95608c49671267e40c689e0bc00ca/conda-cheatsheet.pdf), 
   hoặc [tại đây](https://kapeli.com/cheat_sheets/Conda.docset/Contents/Resources/Documents/index)


- Cách 2: Cài Python Virtual Environment: cài ít hơn, nhưng khó cài thư viện hơn cách 1. Khuyên dùng cho học viên thành thạo.
    + tham khảo cách cài dặt [tại đây](https://viblo.asia/p/tao-virtual-environment-va-su-dung-cac-goi-thu-vien-thong-qua-pip-trong-python-Az45bmAVlxY),
      và [tại đây](https://mothergeo-py.readthedocs.io/en/latest/development/how-to/venv-win.html)
    + hoặc cho linux [tại đây](https://www.geeksforgeeks.org/creating-python-virtual-environment-windows-linux/)
  
    
##    2. Cài đặt IDE
  
Lựa chọn 1 trong số các IDE thông dụng: Pycharm Community
- Jupyter-Notebook  (Dùng cho Colab, online, bắt buộc, free)
- Pycharm Community (Khuyên dùng cho máy local, free)
  + Hướng dẫn cài đặt và tạo môi trường virtual environment [tham khảo tại đây](https://www.thegioididong.com/game-app/huong-dan-cai-dat-su-dung-pycharm-lap-trinh-python-1316867)
  

- Sublime-Text      (Khuyên cài, kết hợp với Pycharm Community, dùng thử)
    
##     3. Cài đặt các thư viện
Phương pháp cài đặt các thư viện, các thư viện cần thiết nhất cần cài trước.
- opencv-python (CV2): đọc webcam, đọc ghi video, xử lý ảnh, đọc ghi ảnh.
- Numpy: thực hiện các phép toán, biến đổi ma trận,...
- pyzbar (để đọc mã vạch)


# Các thứ cần học trước khi học Python:

## Học cách viết tài liệu Markdown 
Tài liệu markdown là tài liệu có đuôi .md, chính là tài liệu bạn đang đọc này, 
nó là một dạng mới của HTML có hỗ trợ rất mạnh cho việc hiển thị Code, format dễ dàng, dễ nhìn hơn HTML rất nhiều. 

Nó được sử dụng rộng rãi trong githuc/gitlab,... 
- Tham khảo [tại đây](https://viblo.asia/helps/cach-su-dung-markdown-bxjvZYnwkJZ)
- Bản tra cứu ngắn gọn; [Xem](https://www.markdownguide.org/cheat-sheet/)

# Kế hoạch học tập

Dưới đây là kế hoạch học tập của từng người theo đuổi khóa học. 
- Mỗi ngày học cuốn chiếu, liên tục 8 tiết, mỗi tiết 50p, giải lao 10p.
- Học 1 hôm có thể nghỉ 1 hôm, không nghỉ quá 2 hôm giữa các ngày học.
- Cuối mỗi ngày, báo cáo kết quả vào phần ISSUE của git repository.  

## Nội dung cho chuyên ngành: Web

| STT        | Nội dung học                                                                                                                                   | Tài liệu                                                                                        |
|------------|------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| Day 0      | Chuẩn bị: Đăng ký tài khoản github, cài đặt môi trường chạy Python, cài Pycharm Community. Dùng Pycharm, clone 1 project bất kỳ xuống máy tính |                                                                                                 |
| Day 1*     | Học xong hết (6 videos quan trọng nhất) về Python trong 1 ngày, học tốc độ 1.7x, chỉ cần hiểu, không cần thuộc                                 | [Tại đây](http://aisolutions.vn/ai/dlclass/index.php)                                           |
| Day 2*     | Đọc lại Python cheatsheets của tất cả các nội dung đã học, chép lại tóm tắt theo ý hiểu, chép thuộc kiến thức cơ bản                           | [Tại đây](https://github.com/anh-ai/AI_Libs/blob/main/Data-Books/000%20Python%20cheatsheet.pdf) |
 | Lesson 01* | Web Flask: học thuộc 1 bài (tùy chọn)                                                                                                          |                                                                                                 |
| Lesson 02* | Upload file dùng flask + Bootstrap 4                                                                                                           |                                                                                                 |
| Lesson 03* | Offices (word và excel, chọn 1 bài cần thiết để học thuộc.                                                                                     |                                                                                                 |
| Lesson 04  | Database: Đọc hiểu cách thức sử dụng database (No SQL), đến mức có thể giảng cho người khác hiểu là đạt.                                       |                                                                                                 |
| Lesson 05  | Web kết hợp với database (NoSQL). Học hiểu, giải thích được có các thành phần nào, dùng để làm gì là đạt.                                      |                                                                                                 |

Chú ý: bài có dấu * là bài bắt buộc phải học thuộc (phần head của HTML có thể chỉ cần hiểu là được)

## Chú ý:

Mỗi ngày học xong cần phải báo cáo kết quả vào ISSUE 
- Cách thức: mỗi người lập 1 ISSUE có tiêu đề: Báo cáo tình hình học tập: <họ tên, lớp>
- Mỗi ngày báo cáo sẽ viết tiếp Comment vào ISSUE của mình (lọc bên trên, phần Author để tìm luồng của mình)
- Nội dung báo cáo mỗi ngày:
  - Hôm nay đã hoàn thành những gì
  - Thu được kết quả như nào? 
    - Xem xong mấy video, 
    - chép nhớ được bào nhiêu lần, 
    - đã nhớ những nội dung gì, 
    - code nào đã hoàn thành, 
    - code nào cần phải nhớ, 
    - khó khăn gặp phải là gì? câu hỏi cần hỏi? 
    - các todo list cần phải hoàn thành là những gì?
    - ...
  - Báo cáo được viết theo chuẩn của Markdown Github (tiêu đề, trích dẫn, code,... cần đúng quy định của Git)

Đến đây bạn đã hiểu về python, cách thức tra cứu tài liệu, cách thức tra cứu để tự làm 1 bài toán Python.



