import time
#Speech START

import pyttsx3
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-40)
engine.say('Hey Ankush ')


engine.say('I am Jarvis')

time.sleep(5)

engine.say('Which song would you like to hear')
#engine.say('I\'m')


engine.runAndWait()




#Speech END



#Speech to Text Start
import speech_recognition as sr
import string
import re


r=sr.Recognizer()
with sr.Microphone() as source:
    print('Speak anything: ')
    audio=r.listen(source)
    try:
        text=r.recognize_google(audio)
        print('You said:{}'.format(text))
    except:
        ('Sorry could not recognise your voice')
        

print(text)
#Speech to text End



# Program searches the song in the location txt file  
# using regular expression
#Problem :Now I have to extract the location of the song

import re

f = open("flac_location.txt", "r")

user=f.read()

#user=input('Enter a string: \n')
#search=input('Enter search string : \n').lower()
search=text
#Search and Play START

raw=re.compile(search)

matches=raw.finditer(user.lower())
raw=raw.split('\n')

for match in matches:
    print(match)
    new=user[:match.span()[1]]
    print(new)
    print("")
    print("")
    
    i=match.span()[1]
    while(user[i]!=':'):
      i=i-1
    location='d'+user[i:match.span()[1]]
    print('d'+user[i:match.span()[1]])
print(location)    
    
from pygame import mixer  # Load the popular external library

mixer.init()
mixer.music.load(location+".flac")
mixer.music.play()

#Search and play END







