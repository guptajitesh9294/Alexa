import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import time
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()
    # time.sleep(30)


def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening......")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            # print(command)
            if 'alexa' in command:
                command = command.replace("alexa", "")
            # print(command)
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    if command:
        print(command)
        if 'play' in command:
            song = command.replace('play', '')
            talk("playing" + song)
            pywhatkit.playonyt(song)
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M')
            talk("Current Time is " + time)
        elif 'who is' in command:
            try:
                person = command.replace('who is', '')
                info = wikipedia.summary(person, 1)
                talk(info)
            except:
                talk('I cant find the information about {}'.format(person))
        elif 'joke' in command:
            talk(pyjokes.get_joke())
            print(pyjokes.get_joke())
        else:
            talk('Repeat kro nahi samajh aya')
    else:
        pass


while True:
    try:
        run_alexa()
    except:
        run_alexa()
