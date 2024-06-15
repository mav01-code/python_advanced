from gtts import gTTS
import os

user = input("Enter the text you want to convert to speech: ")
language = "en"
speech = gTTS(text=user, lang=language, slow=False) # slow=False means the speaking will not be slowed down
speech.save("user_input.mp3") # Saving the converted audio in a file named user_input.mp3

# Playing the converted file
os.system("start user_input.mp3")
