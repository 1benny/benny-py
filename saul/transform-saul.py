from pytube import YouTube

vid = YouTube("https://youtube.com/watch?v=CNcHPxHX63c")

title = vid.title
thumb = vid.thumbnail_url

vid = vid.streams.get_highest_resolution()

vid.download()