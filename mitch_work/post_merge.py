import numpy as np
import pandas as pd
import praw
import time

from subreddit_list import subreddit_list

def post_merge():

    subreddits = subreddit_list()

    # create empty dictionary for subreddit dataframes
    post_dfs = dict.fromkeys(subreddits)

    # fill dictionary with dataframes
    for subreddit in subreddits:
        post_dfs[subreddit]= pd.read_csv('data/posts/'+subreddit+'.csv')

    # build empty merged dictionary

    merge_dfs = {'ID':[], 'Title':[], 'Text':[], 'Author':[], 'OP':[], 'Is Post':[], 'Post Date':[], 'Subreddit':[]}

    for subreddit in subreddits:
        for index, row in post_dfs[subreddit].iterrows():
            merge_dfs['ID'].append(row['ID'])
            merge_dfs['Title'].append(row['Title'])
            merge_dfs['Text'].append(row['Post Text'])
            merge_dfs['Author'].append(row['Author'])
            merge_dfs['OP'].append(int(1))
            merge_dfs['Is Post'].append(int(1))
            merge_dfs['Post Date'].append(row['Post Date'])
            merge_dfs['Subreddit'].append(subreddit)

    merge_dfs = pd.DataFrame(merge_dfs)

    # write to csv
    merge_dfs.to_csv('data/merged/new_posts_merged.csv',index=False)