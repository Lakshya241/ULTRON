import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import random
import os
import tkinter as tk
from tkinter import messagebox
import threading

# Voice assistant code (same as before)
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir")
    else:
        speak("Good Evening Sir")
    speak("I am Ultron, How may I help you?")

def takecommand():
    # this function will take microphone input from the user
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        return query.lower()
    except Exception as e:
        print("Say that again please...")
        return "None"
        
def tell_good_joke():
    jokes = [
        "Why don't skeletons fight each other? They don't have the guts.",
        "I told my wife she was drawing her eyebrows too high. She looked surprised.",
        "Why don/'t scientists trust atoms? Because they make up everything!"
    ]
    joke = random.choice(jokes)
    speak(joke)
    
def tell_dark_joke():
    dark_jokes = [
        "Why don/'t graveyards have 4G service? Because they/'re full of dead zones.",
        "I have a joke about a broken pencil... but it/'s pointless.",
        "I/'m reading a book about anti-gravity. It/'s impossible to put down!"
    ]
    dark_joke = random.choice(dark_jokes)
    speak(dark_joke)

def execute_command(query):
    if 'wikipedia' in query:
        speak("Searching Wikipedia...")
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=7)
        speak("According to Wikipedia")
        speak(results)
    elif 'open youtube' in query:
        speak("Opening YouTube")
        webbrowser.open("youtube.com")
    elif 'search from google' in query:
        speak("Searching Google...")
        query = query.replace("search google", "")  # Extract the search term
        search_url = f"https://www.google.com/search?q={query}"
        speak("here is the result what are you looking for")
        webbrowser.open(search_url)  # Open the search results in the browser
        
    elif 'open stackoverflow' in query:
        speak("Opening StackOverflow")
        webbrowser.open("stackoverflow.com")
    elif 'open chatgpt' in query:
        speak("Opening ChatGPT")
        webbrowser.open("https://chat.openai.com")
    elif 'open notepad' in query:
        speak("Opening Notepad")
        os.system("notepad.exe")
    elif 'play music' in query:
        music_dir = 'C:\\Users\\santa\\Music'
        songs = os.listdir(music_dir)
        song = songs[random.randint(0, len(songs)-1)]
        os.startfile(os.path.join(music_dir, song))
    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir, the time is {strTime}")
    elif 'the date' in query:
        strDate = datetime.datetime.now().strftime("%Y-%m-%d")
        speak(f"Sir, the date is {strDate}")
    elif 'open gmail' in query:
        speak("opening gmail")
        webbrowser.open("gmail.com")
    elif 'open instagram' in query:
        speak("opening instagram")
        webbrowser.open("instagram.com")
    elif 'thank you' in query:
        speak("You're welcome, Sir")
    elif 'goodbye' in query:
        speak("Goodbye Sir, have a nice day")
        exit()
    elif 'tell me a good joke' in query:
        tell_good_joke()
    elif 'tell me a dark joke' in query:
        tell_dark_joke()
    elif 'tell me a random joke' in query:
        random_jokes = [
            "I told my computer I needed a break, and now it won't stop sending me beach wallpapers.",
            "Why did the scarecrow win an award? Because he was outstanding in his field!",
            "I used to play piano by ear, but now I use my hands."
        ]
        joke = random.choice(random_jokes)
        speak(joke)
    elif 'open whatsapp' in query:
        speak("Opening whatsapp")
        webbrowser.open("web.whatsapp.com")
    elif 'Shut down the system' in query:
        speak("stutting down your system")
        os.system("shutdown /s /t 1")
    elif'restart the system'in query:
        speak("restarting your system")
        os.system("shutdown /r /t 1")
    elif 'lock the system' in query:
        speak("locking the system")
        os.system("rundll32.exe user32.dll,lockworkstation")
# GUI using Tkinter
class VoiceAssistantApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ultron Voice Assistant")
        self.root.geometry("400x400")
        self.root.configure(bg="#2C3E50")

        self.label = tk.Label(self.root, text="Ultron Voice Assistant", font=("Helvetica", 18), bg="#2C3E50", fg="white")
        self.label.pack(pady=20)

        self.command_label = tk.Label(self.root, text="Command: ", font=("Helvetica", 12), bg="#2C3E50", fg="white")
        self.command_label.pack(pady=10)

        self.command_entry = tk.Entry(self.root, font=("Helvetica", 12), width=30)
        self.command_entry.pack(pady=10)

        self.speak_button = tk.Button(self.root, text="Speak", font=("Helvetica", 14), command=self.speak_command, bg="#3498DB", fg="white", width=15)
        self.speak_button.pack(pady=10)

        self.execute_button = tk.Button(self.root, text="Execute Command", font=("Helvetica", 14), command=self.execute_from_gui, bg="#2ECC71", fg="white", width=15)
        self.execute_button.pack(pady=10)

        self.quit_button = tk.Button(self.root, text="Quit", font=("Helvetica", 14), command=self.quit, bg="#E74C3C", fg="white", width=15)
        self.quit_button.pack(pady=10)

    def speak_command(self):
        command = self.command_entry.get().lower()
        if command != "":
            threading.Thread(target=execute_command, args=(command,)).start()
        else:
            messagebox.showwarning("Input Error", "Please enter a command.")

    def execute_from_gui(self):
        command = takecommand()  # Get command using the voice assistant
        if command != "":
            threading.Thread(target=execute_command, args=(command,)).start()
        else:
            messagebox.showwarning("Voice Error", "Please try again.")
    def quit(self):
        self.root.quit()
def main():
    wishMe()
    root = tk.Tk()
    app = VoiceAssistantApp(root)
    root.mainloop()
if __name__ == "__main__":
    main()