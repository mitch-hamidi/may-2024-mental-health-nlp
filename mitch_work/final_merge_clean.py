import numpy as np
import pandas as pd
import praw
import time

from subreddit_list import subreddit_list

def final_merge_clean():

    subreddits = subreddit_list()

    # load post dataframe
    merge_dfs = pd.read_csv('data/merged/new_posts_merged.csv',index_col=False)

    # correct column data types
    list = ['ID', 'Title', 'Text', 'Author','Subreddit']
    for item in list:
        merge_dfs[item] = merge_dfs[item].astype('string')

    # create empty dictionary for subreddit dataframes
    comment_dfs = dict.fromkeys(subreddits)

    # fill dictionary with dataframes
    for subreddit in subreddits:
        comment_dfs[subreddit]= pd.read_csv('data/comments/'+subreddit+'_comments.csv')

    # append comments to merged post dataframe
    for subreddit in subreddits:
        reduced_comment_df = {'ID':[], 'Title':[], 'Text':[], 
                        'Author':[], 'OP':[], 'Is Post':[], 
                        'Post Date':[], 'Subreddit':[]}
        for index, row in comment_dfs[subreddit].iterrows():
            reduced_comment_df['ID'].append(row['ID'])
            reduced_comment_df['Title'].append(merge_dfs.loc[(merge_dfs['ID'] == row['ID']) 
                & (merge_dfs['Is Post'] == 1)]['Title'].item())
            reduced_comment_df['Text'].append(row['Comment'])
            reduced_comment_df['Author'].append(row['Author'])
            if row['OP'] == True:
                reduced_comment_df['OP'].append(int(1))
            else:
                reduced_comment_df['OP'].append(int(0))
            reduced_comment_df['Is Post'].append(int(0))
            reduced_comment_df['Post Date'].append(row['Post Date'])
            reduced_comment_df['Subreddit'].append(subreddit)
        reduced_comment_df = pd.DataFrame(reduced_comment_df)
        merge_dfs = pd.concat([merge_dfs,reduced_comment_df]).reset_index(drop=True)

    # drop deleted comments/posts
    merge_dfs = merge_dfs.drop(merge_dfs[merge_dfs['Text']=='[deleted]'].index)

    # drop posts with no author
    merge_dfs = merge_dfs.dropna(subset=['Author'])

    # input indetifier for no text in post/comment
    merge_dfs['Text'] = merge_dfs['Text'].fillna('[no text]')

    # resort according to post
    merge_dfs.sort_values(by=['ID']).reset_index()

    # write to csv
    merge_dfs.to_csv('data/merged/mitch_master_data.csv',index=False)