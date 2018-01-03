# tweepy will allow us to communicate with Twitter, time will allow us to set how often we tweet
import tweepy, time
import weather_status
from datetime import datetime
from threading import Timer

current_time=datetime.today() #get current date and time

CONSUMER_KEY = 'cEmLATBDtoPhdqX9wYlJIn9e2'
CONSUMER_SECRET = 'fdMaPGTZOFQyQ9PpZ6Cs58jQDCE5AyEo4hx5sQul8Pk5oAO2nW'
ACCESS_TOKEN = '947007559600189440-6fIju6enjKJTfeMEnl3kebSMeKexhES'
ACCESS_SECRET = 'L1zAL3Y3EvQZB004rRAcVRcDPkpprj3ArsgnyZS65nGbF'


# configure our access information for reaching Twitter
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

# access Twitter
api = tweepy.API(auth)

def getMin():
	if current_time.minute == 0:
		return "00"
	else:
		return str(current_time.minute)
def getHour():
	if current_time.hour > 12:
		return str(current_time.hour - 12)
	else:
		return str(current_time.hour)
def get_am_pm():
	if current_time.hour >= 12:
		return "pm"
	else:
		return "am"

#get weather status
weather = weather_status.status()
#add hashtag
hashtag="\n#albanyweather"
date = str(current_time.month) + "/" + str(current_time.day) + " "
hour = getHour()
minute = getMin()
am_pm = get_am_pm()

def tweetWeather():
	try:
		api.update_status(date + hour + ":" + minute + " " + am_pm + " update:\n" + weather + hashtag)
	except tweepy.TweepError , err:
		print(err)
	print("All done tweeting!")