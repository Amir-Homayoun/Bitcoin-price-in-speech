from gtts import gTTS
from playsound import playsound
import tempfile
import os

import Data_normalizer

text\
    = Data_normalizer.MAIN()
print(text)
def do_tts():
    tts=gTTS(text)
    temp_file=tempfile.NamedTemporaryFile(suffix='.mp3',delete=False)
    tts.save(temp_file.name)
    file_url="file://" + os.path.abspath(temp_file.name)
    temp_file.close()
    return file_url
file_path=do_tts()
playsound(file_path)
os.remove(file_path)