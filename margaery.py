#!/usr/bin/env python3
# Requires PyAudio and PySpeech.
 
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
import cv2
from tts_stt import speak, recordAudio
from nodes.define import define_subject
from nodes.alarm import alarm
from nodes.whereis import whereis

def jarvis(data):

    if "how are you" in data:
        speak("I am fine")
 
    if "what time is it" in data:
        speak(ctime())
 
    if "where is" in data:
        whereis(data)

    if 'alarm' in data or 'timer' in data:
        alarm(data)

    if 'define' in data:
        define_subject(data)

# initialization
time.sleep(2)

while 1:
    data = recordAudio()
    activation_list = ['alibi', 'hey alibi', 'hay alibi', 'hi alibi']
    if 'marjorie' in data: #need to check how it spells this
        speak("Hi Michael, what can I do for you?")
        data = recordAudio()
        jarvis(data)


