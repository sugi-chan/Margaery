'''
handles text to speech and speech to text
'''

import speech_recognition as sr
from time import ctime
import time
import os
from gtts import gTTS
from pygame import mixer 
import pyglet
import webbrowser
import datetime
import _thread 
import threading
import re


def speak(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='en-uk')
    tts.save("audio/test1.mp3")
    song = pyglet.media.load("audio/test1.mp3")
    song.play()
   

def recordAudio():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
 
    # Speech recognition using Google Speech Recognition
    data = ""
    try:
        # Uses the default API key
        # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        data = r.recognize_google(audio)
        data = data.lower()
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
 
    return data
