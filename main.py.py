import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
import random
import os
import sys
import smtplib
import pyautogui

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
rate=engine.getProperty('rate')
engine.setProperty('rate', rate-5)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning")
    
    elif hour>=12 and hour<18:
        speak("Good afternoon")
    
    else:
        speak("Good evening")
    
    speak("JARVIS IS ONLINE")

def takecommand():
    #It take the audio as input using microphone and convert into text
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold= 1
        audio1= r.listen(source,timeout=20,phrase_time_limit=10)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio1,language='en-in')
        print(f"user said:{query}\n")
    
    except Exception as e:
        speak("couldn't recognize please say it again..")
        return "none"
    return query

def Sendemail(to,content):
    server= smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login("","")
    server.sendmail("shankarkancha57@gmail.com",to,content)
    server.close()

def quit():
    sys.exit()

if __name__=="__main__":
    wishme()
    while True:
        query=takecommand().lower()
        #implementing for logic based on the query
        if "wikipedia" in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        elif "how are you" in query:
            speak("I am fine sir how are you")

        elif "fine" in query:
            speak("that's nice to hear")
        
        elif "open youtube" in query:
            speak("opening youtube")
            webbrowser.open("youtube.com")
        
        elif "open google" in query:
            speak("opening google")
            webbrowser.open("google.com") 

        elif "open stack overflow" in query:
            speak("opening stackoverflow")
            webbrowser.open("stackoverflow.com")

        elif "play music" in query:
            speak("playing your favourite song sir!")
            music_dir="C:\\Users\\Shankar\\Music\\shankar"
            songs=os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,random.choice(songs)))
            
        elif "the time" in query:
            strtime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir the time is {strtime}")
        
        elif "vs code" in query:
            speak("opening vs code sir!")
            codepath="C:\\Users\\Shankar\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif "email" in query:
            try:
                speak("what should I say")
                content= takecommand()
                speak("please give the emailaddress of the person")
                email_name=str(takecommand().lower())
                to=f"{email_name}@gmail.com"
                print(to)
                Sendemail(to,content)
                speak("Email has been sent sir")
            except Exception as e:
                print(e)
                speak("Sorry sir do to some technical issue I can't send the email")

        elif "close" in query:
            pyautogui.hotkey("ctrl","w")

        elif "thanks" in query:
            speak("your welcome sir have a good day")
            quit()
        
        