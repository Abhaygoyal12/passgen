import pyttsx3 # for converting text to speech
import datetime #for current time to A.I.
import speech_recognition as sr
import wikipedia
import webbrowser  #to open any website

engine= pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
#print(voices)
engine.setProperty('voice',voices[1].id)
#print(voices[1].id)
#we made a speak function to convert our text to speech

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
# using wishme function our jarvis will greet the user according to time on your pc

def wishme():
    hour= int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning!")
    elif hour>=12 and hour<17:
        speak("good afternoon!")
    else:
        speak("good evening!")

    speak("i am jarvis . how may i help you")

#With the help of the takeCommand() function, our A.I. assistant will return a string output by taking microphone input from the use


def takecommand():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold=1
        audio = r.listen(source)

    try:
       print("recognizing..")
       query= r.recognize_google(audio,language='en-in')  #Using google for voice recognition.
       print("user said: ", query)

    except Exception as e:
       print("say the please again...")
       return "none"
    return query




if __name__ == '__main__':
    speak("abhay is a good boy")
    wishme()
    while True:
        query= takecommand().lower()
        if 'wikipedia' in query:
            speak("searching wikipedia...")
            query= query.replace("wikipedia","")
            results= wikipedia.summary(query,sentences=2)
            speak("according to wikipedia...")
            print(results)
            speak(results)
        elif 'youtube' in query:
            webbrowser.open("youtube.com")
        elif 'instagram' in query:
            webbrowser.open("instagram.com")
        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

