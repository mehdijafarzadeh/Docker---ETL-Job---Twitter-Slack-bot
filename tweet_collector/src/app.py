import tweepy
import os
import sqlalchemy
import logging
import pandas as pd
from sqlalchemy import create_engine
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
# from dotenv import load_dotenv
# load_dotenv()

logging.basicConfig(
                    level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='/log/etl.log', filemode='a'
)

logging.debug('start extracting data')

auth = tweepy.OAuthHandler(os.getenv('consumer_key'), os.getenv('consumer_secret'))
auth.set_access_token(os.getenv('access_token'), os.getenv('access_token_secret'))



api = tweepy.API(auth)
print('collect tweets from the twitter api')
cursor = tweepy.Cursor(
    api.search,
    q='noam chomsky -filter:retweets',
    tweet_mode='extended',
    lang='en')


print('transform tweets to a pandas dataframe')

analyzer = SentimentIntensityAnalyzer()
print('sentiment is initiliased')
date = []
user = []
tweet = []
sentiments = []

for status in cursor.items(20):
    date.append(status.created_at)
    user.append(status.user.screen_name)
    tweet.append(status.full_text)

    # sentiment analysis
    sent = analyzer.polarity_scores(status.full_text)
    print(sent)
    # compound score between -1 and 1
    # positive: score > 0.05
    # negative: score < -0.05 
    sentiments.append(sent['compound'])
        
print(sentiments)

logging.debug('start transforming data')

data = {'date': date, 'username': user, 'tweet': tweet, 'sentiment':sentiments}
tweets = pd.DataFrame(data)
print(tweets)
print('tweets DataFrame created')


uri = os.getenv('POSTGRESDB_URI')

engine = create_engine(uri)
try:
    tweets.to_sql('tweets_df', engine, if_exists='replace', index=False)
    print('completed')
except sqlalchemy.exc.OperationalError as e:
        print('Error occured while executing a query {}'.format(e.args))


print('write the dataframe to the postgresql database')
logging.debug('done!')