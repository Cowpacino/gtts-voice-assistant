# Requires PyAudio, PySpeech, Speech Recognition, Playsound, Requests, AppOpener, gTTS.
# Please Install Playsound from this command: pip install playsound@git+https://github.com/taconi/playsound

import speech_recognition as sr
import subprocess
import requests
from time import ctime
import time
from gtts import gTTS
import playsound
from AppOpener import open

def speak(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='en')
    filename = "voice.mp3" 
    tts.save(filename)
    playsound.playsound(filename)

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
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    return data

def get_weather(location):
    api_key = #GET YOUR API KEY AT openweathermap.org
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    print("URL:", url)
    response = requests.get(url)
    data = response.json()
    if data["cod"] == 200:
        weather_description = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        return f"The weather in {location} is {weather_description}. The temperature is {temperature} degrees Celsius."
    else:
        return "Unable to fetch weather information for the specified location."
    
def get_name():
    name = recordAudio()
    if name == "":
        speak("Sorry i couldn't quite hear you. Can you please speak again?")
        return get_name()
    else:
        return name

def change(data):
    arr = data.split(" ")
    for count,plus in enumerate(arr):
        if plus == "+":
            plus = "plus"
            arr[count] = "plus"
    data = " ".join(arr)
    return data

def assistant(data):
    if "how are you" in data.lower():
        speak("I am fine")

    elif "what time is it" in data.lower() or "time" in data.lower():
        speak(ctime())

    elif "where is" in data.lower() or "location" in data.lower():
        data = data.split(" ")
        if "in" in data:
            place_index = data.index("is") + 1
        elif "of" in data:
            place_index = data.index("of") + 1
        place = " ".join(data[place_index:])
        speak(f"Hold on {name}, I will show you where " + place + " is.")
        url = f"https://www.google.nl/maps/place/{place}"
        subprocess.run(["start", "msedge", url], shell=True)
    
    elif "weather" in data.lower():
        data = data.split(" ")
        if "in" in data:
            place_index = data.index("in") + 1
        elif "of" in data:
            place_index = data.index("of") + 1
        elif "for" in data:
            place_index = data.index("for") + 1    
        elif "at" in data:
            place_index = data.index("at") + 1

        place = " ".join(data[place_index:]) 
        weather_info = get_weather(place)
        speak(weather_info)

    
    elif "youtube" in data.lower():
        speak("What do you want to search in youtube")
        time.sleep(2)
        query = recordAudio()
        url = f"https://www.youtube.com/results?search_query={query}"
        subprocess.run(["start", "msedge", url], shell=True)

    elif "close" in data.lower():
        speak("Im glad I could help you. Have a nice day")
        exit()
    
    elif "maths" in data.lower() or "mathematical" in data.lower() or "equation" in data.lower() or "equations" in data.lower():
        speak("What kind of question do you have for me?")
        time.sleep(2)
        question = recordAudio()
        if "+" in question:
            question = change(question)
        result = f"https://www.google.com/search?q={question}"
        subprocess.run(["start", "msedge", result], shell=True)
    
    elif "internet" in data.lower() or "google" in data.lower():
        speak("What do you want to Search?")
        question = recordAudio()
        result = f"https://www.google.com/search?q={question}"
        subprocess.run(["start", "msedge", question], shell=True)
    
    elif "news" in data.lower() or "headlines" in data.lower():
        result = "https://timesofindia.indiatimes.com/home/headlines"
        subprocess.run(["start", "msedge", result], shell=True)
    
    elif "open" in data.lower():
        speak("What application do you want to start?")
        application = recordAudio()
        open(application)

# Initialization
speak("Hey Im your personal assistant. What is your name?")
name = get_name()
speak(f"Hey {name} what are your queries for today?")
while True:
        data = None
        data = recordAudio()
        assistant(data)
