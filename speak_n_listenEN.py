import pyttsx3
import speech_recognition as sr


engine = pyttsx3.init()
engine.setProperty("rate", 200)
engine.setProperty("voice", "english")

r = sr.Recognizer()

def speak(text):
    engine.say(text)
    engine.runAndWait()


def listen():
    with sr.Microphone() as source:
        print("You can talk now!")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio, language="en-US")
            print("I´ve heard: -- {} --".format(text))
            return text
        except sr.UnknownValueError:
            print("I did not heard what you say :(")

#by: github.com/vapemx