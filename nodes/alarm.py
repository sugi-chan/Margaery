
from gtts import gTTS
import pyglet
import _thread 
import threading
import re


def alarm(speech_data):
    print('alarm!',speech_data)
    result = re.sub('[^0-9]','', speech_data)
    print(result,int(result)*60)

    def alarm2():
        tts = gTTS(text="Time is up!", lang='en-uk')
        tts.save("audio/timer.mp3")
        song = pyglet.media.load("audio/timer.mp3")
        song.play()

    t = threading.Timer(int(result)*60.0, alarm2)
    t.start()

    return
        