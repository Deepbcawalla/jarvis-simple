import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import requests
from openai import OpenAI
from gtts import gTTS
import pygame
import os

recognizer =sr.Recognizer()
engine = pyttsx3.init()
newsapi = ""#add news api key

def speak_old (text):
    engine.say(text)
    engine.runAndWait()

def speak(text):
      tts = gTTS(text)
      tts.save('temp.mp3')

      pygame.mixer.init()             
      pygame.mixer.music.load('temp.mp3')          
      pygame.mixer.music.play()
      while pygame.mixer.music.get_busy():                        
          pygame.time.Clock().tick(0.1)
          pygame.mixer.music.unload()
          os.remove("temp.mp3")  

def aiprocess(command):
      client = OpenAI(
            api_key = "",#add openai api key

)
      completion = client.chat.completions.create(
             
             model="gpt-3.5-turbo",
             messages=[
             {
               "role":"system", 
               "content": "you are a virtual assistent name jarvis skilled in genaral task like alexa and google cloud.give short responses"
             },
                    {
                        "role": "user",
                        "content":command
                    }
                ]
            )

      return completion.choices[0].message.content

def processcommand(c):
        if "open google" in c.lower():
                  
                  webbrowser.open("https://google.com")
        elif "open youtube" in c.lower():
                  
                  webbrowser.open("https://youtube.com")
        elif "open instagram" in c.lower():
                  
                  webbrowser.open("https://instagram.com") 
        elif "open facebook" in c.lower():
                  
                  webbrowser.open("https://facebook.com")

        elif c.lower().startswith("play"):
                  song = c.lower().split(" ")[1]
                  link = musiclibrary.music[song]
                  webbrowser.open(link)       
        elif "news" in c.lower():           
               r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}") 
               if r.status_code == 200:  
                 data = r.json()
                 articles = data.get('articles',[])
                 for article in articles:
                       speak(article['title'])
                              
        else:
            output = aiprocess(c)
            speak(output)

if __name__ == "__main__":
       speak("initializing jarvis...")
       while True:
               r = sr.Recognizer()
               print("Recognizing....")

               try:      
                  with sr.Microphone() as source:
                    print("Listening...")
                    audio = r.listen(source,timeout=2, phrase_time_limit=1)                    
                    word = r.recognize_google(audio)
                    if(word.lower()=="jarvis"):
                           speak("bolo deep")
                           
                           with sr.Microphone() as source:
                              print("jarvis Active...")
                              audio = r.listen(source)
                              command = r.recognize_google(audio)
                    processcommand(command)
               except Exception as e:
                print("Error; {0}".format(e))
