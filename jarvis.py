import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import pyaudio
import webbrowser
import os

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voices',voices[1].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour <18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")    
        
    speak("Hello I m Jarvis. How can i help you?")   


def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=0.5
        audio=r.listen(source)

    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print("User Said",query)

    except Exception as e:
        print("Please say it again.")
        return "none"

    return query   


    
if __name__ == "__main__":
    wishMe()
    while True:
        query=takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query=query.replace("wikipedia","")
            result=wikipedia.summary(query,sentences=5)
            speak("According to wikipedia")
            print(result)
            speak(result)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir="E:\Songs\Arijit"
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        elif 'thank you jarvis'in query:
            speak("You are welcome, Have a good day!")