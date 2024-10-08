import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import wikipedia
import os

try:
    import pyaudio
except ImportError:
    print("pyaudio module not found. Installing pyaudio...")
    try:
        print("!pip install pyaudio")
    except:
        print("pyaudio module installation failed. Please install manually.")
        exit()


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    
    speak("I am Perry Sir. Please tell me how I may help you")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

if __name__ == "__main__":
    wishme()
    while True:
        query = takecommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia......')
            query = query.replace("wikipedia", "")
            try:
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except wikipedia.exceptions.PageError:
                speak("Sorry, the page you're looking for doesn't exist.")
        elif 'open youtube' in query:
            speak("opening youtube sir")
            webbrowser.open("https://www.youtube.com/")
        elif 'open google' in query:
            speak("opening google sir")
            webbrowser.open("https://www.google.com/")   
        elif 'open jiocinema' in query:
            speak("opening jio cinema sir")
            webbrowser.open("https://www.jiocinema.com/")    
        elif 'open ai' in query:
            speak("opening chatgpt sir")
            webbrowser.open("https://chat.openai.com/")
        elif 'open stack' in query:
            speak("openig stackoverflow sir")
            webbrowser.open("https://stackoverflow.com/")
        elif 'play music' in query:
            speak("playing music sir")
           # os.startfile("D:\song\Cheri-Cheri-Lady.mp3")    
        elif'the time'in query:
            strtime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strtime}")
        elif'hello 'in query:
            speak("hello darshil how can i help you")
        elif'mera ek dost hai'in query:
            speak("Yes I know Yuvraj who doesn't have Chinki anymore but still dreams of meeting her")
        elif'you know who is'in query:
            speak("yes,its number six ")    
        elif 'exit' in query:
            speak("Goodbye, have a great day darshil!")
            break
        else:
            speak("I didn't understand that. Please try again.")