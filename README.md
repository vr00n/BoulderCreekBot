# BoulderCreekBot
https://twitter.com/BoulderCreekBot

## WHAT
An automated twitter bot that reports the daily discharge volume of the Boulder Creek at North 75th Street, Boulder, CO. Source data is located at: https://waterdata.usgs.gov/co/nwis/uv?cb_00060=on&cb_00065=on&format=gif_default&site_no=06730200&period=45&begin_date=2018-03-21&end_date=2018-05-05

## WHY
- Code for Boulder Boulder Startup week Workshop.
- Monitoring Creek discharge relative to historical discharge volumes can be a proxy for available water in the region.
- Twitter Bots are fun.

## HOW
1. [Install Python here - preferably 2.7](https://www.python.org/downloads/mac-osx/)
2. git clone this repo
3. `pip install tweepy` + `pip install requests`
4. Create a dummy Twitter account. For this to work, you need to associate your phone number with your Twitter account.
5. Go to `apps.twitter.com` and click on 'Create New App ' button
6. Fill out details like so and hit `Create you Twitter Application`.
![image](https://user-images.githubusercontent.com/4397663/40180231-8ddd7aec-59a3-11e8-98c4-5cf0960ce2a8.png)
7. You will now have your Application Key/Secret.
8. Create your Access Key/Secret.
![image](https://user-images.githubusercontent.com/4397663/40180395-f3519cfa-59a3-11e8-8759-191026f10539.png)
9. Fill out `secrets.py` with App/Access Key/Secrets information.
10. `python bot.py {number of days you want to look back, max 120}`
11. Tweak as per desire.


## WHEN 
Saturday, My 19th

## Who
varun@codeforboulder.org
