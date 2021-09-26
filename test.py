from pytube import YouTube, Search, captions


yt = YouTube("http://youtube.com/watch?v=2lAe1cqCOXo")
choice = yt.captions

print(choice.lang_code_index)
for k,v in choice.lang_code_index.items():
    print(k)
    caption = choice.get_by_language_code(k)
    print(caption.xml_captions)
