import pyttsx3

#initialized the engine
engine = pyttsx3.init()
text ='Data class, related to ml'

engine.say(text)
engine.runAndWait()