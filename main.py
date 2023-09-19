from pytube import YouTube
import os
from moviepy.editor import *
from io import StringIO
import PySimpleGUI as sg

def showstreams(yt):
    result = yt.streams.filter(progressive=True, file_extension='mp4')
    return result

def selectSong(url, output):
    while True:
        yt = YouTube(url)
        title = f'{yt.title}.mp4'
        filename = f'{output}\{title}'
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

def runCommand(url, saveas, timeout=None, window=None):
    p = selectSong(url, saveas)
    output = ''
    for line in p.stdout:
        line = line.decode(errors='replace' if (sys.version_info) < (3, 5) else 'backslashreplace').rstrip()
        output += line
        print(line)
        window.Refresh() if window else None        # yes, a 1-line if, so shoot me
    retval = p.wait(timeout)
    return (retval, output)


frame_layout = [[sg.Multiline("", size=(80, 20), autoscroll=True,
    reroute_stdout=True, reroute_stderr=True, key='-OUTPUT-')]]
sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Link: '), sg.Input(size=(15,1), pad=(0,0), key='-URL-')],
            [sg.Text('Save to: '), sg.Input(size=(15,1), key='-SAVEAS-'), sg.FolderBrowse()],
            [sg.Frame("Output console", frame_layout)],
            [sg.Button('Ok', key='-OK-'), sg.Button('Exit', key='-EXIT-')] ]

# Create the Window
window = sg.Window('YT-MP3', layout, finalize=True)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == '-EXIT-': # if user closes window or clicks cancel
        break
    elif event == '-OK-':
        #runCommand(values['-URL-'], values['-SAVEAS-'], window=window)
        selectSong(values['-URL-'], values['-SAVEAS-'])
        continue

window.close()

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