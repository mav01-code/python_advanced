import pyttsx3
e=pyttsx3.init()
e.setProperty('rate',150)
e.setProperty('Volume', 3)

text=input()
e.say(text)
e.runAndWait()