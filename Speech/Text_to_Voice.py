import pyttsx3
speech=pyttsx3.init()
voices=speech.getProperty('voices')
info="Attitude is a choice. Happiness is a choice. Optimism is a choice. Kindness is a choice. Giving is a choice. Respect is a choice. Whatever choice you make makes you. Choose wisely."
speech.setProperty("voice",voices[1].id) #female voice
speech.setProperty("rate",100)
speech.setProperty("volume",1)
speech.save_to_file(info,"python.mp3")
speech.runAndWait()
print('success')