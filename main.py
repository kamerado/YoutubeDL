from pytube import YouTube
import os
from moviepy.editor import *
from io import StringIO

def showstreams(yt):
    result = yt.streams.filter(progressive=True, file_extension='mp4')
    return result

def selectSong():
    while True:
        song = input('enter song url: \n')
        yt = YouTube(song)
        title = f'{yt.title}.mp4'
        filename = f'Videos\{title}'
        title2 = yt.title + '.mp3'
        print(title)
        streams = f'{showstreams(yt)}'
        streams = streams.split(',')
        for i in streams:
            if 'itag="22"' in i:
                itag = 22
                stream = yt.streams.get_by_itag(itag)
                stream.download('Videos')
            elif 'itag="18"' in str(i):
                stream = yt.streams.get_by_itag(18)
                stream.download('Videos')
            else:
                print('nada') 
        video = VideoFileClip(os.path.join("Videos",title))
        video.audio.write_audiofile(os.path.join("Videos",title2))
        video.close()
        os.remove(filename)
        break


if __name__ == '__main__':
    while True:
        ine = input('S to start, X to quit.').lower()
        if ine == 's':
            song = selectSong()
        elif ine == 'x':
            exit()
        else:
            print('wrong input.')
            continue