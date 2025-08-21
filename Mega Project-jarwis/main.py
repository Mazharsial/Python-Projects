import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import sys

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.say("Hello, I am Jarvis. How can I help you?")
engine.runAndWait()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def listen_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
        except sr.UnknownValueError:
            print("Sorry, I did not catch that.")
            return ""
        except sr.RequestError:
            print("Network error.")
            return ""
        return command.lower()

def run_jarvis():
    command = listen_command()

    if 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk(f"The time is {time}")

    elif 'date' in command:
        date = datetime.date.today().strftime('%B %d, %Y')
        talk(f"Today's date is {date}")

    elif 'play' in command:
        song = command.replace('play', '').strip()
        talk(f"Playing {song}")
        pywhatkit.playonyt(song)

    elif 'search' in command:
        search_query = command.replace('search', '').strip()
        talk(f"Searching Google for {search_query}")
        pywhatkit.search(search_query)

    elif 'hello' in command:
        talk("Hello! Nice to meet you.")

    elif 'stop' in command:
        talk("Goodbye!")
        sys.exit()

    else:
        talk("Sorry, I don't understand that command.")

# Run continuously
while True:
    run_jarvis()
