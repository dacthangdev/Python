import os
from gtts import gTTS
import playsound


tiengviet  =  gTTS(text = "Xin chào các bờ rô", lang= "vi")
voice_Viet = "wiki.mp3"
tiengviet.save(voice_Viet)
playsound.playsound(voice_Viet, True)
os.remove(voice_Viet)