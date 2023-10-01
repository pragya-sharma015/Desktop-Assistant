import pyttsx3
import speechRecognition as sr
import wikipedia


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

# function foe take command

def takeCommand():        #It takes microphone input from the user and returns string output
   r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

        #for exception
  try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

    except Exception as e:
         print("Say that again please...")  
        return "None" 
    return query

    wishme()

     # Logic for executing tasks based on query


    while True:
  
        query = takeCommand().lower() #Converting user query into lower case

        git # For wikipedia

        if 'wikipedia' in query:  
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia")
            print(results)
            speak(results)

