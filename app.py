from flask import Flask, render_template, request, redirect
from pytube import YouTube


app=Flask(__name__)

@app.route("/",methods=["POST","GET"])
def main():
    if request.method=="POST":
        return redirect("/downloadPage")
    else:
        return render_template("home.html")

@app.route("/downloadPage",methods=["POST", "GET"])
def retrieve():
    url = request.form.get("yt_url")
    yt = YouTube(url)
    videoID = yt.video_id
    title = yt.title
    #Audio download
    audio_streams = yt.streams.filter(only_audio=True)
    #mp4 download
    video_streams = yt.streams.filter(file_extension="mp4")
    return render_template("downloadPage.html",title=title,url=url,videoID=videoID,audio_streams=audio_streams,video_streams=video_streams)

@app.route("/download",methods=["POST","GET"])
def download():
    downloadTag = request.form.get("audios")
    print(downloadTag)
    return redirect("/")
        
if __name__=="__main__":
    app.run(debug=True)