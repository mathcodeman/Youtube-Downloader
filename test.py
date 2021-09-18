from pytube import YouTube, Search
from pytube.extract import video_id

yt = YouTube('https://www.youtube.com/watch?v=WMI0TTgy3y8')
print(type(yt))
video = yt.streams.filter(only_audio=True)
print(video)
v = yt.streams.get_by_itag(22)
print(type(v))