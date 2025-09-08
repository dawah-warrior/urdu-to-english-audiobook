from transformers import pipeline
from gtts import gTTS
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

# Load translation pipeline (small, efficient model)
translator = pipeline("translation", model="Helsinki-NLP/opus-mt-ur-en")

def translate_text(text):
    return translator(text, max_length=400)[0]['translation_text']

def text_to_speech(text):
    tts = gTTS(text=text, lang="en")
    mp3_path = "audiobook.mp3"
    tts.save(mp3_path)
    return mp3_path

def save_to_drive(filename, content, is_file=False):
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()
    drive = GoogleDrive(gauth)

    if is_file:
        file = drive.CreateFile({'title': filename})
        file.SetContentFile(content)
    else:
        file = drive.CreateFile({'title': filename})
        file.SetContentString(content)

    file.Upload()