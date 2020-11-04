import tweepy
from tweepy import OAuthHandler

import time

consumer_token = 'IruhpnVfPGVAh5hBivzW1gAWk'
consumer_secret = 'tYs8rloWpMatyXS0B2CqQwB4c731J7ksvPqFRjKpGGfX5bPDx6'
access_token = '1317324413231005697-MtfX7P8wIhtY0rJ8CNxaJPdmYYiqO5'
access_token_secret = 'veyBSAT6MlV0Qzda82SZwqoZWv0zS9B7CR7RBgHxf2l0y'

auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

QUERY = '#CupidBotDM!'

# Twitter bot setting for liking Tweets
LIKE = True 

# Twitter bot setting for following user who tweeted
FOLLOW = True

# Twitter bot sleep time settings in seconds. For example SLEEP_TIME = 300 means 5 minutes.
# you can decrease it or increase it as you like.Please,use large delay if you are running bot all the time  so that your account does not get banned.

SLEEP_TIME = 300

#number = int(input('Hey John! How many things do you need to do today? '))

#todo_list = []
#print('What do you need to do? ')

#for x in range(0, number):
	#num = input(' ')
	#todo_list.append(num)


#listToStr = ' '.join(map(str, todo_list))


#Write a tweet to push to our Twitter account
#tweet = print("Tweeted: " + listToStr + ' @jooohnrodrigues')
#if listToStr.strip():    
        #api.update_status(status=("To-Do: " + listToStr + ' ' + '@jooohnrodrigues'))

my_file=open('text.txt','r')
file_lines=my_file.readlines()
my_file.close()

for line in file_lines:
    try:
        if line != '\n':
            api.update_status(line)
        else:
            pass
    except tweepy.TweepError as e:
        print(e.reason)
    time.sleep(10)
    

#print("Twitter bot which retweets,like tweets and follow users")
#print("Bot Settings")
#print("Like Tweets :", LIKE)
#print("Follow users :", FOLLOW)

#for tweet in tweepy.Cursor(api.search, q=QUERY).items():
 #   try:
  #      print('\nTweet by: @' + tweet.user.screen_name)
#
 #       tweet.retweet()
  #      print('Retweeted the tweet')
#
 #       screen_name = tweet.user.screen_name
  #      user = api.get_user(screen_name)

        # Favorite the tweet
   #     if LIKE:
     #       tweet.favorite()
    #        print('Favorited the tweet')
      #      api.send_direct_message(user.id_str, "hey")

        # Follow the user who tweeted
        #check that bot is not already following the user
       # if FOLLOW:
        #	if not tweet.user.following:
        #		tweet.user.follow()
         #       print('Followed the user')

       # time.sleep(SLEEP_TIME)

    #except tweepy.TweepError as e:
    #    print(e.reason)

   # except StopIteration:

