import os
import requests
import pandas as pd
from sqlalchemy import create_engine


engine = create_engine(os.getenv('POSTGRESDB_URI'))
tweets = pd.read_sql_table('tweets_df', engine, index_col=0 )
tweets = tweets.iloc[0]
print(tweets)

data = {'text': f'{tweets}'}
webhook_url= os.getenv('SLACK_WEBHOOK_URL')
requests.post(url=webhook_url, json=data)