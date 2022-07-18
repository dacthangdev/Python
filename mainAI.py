from base64 import encode
from email.mime import audio
from logging import shutdown
from logging.config import listen
import os
import time
import webbrowser
import playsound
from gtts import gTTS
import speech_recognition
import pyttsx3
from datetime import date,datetime
import requests, json
import wikipedia
import random

robot_mouth = pyttsx3.init()
robot_ear = speech_recognition.Recognizer()
robot_brain = ""
i = 0

# AI weather
def weather(city_name):
    api_key = "41aff991be2645a2f3bf162364a3f06d"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key + "&q=" +city_name
    response = requests.get(complete_url)
    x = response.json()
    if x["cod"] != "404":
        y = x["main"]
        current_temperature = int(y["temp"] - 271.15) # trừ đi độ K
        current_pressure = y["pressure"]
        current_humidity = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]
        robot_brain = "Now is :" + str(weather_description) + ", Temperature is :" + str(current_temperature) +", Pressure is:" + str(current_pressure)+ ", Humidity is:" +str(current_humidity)+ "%"
    else:
        robot_brain = "Not found the city you say."
    return robot_brain

# Câu trả lời từ wikipedia

def wiki_search(input):
    try:
        robot_brain = wikipedia.summary(str(input), sentences=1)
    except:
        robot_brain = "Not found"
    return robot_brain

# AI listen
def input_listen():
    with speech_recognition.Microphone() as mic:
        audio = robot_ear.record(mic, duration=3)
        robot_ear.adjust_for_ambient_noise(mic)
        try:
            you = robot_ear.recognize_google(audio)
        except:
            you = ""
        return you
# AI speak
def output_voice(robot_brain):
    robot_mouth.say(robot_brain)
    robot_mouth.runAndWait()
# AI start cc
def startCoccoc():
    global run
    
    output_voice('starting Coccoc')        #dòng này có cũng được không có cũng không sao :v

    os.startfile(r'C:\Users\HP\AppData\Local\CocCoc\Browser\Application\browser.exe')
    run = False

    # play some music 
def playmusic():
    global run
    music_dir = 'D:\Python\RobotAI\Music'          
    songs = os.listdir(music_dir)
    os.startfile(os.path.join(music_dir,songs[0]))
    run = False
# user speak
while i < 3:
    with speech_recognition.Microphone() as mic:
        print("Robot: I'm listening")
        audio = robot_ear.record(mic, duration=5)
        robot_ear.adjust_for_ambient_noise(mic)
    print("Robot:...")

    try:
        you = robot_ear.recognize_google(audio)
    except:
        you = ""
    print("You:" + you)
        
    
    # AI understand 
    robot_brain = ""
    if you == "":
        i+=1
        robot_brain = "I can't hear anything. Say again !"

    elif "hello" in you:
        robot_brain = "hello, Moon"

    elif "today" in you:
        today = date.today()
        robot_brain = today.strftime("%B %d, %Y")

    elif "time" in you:
        now = datetime.now()
        robot_brain = now.strftime("%H:%M:%S")
    
    elif "browser" in you:
        startCoccoc()
        break
    
    elif "music" in you :
        playmusic()
    elif "weather" in you:
        robot_brain = "Say name of the city"
        print("robot: "+robot_brain)

    
        output_voice(robot_brain)

        you = input_listen()

        
        print("You search:" + you)
        robot_brain = weather(you)
        if "Not found" in robot_brain:
            you = input("Robot: Try input here: ")
            robot_brain = weather(you)
    elif "Wikipedia" in you:
        robot_brain = "What do you want to search ?"
        print("Robot: "+ robot_brain)

        output_voice(robot_brain)

        you  = input_listen()

        print("You are searching: "+ you)
        
        robot_brain = wiki_search(you)
        

        if  "Not found" in robot_brain:
            you = input("Robot: Try input here: ")
            robot_brain   = wikipedia.summary(str(you), sentences=1)

    elif "joke" in you:
        with open('joke.txt','r', encoding= "utf8") as file:
            jokelist = file.read().split('\n*')
        
        joke = str(random.choice(jokelist))
        robot_brain = joke

    elif "YouTube" in you:
        webbrowser.open('https://www.youtube.com/', new= 1)
        robot_brain = "Open youtube"
        output_voice(robot_brain)
        break
    
    elif "Facebook" in you:
        webbrowser.open('https://www.facebook.com/', new= 1)
        robot_brain = "Opening Facebook"
        output_voice(robot_brain)
        break
    
    elif "1 minutes" in you:
        time.sleep(60)

    elif "Shut down" in you:
        os.system('shutdown -s')

    elif "restart" in you:
        os.system('shutdown -r')

    elif "bye" in you:
        robot_brain = "bye moon"
        print("Robot: "+ robot_brain)
        output_voice(robot_brain)
        break
    else:
        robot_brain = "Thank you ! How are you today ?"

    print("Robot: "+ robot_brain)
    # robot speak


    output_voice(robot_brain)
