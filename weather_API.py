from pyowm import OWM
from pyowm.utils.config import get_config_from

config_dict = get_config_from('configfile.json')
# Enter your api key OWM
owm = OWM('*API_KEY', config_dict)
mgr = owm.weather_manager()


# We get the temperature in degrees Celsius
def weather(city):
    observation = mgr.weather_at_place(city)
    w = observation.weather
    temp = w.temperature('celsius')['temp']
    print(str(round(temp)))
    return round(temp)


# Get weather detailed status
def status(city):
    observation = mgr.weather_at_place(city)
    w = observation.weather
    status = w.detailed_status
    print(status)
    return status
