# Indio Picaro RaspberryPi Project 

This project uses a actuator and a lsd screen to manipulate a typical chilean artisan figure. It's just a funny project I wanted to do for a long time.

The actuator is handled by a L298 relay connected to the PI and it creates a small server using Flask to remotely control the actuator state and screen text
The screen is a DFRobot_RGBLCD1602 32 char model.

![IMG_1569](https://github.com/tsunamas/indiopicaro/assets/3854538/514d2a55-9779-492d-8650-9d105d658bb4)



## Installation

1. Pull the contents of the repo directly on the raspberry pi
2. CD into the directory `indiopicaro`
3. Run `pip install -r requirements.txt`
4. Run `python app.py`
