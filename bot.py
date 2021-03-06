import tweepy
import requests
from secrets import *
import datetime
from datetime import date
import sys
import os

period=sys.argv[1]

#Establish dates
today = date.today()
end_date = today.strftime('%Y%m%d')
d = today - datetime.timedelta(days=int(period))
from_date = d.strftime('%Y%m%d')

#Establish URL endpoints. You need to hit the usgs_url so that the img_url becomes available.
usgs_url="https://waterdata.usgs.gov/co/nwis/uv?cb_00060=on&cb_00065=on&format=gif_default&site_no=06730200&period="+str(period)+"&begin_date="+str(d)+"&end_date="+str(today)
img_url1="https://natwebvaww01.er.usgs.gov/nwisweb/data/img/USGS.06730200.211031.00060.."+from_date+"."+end_date+".log.0.p50.gif"
img_url2="https://natwebcaww01.wr.usgs.gov/nwisweb/data/img/USGS.06730200.211031.00060.."+from_date+"."+end_date+".log.0.p50.gif"
r = requests.get(usgs_url, timeout=None)
r2 = requests.get(img_url2, timeout=None)
print "ImageSize: ",len(r2.content)
if len(r2.content) < 7000:
 print "Trying using alternate image_url"
 r2 = requests.get(img_url1, timeout=None)
else:
 print "Image good"

print img_url1
print img_url2
print usgs_url

#Download image locally
filename='BoulderStream.gif'
open(filename, 'wb').write(r2.content)


#create an OAuthHandler instance. Twitter requires all requests to use OAuth for authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

 #Construct the API instance
api = tweepy.API(auth) # create an API object
status_txt="TODAYs Boulder Creek Bot - looking back "+str(period)+" days via USGS - "+usgs_url
#print status_txt
try:
 api.update_with_media(filename,str(status_txt))
except tweepy.error.TweepError as e:
 print ("Trying 2nd time")
 try:
  api.update_with_media(filename,str(status_txt))
 except tweepy.error.TweepError as f:
  print ("Trying 3rd time")
  try:
   api.update_with_media(filename,str(status_txt))
  except tweepy.error.TweepError as g:
   print ("Trying 4th time")
   try:
    api.update_with_media(filename,str(status_txt))
   except tweepy.error.TweepError as h:
    print (h)

