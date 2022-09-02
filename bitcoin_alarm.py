import pyttsx3
import cryptocompare
import time
from playsound import playsound
btc_info = cryptocompare.get_price('BTC','USD')
current_price = btc_info['BTC']['USD']
print(current_price)
engine = pyttsx3.init()


def alarmer(btc_price=current_price):
    while True:
        if current_price > 19990.00:
            #playsound('/Githubprojects/bitcoin_alarmer/up.wav')
            voices = engine.getProperty('voices') 
            #engine.setProperty('voice', voices[1].id) --> for female voice
            #engine.say('Bitcoin price is as high as %s'% current_price)
            #engine.runAndWait()
            #break
        elif current_price < 19900:
            #playsound('/Githubprojects/bitcoin_alarmer/up.wav')
            voices = engine.getProperty('voices')
            #engine.setProperty('voice', voices[1].id) --> for female voice
            #engine.say('bitcoin price is as high as %s'% current_price)
            #engine.runAndWait()
            #break
        else:
            print(current_price)
        time.sleep(5)

alarmer(current_price)


