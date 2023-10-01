import pyttsx3

engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices') 
engine.setProperty('voice', voice[0].id)
 
 #function for voice command

def speak(audio):
engine.say(audio) 
engine.runAndWait()

# function for wish command

def wishme():
hour = int(datetime.datetime.now().hour)
if hour>=0 and hour<12:
    speak("Good Morning!!")
else if hour>=12 and hour<18:
    speak("Good Afternoon!!")
else:
    speak("Good Evening!!")

Speak("I am your personal assistant Mam , please tell me how may I help you")
 