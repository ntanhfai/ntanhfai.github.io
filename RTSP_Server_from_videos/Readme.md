# Phát rtsp stream từ videos

Copy video path to `video_list.txt` file, 

```
"G:\Cam360Data\192.168.43.58_8555_live.mp4"
"G:\Cam360Data\all_video.mp4"
"G:\Cam360Data\TAHome.mp4"

```

run `mediamtx_rtsp_server_muliple_video_V2_From_video_list.bat`

nó sẽ in ra một file rtsp link như sau:

```
rtsp://localhost:8554/live1.sdp 
rtsp://localhost:8554/live2.sdp 
rtsp://localhost:8554/live3.sdp 
```

# Nội dung của mediamtx_rtsp_server_muliple_video_V2_From_video_list.bat

```cmd
@echo off
rem File này đọc danh sách video từ file text và tự động phát lên RTSP.
rem Đồng thời ghi URL của các luồng RTSP vào file output_rtsp.txt.

setlocal enabledelayedexpansion

rem Đường dẫn file chứa danh sách video
set "video_list=video_list.txt"

rem File ghi danh sách các URL RTSP
set "output_rtsp=output_rtsp.txt"

rem Kiểm tra file danh sách video
if not exist "%video_list%" (
    echo [ERROR] File "%video_list%" không tồn tại. Vui lòng tạo file này và nhập danh sách video.
    pause
    exit /b
)

rem Xóa file RTSP cũ nếu tồn tại
if exist "%output_rtsp%" del "%output_rtsp%"

rem Khởi động MediaMTX
start "" "G:\mediamtx\runMTX.bat"

rem Chờ vài giây để MediaMTX khởi động
timeout /t 5 /nobreak >nul

rem Biến đếm số luồng
set "stream_index=1"

rem Đọc từng dòng trong file video_list.txt
for /f "usebackq delims=" %%A in ("%video_list%") do (
    rem Tạo URL RTSP cho luồng hiện tại
    set "rtsp_url=rtsp://localhost:8554/live!stream_index!.sdp"
    
    rem Phát video qua FFmpeg
    echo [INFO] Đang phát video: %%A
    start "" ffmpeg -re -i "%%A" -c:v libx264 -preset veryfast -maxrate 800k -bufsize 1600k -vf "scale=720:360" -g 50 -f rtsp !rtsp_url!
    
    rem Ghi URL RTSP vào file
    echo !rtsp_url! >> "%output_rtsp%"
    
    rem Tăng biến đếm luồng
    set /a stream_index+=1
)

rem Hoàn tất
echo [INFO] Đã phát tất cả các video trong danh sách.
echo [INFO] Danh sách URL RTSP đã được ghi vào "%output_rtsp%".

pause
```