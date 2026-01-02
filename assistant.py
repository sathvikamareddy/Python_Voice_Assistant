import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pywhatkit
import pyjokes

# ==================================================
# SAT - SIMPLE ASSISTANT TOOL

# Language : Python
# ==================================================

# -------------------- VOICE ENGINE SETUP --------------------
engine = pyttsx3.init()
engine.setProperty("rate", 165)

def speak(text):
    """Convert text to speech"""
    print("🤖 SAT:", text)
    engine.say(text)
    engine.runAndWait()

def take_command():
    """Listen to user voice and convert to text"""
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎧 SAT is listening...")
        listener.adjust_for_ambient_noise(source, duration=0.5)
        voice = listener.listen(source)

    try:
        command = listener.recognize_google(voice)
        command = command.lower()
        print("🗣️ You:", command)
        return command
    except sr.UnknownValueError:
        speak("Sorry, I did not understand that.")
        return ""
    except sr.RequestError:
        speak("Network error. Please check your internet connection.")
        return ""

def run_sat():
    """Main assistant logic"""
    speak("Hello! I am SAT, your Python voice assistant. How can I help you?")

    command = take_command()

    if "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {current_time}")

    elif "date" in command:
        current_date = datetime.date.today().strftime("%B %d, %Y")
        speak(f"Today's date is {current_date}")

    elif "who is" in command:
        person = command.replace("who is", "").strip()
        try:
            info = wikipedia.summary(person, sentences=1)
            speak(info)
        except:
            speak("Sorry, I could not find information about that person.")

    elif "play" in command:
        song = command.replace("play", "").strip()
        speak(f"Playing {song} on YouTube")
        pywhatkit.playonyt(song)

    elif "joke" in command:
        speak(pyjokes.get_joke())

    elif "exit" in command or "stop" in command:
        speak("Goodbye! Have a nice day.")
        exit()

    else:
        speak("Sorry, I did not understand that command.")

# -------------------- RUN SAT --------------------
if __name__ == "__main__":
    run_sat()
