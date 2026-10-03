import webbrowser
import datetime
import pyttsx3
import speech_recognition as sr
import pyjokes


def sptext():
    recognizer = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
            try:
                print("Recognizing...")
                data = recognizer.recognize_google(audio)
                print(data)
                return data.lower()
            except sr.UnknownValueError:
                print("Not Understand")
                return ""
            except sr.RequestError:
                print("Could not request results from Google Speech Recognition service.")
                return ""
    except OSError:
        print("No microphone available or no default input device detected.")
        return ""
    except sr.WaitTimeoutError:
        print("Listening timed out.")
        return ""


def speechtx(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    if voices:
        engine.setProperty('voice', voices[0].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 150)
    engine.say(x)
    engine.runAndWait()


if __name__ == '__main__':
    first_command = sptext()

    if first_command and "hey siri" in first_command:
        while True:
            data1 = sptext()
            if not data1:
                continue

            if "your name" in data1:
                speechtx("my name is siri")
            elif "how old are you" in data1:
                speechtx("i am 15 minutes old")
            elif "now time" in data1:
                current_time = datetime.datetime.now().strftime("%I:%M %p")
                speechtx(current_time)
            elif "youtube" in data1:
                webbrowser.open("https://www.youtube.com/")
            elif "joke" in data1:
                joke_1 = pyjokes.get_joke(language='en', category='neutral')
                speechtx(joke_1)
            elif "exit" in data1:
                speechtx("thank you sir")
                break
            else:
                speechtx("command not recognized")
    else:
        print("wrong command")