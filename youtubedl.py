from pytube import YouTube

def download(yt):
    pass

def showstreams(yt):
    yt.streams.filter(progressive=True, file_extension='mp3')
    result = yt.streams.filter(progressive=True, file_extension='mp4')
    return result
    