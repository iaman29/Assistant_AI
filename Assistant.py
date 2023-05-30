
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes



listener = sr.Recognizer()
engine = pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()
    # engine.say('What can i do for you')

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening......')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command=command.lower()
            if 'alexa' in command:
                command= command.replace('alexa','')
                # print(command)
            
    except:
        print("Sorry I am not Available")
    return command


def run_alexa():
    command=take_command()
    print(command)
    if 'play' in command:
        song=command.replace('play','')
        if 'hey' in command:
            song=command.replace('hey','')    
            talk('playing'+song)
            pywhatkit.playonyt(song)
            
            
            # INT BYE BYE COMMAND I WONNA USE THW BREAK BUT BREAK ONLY EXIT IF ELSE CONDITION
    elif 'bye-bye' or 'bye bye' in command:
        talk('bye bye, see you soon, have a good day ahead')
        talk("Just don't say in next listening command na i will get lost")
        
        
    elif 'time' in command:
        # UPPER TIME COMMAND SHOWS HM FORMAT
        # time=datetime.datetime.now().strftime('%H:%M')
        time=datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is '+ time)
        
        #YOU MAY CHANGE NAME FROM DEVRAJ -> ANY NAME OF FRIEND ETC.   
    elif "who is devraj" in command:
        print("please stop. Don't talk about Devraj Singh")
        talk("please stop. Don't talk about Devraj Singh")
        print("After hearing his name my ears are pissed off")
        talk("After hearing his name my ears are pissed off")
        print("haha")
        talk("haha")
        print("Don't you get it")
        talk("Don't you get it")
        print("by the way he is of my level")
        talk("by the way he is of my level")
        
    elif 'who is' or 'tell me about' in command:
        person= command.replace('who is','')
        person= command.replace('tell me about','')
        info = wikipedia.summary(person,1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry,I have a headache')   
    elif 'are you single' in command:
        talk('I am in relationship with wifi')
    elif 'joke' in command:
        joke1=pyjokes.get_joke()
        talk(joke1)
        print(joke1)
    else:
        talk("Please The Command Again")
        
        
        
        
while True:   
    run_alexa()