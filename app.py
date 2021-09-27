from flask import Flask, render_template, request, redirect, send_file
from pytube import YouTube, Search

app=Flask(__name__)

storage = {}

@app.route("/",methods=["POST","GET"])
def main():
    if request.method=="POST":
        try:
            url = request.form.get("yt_url")
            yt = YouTube(url)
            ID = yt.video_id
            storage["ytObject"] = yt
            return redirect(f"/downloadPage/{ID}")
        except:
            msg = "Please enter a valid URL"
            return render_template("home.html",msg=msg)
    else:
        return render_template("home.html")

@app.route("/downloadPage/<video_url>",methods=["POST","GET"])
def downloadPage(video_url):
    yt = storage["ytObject"]
    videoID = yt.video_id
    title = yt.title
    #Audio download
    audio_streams = yt.streams.filter(only_audio=True)
    #mp4 download
    video_streams = yt.streams.filter(file_extension="mp4")
    #caption download
    caption_choices = yt.captions.lang_code_index
    return render_template("downloadPage.html",title=title,videoID=videoID,
                            audio_streams=audio_streams,video_streams=video_streams,
                            caption_choices=caption_choices)

@app.route("/download",methods=["POST","GET"])
def download():
    youtube_object = storage["ytObject"]
    audio_downloadTag = request.form.get("audios")
    video_downloadTag = request.form.get("videos")
    caption_downloadTag = request.form.get("captions")
    if audio_downloadTag:
        file_path = youtube_object.streams.get_by_itag(audio_downloadTag).download()
        return send_file(file_path,as_attachment=True)
    elif video_downloadTag:
        file_path = youtube_object.streams.get_by_itag(video_downloadTag).download()
        return send_file(file_path,as_attachment=True)
    elif caption_downloadTag:
        caption_raw = youtube_object.captions.get_by_language_code(caption_downloadTag)
        xml_text = caption_raw.xml_captions
        f=open(f"{youtube_object.title} caption in {caption_downloadTag}.txt","w+")
        f.write(xml_text)
        f.close()
        caption_file_name=f"{youtube_object.title} caption in {caption_downloadTag}.txt"
        return send_file(caption_file_name,as_attachment=True)

@app.route("/search", methods=["POST","GET"])
def search():
    if request.method=="POST":
        return redirect('/downloadPage2')
    else:
        return render_template("search.html")
    

@app.route("/downloadPage2", methods=["POST","GET"])
def downloadPage2():
    keyWord=request.form.get("search_word")
    video_list = Search(keyWord)
    return render_template("viewplayList.html",video_list=video_list.results)


if __name__=="__main__":
    app.run(debug=True)