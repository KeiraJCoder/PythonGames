import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[28].id)
engine.say("Dzien Dobry")

engine.runAndWait()