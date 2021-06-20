import speech_recognition as sr
import pyttsx3
import datetime
import weather_API
import requests
from translate import Translator

translator = Translator(to_lang="Russian")

response = requests.get("http://ipinfo.io/json").json()
city = response['city']
time = ['сколько сейчас времени', 'который час', 'подскажи время', 'сколько времени']
time_now = datetime.datetime.now()
weather_dict = ['какая погода', 'какая температура на улице', 'сколько градусов за окном']


def record_volume():
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 0.9)
    r = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        print('Слушаю...')
        engine.say('Слушаю')
        engine.runAndWait()
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    query = r.recognize_google(audio, language='ru-RU')
    text = query.lower()
    print(str(query.lower()))
    if text in time:
        engine.say(f'Сейчас {time_now.hour} часов {time_now.minute} минут')
        engine.runAndWait()
    if text in weather_dict:
        print(str(weather_API.weather(city=city)))
        engine.say('В' + translator.translate(city) + 'сейчас' + str(weather_API.status(city=city))
                   + 'температура на улице' + str(weather_API.weather(city=city)) + 'градуса')
        engine.runAndWait()
    else:
        engine.say('Я вас не понимаю')
        engine.runAndWait()


record_volume()