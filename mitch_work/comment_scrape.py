import numpy as np
import pandas as pd
import praw
import time

def comment_scrape():

    from praw.models import MoreComments
    from my_praw_info import get_client_id, get_client_secret, get_user_agent
    from subreddit_list import subreddit_list

    # create a Reddit read-only instance
    reddit = praw.Reddit(client_id=get_client_id(),
                      client_secret=get_client_secret(),
                      user_agent=get_user_agent())

    subreddits = subreddit_list()
    
    for r_name in subreddits:

        postdf = pd.read_csv('data/posts/'+r_name+'.csv')
        postdf.drop_duplicates(subset=None, keep='first',inplace=True)

        links = postdf.loc[(postdf['Total Comments'] != '0') 
                        & (postdf['Total Comments'] != 'Total Comments')].reset_index()

        comments = {'ID':[],'Comment':[], 'Author':[],'OP':[],'Post Date':[]}

        i = 0

        for link in range(len(links)):
            flag = 0
            submission = reddit.submission(id=links['ID'][link])

            try:
                submission.comments.replace_more(limit=None)
            except:
                flag = 1
            
            if flag == 0:
                for comment in submission.comments.list():
                    comments['ID'].append(links['ID'][link])
                    try:
                        comments['Comment'].append(comment.body)
                    except:
                        comments['Comment'].append('None')
                    try:
                        comments['Author'].append(comment.author)
                    except:
                        comments['Author'].append('NONE')
                    try:
                        comments['OP'].append(comment.is_submitter)
                    except:
                        comments['OP'].append('NONE')
                    try:
                        comments['Post Date'].append(comment.created_utc)
                    except:
                        comments['Post Date'].append('NONE')

            i += 1
            flag = 0
            
            if i % 100 == 0:
            #    mins = np.random.randint(low=4, high=6)
            #    # print delay
            #    print('Completed',link,'posts. Delaying',mins,'minutes')
                print('Completed',link+1,'posts.')
            #    time.sleep(60*mins)

        comments_df = pd.DataFrame(comments)

        # old dataframe
        old_df = pd.read_csv('data/comments/'+r_name+'_comments.csv')

        # write to csv
        comments_df.to_csv('data/comments/'+r_name+'_comments.csv',index=False,mode='a')

        # new dataframe
        new_df = pd.read_csv('data/comments/'+r_name+'_comments.csv')

        # print success
        print('Successfully appended',len(new_df)-len(old_df),'pulled comments to data/comments/'+r_name+'_comments.csv')

        time.sleep(60*4)