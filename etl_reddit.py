
import pandas as pd 
import s3fs
import json
from datetime import datetime
import requests
import variables as vars


def reddit_extract_data():

    headers = vars.request_headers

    urls = vars.reddit_urls

    list_dfs = list()

    for url in urls:
        response = requests.get(url, headers = headers).json()

        response = response['data']['children']

        sub_ids = [sub_data['data']['subreddit_id'] for sub_data in response]
        sub_reddits = [sub_data['data']['subreddit'] for sub_data in response]
        user_ids = [sub_data['data']['author'] for sub_data in response]
        text = [sub_data['data']['selftext'] for sub_data in response]
        sub_ups = [sub_data['data']['ups'] for sub_data in response]
        sub_utc = [datetime.utcfromtimestamp(sub_data['data']['created']) for sub_data in response]
         
        data = list(zip(sub_ids, sub_reddits, user_ids, text, sub_ups, sub_utc))

        sub_reddit_df = pd.DataFrame(data, columns = ['id', 'sub_reddit',  'user_id', 'text' ,'sub_ups', 'creation_utc'])

        list_dfs.append(sub_reddit_df)

    df = pd.concat(list_dfs)
    df.reset_index(inplace = True, drop = True)

    # df.to_csv("s3://reddit-etl-data/cloudcomputing_Devops_reddit_data.csv", index = False)
    df.to_csv('/Users/zamar/Downloads/test.csv', index = False)

reddit_extract_data()


