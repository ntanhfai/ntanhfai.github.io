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

