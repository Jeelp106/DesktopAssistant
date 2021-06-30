import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

def speak(audio):
    engine=pyttsx3.init('sapi5')
    voices=engine.getProperty('voices')
    engine.setProperty("voice",voices[0].id)
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning,jeel")
    elif hour>=12 and hour<=18:
        speak("Good Aftermoon,jeel")
    else:
        speak("Good Evening,jeel")
    speak("I am Jarvis sir,How can i help you sir")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening')
        r.pause_threshold = 0.7
        audio = r.listen(source)
        try:
            print("Recognizing")
            Query = r.recognize_google(audio)
            print("the query is printed='", Query, "'")
        except Exception as e:
            print(e)
            print("Say that again sir")
            return "None"
    return Query
def sendEmail(to,content):
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login("Email","pass")
    server.sendmail("Email",to,content)
    server.close()

if __name__=="__main__":
    clear=lambda :os.system('cls')
    clear()
    wishme()
    # usrname()
    while True:
        query=takeCommand().lower()
        if "wikipedia" in query:
            speak("Searching wikipedia.....")
            query=query.replace("wekipedia","")
            result=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(result)
            speak(result)
        elif "open youtube" in query:
            webbrowser.open("youtube.com")
        elif "open google" in query:
            webbrowser.open("google.com")
        elif "open facebook" in query:
            webbrowser.open("facebook.com")
        elif "open instagram" in query:
            webbrowser.open("instagram.com")
        elif "open stackoverflow" in query:
            webbrowser.open("stackoverflow.com")
        elif "play music" in query:
            music_dir = "path name of this"
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        elif "the time" in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir,The time is {strTime}")
        elif "open vscode" in query:
            codepath=("path name")
        elif "send mail" in query:
            try:
                speak("What should I say")
                content=takeCommand()
                to="youremail@gamil.com"
                sendEmail(to,content)
            except Exception as e:
                print(e)
                speak("Sorry my friend jeel bhai.I am not able to send this Email At the moment")
            pass     #we can use dictionary and we use this
        elif "who made you" in query:
            speak("I have been created by Jeel Patel")
        elif "who i am" in query:
            speak("If you talk then Definately you are humen")
        elif "is love" in query:
            speak("it is a 7th sense that destroy the all the sense")






















