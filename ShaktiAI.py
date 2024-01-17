import openai
from apikey import api_data
import pyautogui
import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import wikipedia
import webbrowser
import pywhatkit as kit
import sys
import time
import requests
from bs4 import BeautifulSoup
import subprocess

from requests import get
openai.api_key=api_data

completion=openai.Completion()

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def TakeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        r.pause_threshold = 1
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=5)  # Adjust the timeout and phrase time limit
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
            return query.lower()
        except sr.WaitTimeoutError as e:
            print("Timeout occurred. No speech detected within the specified time.")
            return "None"
        except Exception as e:
            print(f"Say that again: {str(e)}")
            return "None"

# def TakeCommand():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("listning.....")
#         r.pause_threshold = 1
#         audio = r.listen(source, timeout=1,phrase_time_limit=4)

#     try:
#         print("Recognising...")
#         query = r.recognize_google(audio, language='en-in')
#         print(f"user said: {query}\n")
#     except Exception as e:
#         #speak("say again please")
#         return "None"
#     query = query.lower()
#     return query
def Chatmode():
        speak("welcome to Chatmode sir.")
        while True:

                def Reply(question):
                    prompt=f'Vishal: {question}\n Shakti: '
                    response=completion.create(prompt=prompt, engine="text-davinci-002", stop=['\Vishal'], max_tokens=200)
                    answer=response.choices[0].text.strip()
                    return answer
                query=TakeCommand().lower()
                ans=Reply(query)
                print(ans)
                speak(ans)
                if "exit" in query or "close" in  query:
                     speak("exited sir")
                     break 
                
def wish():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<=12:
        speak("good morning")
    elif hour>=12 and hour<=18:
        speak("good afternoon")
    else:
        speak("good evening")
    speak("i am Shakti sir please tell me how can i help you")

def help():
        notepad_help_file = "help.txt" 
        try:
            subprocess.Popen(["hh", notepad_help_file])
        except FileNotFoundError:
            # Handle file not found error
            print("File not found or error opening the help file")
        

def TaskExecution():

    wish()
    while True:
    #if 1:

        query = TakeCommand()
        if "open notepad" in query:
            npath="C:\\Windows\\notepad.exe"
            os.startfile(npath)

        elif "Chat Mode " in query or "chat mod" in query:
            Chatmode()

        elif "play music" in query:
            music_dir = "C:\\Users\\vishal bind\\Desktop\\New folder\\"
            songs = os.listdir(music_dir)
            #rd = random.choice(songs)
            for song in songs:
                if song.endswith('.mp3'):
                    os.startfile(os.path.join(music_dir, song))
            #os.startfile(bpath)
        elif "open command prompt" in query:
            os.system("start cmd")

        elif "help" in query:
            help()
        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam',img)
                k = cv2.waitKey(50)
                if k==27:
                    break;
            cap.release()
            cv2.destroyAllWindows()

        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"your IP address is :{ip}")
            print(ip)
        elif "wikipedia" in query:
            speak("searching wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            speak(results)
            print(results)
        
        
        elif "volume up" in query:
            pyautogui.press("volumeup")

        elif "volume down" in query:
            pyautogui.press("volumedown")

        elif "volume mute" in query or 'mute' in query:
         pyautogui.press("volumemute")

        elif "close app" in query or 'close' in query:
         pyautogui.hotkey('fn','alt','f4')

        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")

        elif "open stackoverflow" in query:
            webbrowser.open("www.stackoverflow.com")

        elif "open google" in query:
            speak("sir , what should i search on google")
            cm = TakeCommand()
            webbrowser.open(f"{cm}")

        elif "send message" in query:
            kit.sendwhatmsg("+919892246353","hello sir..... i am shaktiman",1,25)

        elif "play song on youtube" in query:
            speak("which song do you wants to play")
            cm = TakeCommand()
            kit.playonyt(f"{cm}")

        elif "restart the system" in query:
            speak("sir i am going to restart the system")
            os.system('shutdown /r /t 1')

        elif "shutdown the system" in query:
            speak("sir i am going to shutdowm the system")
            os.system('shutdown /s /t 3')

        elif "hello" in query or "hey " in query:
            speak("Hello sir , how may i help you")
        
        elif "how r u" in query or "how are you" in query:
            speak("I am fine sir, what about you.")

        elif "i am also good" in query or "fine " in query:
            speak("thats's great to here from you.")

        elif "thank you" in query or "thanks" in query or "thank u" in query:
            speak("it's my pleasure sir.")
        
        elif "take screenshot" in query or "take a screenshot" in query :
            speak("sir, please tell me the name for this screenshot file")
            name = TakeCommand().lower()
            speak("please sir hold for a second")
            time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("i am done sir, the screenshot is saved in our main folder.")

        elif "open" in query:
            query = query.replace("open", "")
            query = query.replace("shakti","")
            pyautogui.press("super")
            pyautogui.typewrite(query)
            pyautogui.sleep(2)
            pyautogui.press("enter")
        
        elif "temperature" in query:
            search = "temperature in mumbai"
            url = f"https://www.google.com/search?q={search}"
            r  = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div", class_ = "BNeawe").text
            speak(f"current{search} is {temp}")
        elif "weather" in query:
            search = "temperature in mumbai"
            url = f"https://www.google.com/search?q={search}"
            r  = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div", class_ = "BNeawe").text
            speak(f"current{search} is {temp}")

        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M")    
            speak(f"Sir, the time is {strTime}")

        elif "you can sleep" in query or "sleep now" in query:
            speak("okay sir, i am going to sleep you can call me any time") 
            break

        # elif "no thanks" in query:
        #     speak("thanks for using me sir, have a good day.")
        #     sys.exit()
        #speak("  sir do you have any other work")

if __name__=="__main__":
    while True:
        Permission = TakeCommand()
        if "wake up" in Permission:
            TaskExecution()
        elif "good bye" in Permission:
            speak("thanks for using me sir , have a good day")
            sys.exit()
