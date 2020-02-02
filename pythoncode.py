import sys
import tweepy
from serial import Serial
from time import sleep

microbitPort = '/dev/tty.usbmodem14102' # USB port address for the micro:bit /dev/ttyACM0 or /dev/tty.usbmodem40132 or similar
microbitBaud = '115200' # Baud for serial communication

from auth_robotgimse import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
#api = tweepy.API(auth, wait_on_rate_limit=True)

ser = Serial(microbitPort, microbitBaud, timeout=3)

print("Lamp ready....")
class CustomStreamListener(tweepy.StreamListener):
    def on_status(self, status):


        if 'coronavirus' in status.text.lower():
            print("coronavirus " + str(status.user.name.encode("utf-8", errors='ignore')))
            ser.write(str.encode("virus" + "\n"))
        if '#coronaviruslampred' in status.text.lower():
            print("Red lamp " + str(status.user.name.encode("utf-8", errors='ignore')))
            ser.write(str.encode("red_lamp" + "\n"))
        if '#coronaviruslampblue' in status.text.lower():
            print("Blue lamp " + str(status.user.name.encode("utf-8", errors='ignore')))
            ser.write(str.encode("blue_lamp" + "\n"))
        if '#coronaviruslampgreen' in status.text.lower():
            print("Green lamp " + str(status.user.name.encode("utf-8", errors='ignore')))
            ser.write(str.encode("green_lamp" + "\n"))
        if '#coronaviruslampyellow' in status.text.lower():
            print("Yellow lamp " + str(status.user.name.encode("utf-8", errors='ignore')))
            ser.write(str.encode("yellow_lamp" + "\n"))
        if '#coronaviruslampblack' in status.text.lower():
            print("Black lamp " + str(status.user.name.encode("utf-8", errors='ignore')))
            ser.write(str.encode("black_lamp" + "\n"))
        if '#coronaviruslampfade' in status.text.lower():
            print("Fade lamp " + str(status.user.name.encode("utf-8", errors='ignore')))
            ser.write(str.encode("fade" + "\n"))

    def on_error(self, status_code):
        print >> sys.stderr, 'Encountered error with status code:', status_code
        return True # Don't kill the stream

    def on_timeout(self):
        print >> sys.stderr, 'Timeout...'
        return True # Don't kill the stream

sapi = tweepy.streaming.Stream(auth, CustomStreamListener())    
sapi.filter(locations=[-27.9,32.7,63.3,73.6]) # make area and numbers on http://boundingbox.klokantech.com/
#sapi.filter(locations=[-51.0,-13.2,174.8,79.8])
