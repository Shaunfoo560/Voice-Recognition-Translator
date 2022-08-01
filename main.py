import os
import speech_recognition
from playsound import playsound
from gtts import gTTS
from google_trans_new import google_translator

# Enter the ISO-639-1 language code that you would like to translate to in between the '' below. (e.g. 'fr' for french)
translateTo = ''

while True:

    with speech_recognition.Microphone() as source:

        print("Say what you want to be translated! Say 'stop' to terminate the program!")
        recording = speech_recognition.Recognizer().listen(source)

        try:
            transcript = speech_recognition.Recognizer().recognize_google(recording)
            if transcript == "stop":
                print("Come back anytime!")
                break
            print("Original: " + transcript)

        except speech_recognition.UnknownValueError or speech_recognition.RequestError:
            print("Please repeat yourself clearly into the microphone!")

        translated = google_translator().translate(transcript, lang_tgt=translateTo)
        print("Translation: " + translated)

        temp = gTTS(translated, lang=translateTo)
        temp.save("temp.mp3")
        playsound("temp.mp3")
        os.remove("temp.mp3")