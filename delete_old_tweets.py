# https://pushpullfork.com/i-deleted-tweets/
import tweepy
import csv

consumer_key = ''
consumer_secret = ''
access_key = ''
access_secret = ''

def read_csv(file):
    """
    reads a CSV file into a list of lists
    """
    with open(file, encoding = 'utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter = ',')
        rows = []
        for line in reader:
            row_data = []
            for element in line:
                row_data.append(element)
            if row_data != []:
                rows.append(row_data)
    rows.pop(0)
    return(rows)

def oauth_login(consumer_key, consumer_secret):
    """Authenticate with twitter using OAuth"""
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth_url = auth.get_authorization_url()
    verify_code = raw_input("Authenticate at %s and then enter you verification code here > " % auth_url)
    auth.get_access_token(verify_code)
    return tweepy.API(auth)

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)
print("Authenticated as: %s" % api.me().screen_name)

tweets = read_csv('/Users/dinomite/tmp/twitter/tweets.csv')

before_time = '2016'
tweets_marked = [tweet for tweet in tweets if tweet[3][0:4] < before_time]

print(tweets_marked[0])
print(tweets_marked[-1])
print(len(tweets_marked), 'tweets marked for deletion.')

# delete marked tweets by status ID
delete_count = 0
to_delete_ids = [tweet[0] for tweet in tweets_marked]
for status_id in to_delete_ids:
    try:
        api.destroy_status(status_id)
        print(status_id, 'deleted!')
        delete_count += 1
    except:
        print(status_id, 'could not be deleted.')
print(delete_count, 'tweets deleted.')

#tweet = tweets_marked[0]
#print(tweet)
#['8433254323', '', '', '2010-01-31 00:00:00 +0000', '<a href="http://twitter.com" rel="nofollow">Twitter Web Client</a>', "Europe's alcohol belts: http://is.gd/7o1u8", '', '', '', '']
