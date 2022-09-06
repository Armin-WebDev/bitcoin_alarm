
import sys
import keyboard
import pyttsx3
import cryptocompare
import time
from playsound import playsound
from threading import Thread 

class BitcoinAlarmer:
    def __init__(self,low_threshold,high_threshold):
        self.low_threshold = low_threshold
        self.high_threshold = high_threshold
        self.current_price = None
        self.engine = None
        self.x = Thread(target=self.get_price)
        self.x.start()

    def get_price(self):
        self.current_price = cryptocompare.get_price('BTC','USD')['BTC']['USD']
        print(self.current_price)
        self.y= Thread(target=self.alarm)
        self.y.start()
        while True:
            try:
                self.current_price = cryptocompare.get_price('BTC','USD')['BTC']['USD']
            except:
                pass
            #print(self.current_price)
            time.sleep(5)

    
    def alarm(self):
        while True:
            if keyboard.is_pressed("esc"):
                print('you pressed esc')
                sys.exit()
            if self.current_price > int(self.high_threshold):
                self.sound = '/Githubprojects/bitcoin_alarmer/up.wav'
                playsound(self.sound)
                self.engine = pyttsx3.init()
                self.engine.say('Bitcoin price is higher then  %s'% self.high_threshold)
                self.engine.runAndWait()
                self.engine = None
            elif keyboard.is_pressed("esc"):
                print('you pressed esc')
                sys.exit()
            elif self.current_price < int(self.low_threshold):
                playsound(self.sound)
                self.engine = pyttsx3.init()
                self.engine.say('Bitcoin price is lower then  %s'% self.low_threshold)
                self.engine.runAndWait()
                self.engine = None
            else:
                pass               

    

#high_threshold =  input('please enter the high threshold : ')
#low_threshold = input('please enter the low threshold : ')
#obj = BitcoinAlarmer(19800,19700)






