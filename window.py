
import sys
import time
import keyboard
from threading import Thread
from tkinter import font
import BTC_alarm
from tkinter import *
import re


class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        x = Thread(target=self.get_price)
        x.start
        #self.config(bg='C6E7C8')
        self.title('Bitcoin Alarmer')
        self.geometry('610x500')
        self.resizable(width=False,height=False)
        self.bg = PhotoImage(file = "image3.png")
        Label(self,image=self.bg,).place(x =-10, y = 330)
        self.price_window = Label(self,text="Current Bitcoin price is : " , fg='black',font=("Lucida Console",11))
        self.price_window.pack()
        Button(self,text='Get the Price',width=12,bd=3,command=self.get_price,bg='lightgreen').pack(pady=5)
        Label(self,text="").pack(pady=20)
        Label(self,text="please enter the \"HIGH\" threshold ", font=("Lucida Console",11)).pack()
        self.high = Entry(self,width=26)
        self.high.pack()
        Label(self,text="please enter the \"LOW\" threshold ",font=("Lucida Console",11)).pack(pady=5)
        self.low = Entry(self,width=26)
        self.low.pack()
        Button(self,text='Set Alarm',width=10,bd=3,command=self.set_alarm,bg='lightgreen').pack(pady=10)
        self.alert = Label(self)
        self.alert.pack()
        #Label(self,text="").pack(pady=25)
        self.cancel = Label(self,text="",font=("Lucida Console",11))
        self.cancel.pack(pady=40)
        #self.cancel_btn = Button(self,text='',width=0,bd=0,command=self.cancel_alarm)
        #self.cancel_btn.pack()


    def get_price(self):
        self.price = BTC_alarm.cryptocompare.get_price('BTC','USD')['BTC']['USD']
        self.price_window.config(text="Current Bitcoin price is : {}".format(self.price))
        #a = Thread(target=self.set_alarm)
        #a.start()

    def set_alarm(self):
        self.high_threshold = self.high.get()
        self.low_threshold = self.low.get()
        if self.high_threshold == '' or self.low_threshold == '':
            self.alert.config(text="Please fill the boxes to set the alarm".format(self.high_threshold,self.low_threshold),font=("Lucida Console",11),fg='#EA352E')
        elif re.search("^\d.+",self.high_threshold) == None or re.search("^\d.+", self.low_threshold) == None:
            self.alert.config(text="The given value must be a number".format(self.high_threshold,self.low_threshold),font=("Lucida Console",11),fg='#EA352E')
        elif self.high_threshold != '' and self.low_threshold != '':
            self.alert.config(text="Alarm set successfully at {} and {}".format(self.high_threshold,self.low_threshold),font=("Lucida Console",11),fg='green')
            self.cancel.config(text="Hold \"Esc\" to cancel/silent the Alarm",font=("Lucida Console",11),fg="#F87E7D")
            if __name__ == "__main__":
                BTC_alarm.BitcoinAlarmer(self.low_threshold,self.high_threshold)
                a = Thread(target=self.silent)
                a.start()
    def silent(self):
        while True:
            if keyboard.is_pressed('esc'):
                    time.sleep(5)
                    self.cancel.config(text="alarm stopped successfully",font=("Lucida Console",11),fg="#5FB3F9")

if __name__ == "__main__":
    app = App()
app.mainloop()