import tweepy
import requests
from secrets import *
import datetime
from datetime import date
import sys

period=sys.argv[1]

#Establish dates
today = date.today()
end_date = today.strftime('%Y%m%d')
d = today - datetime.timedelta(days=int(period))
from_date = d.strftime('%Y%m%d')

#Establish URL endpoints. You need to hit the usgs_url so that the img_url becomes available.
usgs_url="https://waterdata.usgs.gov/co/nwis/uv?cb_00060=on&cb_00065=on&format=gif_default&site_no=06730200&period="+str(period)+"&begin_date="+str(d)+"&end_date="+str(today)
img_url="https://natwebvaww01.er.usgs.gov/nwisweb/data/img/USGS.06730200.211031.00060.."+from_date+"."+end_date+".log.0.p50.gif"
r = requests.get(usgs_url)
r2 = requests.get(img_url)

#Download image locally
open('BoulderStream.gif', 'wb').write(r2.content)

#create an OAuthHandler instance. Twitter requires all requests to use OAuth for authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

 #Construct the API instance
api = tweepy.API(auth) # create an API object
status_txt="TODAYs Boulder Creek Bot - looking back "+str(period)+" days via USGS - "+usgs_url
api.update_with_media('BoulderStream.gif',str(status_txt))
