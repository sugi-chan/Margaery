
import webbrowser

from tts_stt import speak

def whereis(data):
    data = data.split(" ")
    location = data[2]
    speak("Hold on Michael, I will show you where " + location + " is.")
    url = "https://www.google.nl/maps/place/" + location + "/&amp;"
    webbrowser.open(url, new=0, autoraise=True)