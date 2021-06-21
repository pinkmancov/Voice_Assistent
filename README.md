# Voice_Assistent

# Introduction

This small application was created to show how the "speech_recognition" + "pyttsx3" library works. \

Also, to get the weather, a small API module was created using the "OWM" library, \ 
for its work you will need a little study of the official documentation and the creation of a config.json file and your API key. \

# Demo/how to use

To work, just run the application, wait for the message "Слушаю.." in the terminal, \ 
then ask the predefined command "Который час / Какая погода". \
The application will automatically detect your location by IP and select the desired city. \

# Installing from Terminal

mkdir Projects \
cd Projects \
git clone https://github.com/pinkmancov/voice_assistent.git \
python3 -m venv venv \
source venv/bin/activate \
pip install -r requirements.txt 
