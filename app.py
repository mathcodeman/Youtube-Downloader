from flask import Flask, render_template, request, redirect, send_file
from pytube import YouTube


app=Flask(__name__)

storage = {}

@app.route("/",methods=["POST","GET"])
def main():
    if request.method=="POST":
        return redirect("/downloadPage")
    else:
        return render_template("home.html")

@app.route("/downloadPage",methods=["POST","GET"])
def downloadPage():
    url = request.form.get("yt_url")
    yt = YouTube(url)
    storage["ytObject"] = yt
    print(storage)
    videoID = yt.video_id
    title = yt.title
    #Audio download
    audio_streams = yt.streams.filter(only_audio=True)
    #mp4 download
    video_streams = yt.streams.filter(file_extension="mp4")
    return render_template("downloadPage.html",title=title,url=url,videoID=videoID,audio_streams=audio_streams,video_streams=video_streams)

@app.route("/download",methods=["POST","GET"])
def download():
    youtube_object = storage["ytObject"]
    audio_downloadTag = request.form.get("audios")
    video_downloadTag = request.form.get("videos")
    print(video_downloadTag)
    if audio_downloadTag:
        file_path = youtube_object.streams.get_by_itag(audio_downloadTag).download()
        return send_file(file_path,as_attachment=True)
    elif video_downloadTag:
        file_path = youtube_object.streams.get_by_itag(video_downloadTag).download()
        return send_file(file_path,as_attachment=True)

    

if __name__=="__main__":
    app.run(debug=True)