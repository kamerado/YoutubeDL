from pytube import YouTube
import youtubedl
import os
from moviepy.editor import *

def selectSong():
    while True:
        song = input('enter song url: \n')
        yt = YouTube(song)
        title = f'{yt.title}.mp4'
        filename = f'Videos\{title}'
        title2 = yt.title + '.mp3'
        print(title)
        a = input('correct?')
        print(youtubedl.showstreams(yt))       
        itag = input('\nSelect itag: \n')
        try:
            stream = yt.streams.get_by_itag(itag)
            stream.download('Videos')
        except Exception:
            print('Try another url: ')
            continue  
        video = VideoFileClip(os.path.join("Videos",title))
        video.audio.write_audiofile(os.path.join("Videos",title2))
        video.close()
        os.remove(filename)

if __name__ == '__main__':
    ine = ''
    title = ''
    while ine != 'x':
        ine = input('S to start, X to quit.').lower()
        if ine == 's':
            title = selectSong()
        else:
            print('wrong input.')
            continue