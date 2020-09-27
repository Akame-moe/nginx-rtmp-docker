
### 1.BUILD
```
docker build -t nginx-rtmp .
```

### 2.RUN
```
docker run --name live -p 8080:8080 -p 1935:1935 -d nginx-rtmp
```

### 3.TEST
- push mp4 stream via ffmpeg
  ```
  ffmpeg -re -i input.mp4 -vcodec libx264 -vprofile baseline -g 30 -acodec aac -strict -2 -f flv rtmp://<IP-ADDRESS>:1935/live/stream
  ```

- push stream via OBS
  set `rtmp://<IP-ADDRESS>:1935/live` as stream url and `stream` as key, then start push stream

- pre-convert mp4 format to flv format  
  ```
  ffmpeg -i input.mp4 -c:v libx264 -preset medium -b:v 3000k -maxrate 3000k -bufsize 6000k -vf "scale=1280:-1,format=yuv420p" -g 50 -c:a aac -b:a 128k -ac 2 -ar 44100 -strict -2 movie.flv
  ```
  then push with following command
  ```
  ffmpeg -re -i file.flv -c copy -f flv rtmp://<IP-ADDRESS>:1935/live/stream
  ```

- watch  
open link `http://<IP-ADDRESS>:8080/hls/stream.m3u8` with potplayer  and enjoy your achievement!