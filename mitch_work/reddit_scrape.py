import numpy as np
import pandas as pd
import praw
import time

def reddit_scrape():

    # Can generalize in the following way
    # subreddit = string for subreddit name, e.g., r/'SUBREDDIT'
    # n = number of posts to pull -- default is 500
    # category = 0, 1, or 2 where 0 = .new, 1 = .top, 2 = .hot
    # time_delay = number of seconds to delay for next pull 
    #   for comments - the delay is computed by
    #   time_delay*np.random.randint([13)

    from praw.models import MoreComments
    from my_praw_info import get_client_id, get_client_secret, get_user_agent
    from subreddit_list import subreddit_list

    # create a Reddit read-only instance
    reddit = praw.Reddit(client_id=get_client_id(),
                      client_secret=get_client_secret(),
                      user_agent=get_user_agent())

    subbreddits = subreddit_list()
    
    for r_name in subbreddits:

        # Loop subreddits to scrape

        subreddit = reddit.subreddit(r_name)

        # Get new posts in subreddit

        posts = subreddit.new(limit=1000) 

        # print success
        print('Successfully scraped r/'+r_name)

        # Create post dictionary

        posts_dict = {'Title':[], 'Post Date':[],
                    'Post Text':[], 'Author':[],
                    'Author Flair':[], 'Original Content':[],
                    'ID':[], 'Score':[], 
                    'Total Comments':[], 'Post URL':[]}

        # Scrape submissions in posts

        for post in posts:
            # Title of each post
            posts_dict["Title"].append(post.title)

            # Date of past in Unix Time
            posts_dict['Post Date'].append(post.created_utc)
            
            # Text inside a post
            posts_dict["Post Text"].append(post.selftext)

            # Text inside a post
            posts_dict["Author"].append(post.author)

            # Author flair text - None if no flair
            posts_dict['Author Flair'].append(post.author_flair_text)

            # Check for original content
            posts_dict['Original Content'].append(post.is_original_content)
            
            # Unique ID of each post
            posts_dict["ID"].append(post.id)
            
            # The score of a post
            posts_dict["Score"].append(post.score)
            
            # Total number of comments inside the post
            posts_dict["Total Comments"].append(post.num_comments)
            
            # URL of each post
            posts_dict["Post URL"].append(post.url)

        # Save the data in a dataframe

        postdf = pd.DataFrame(posts_dict)

        # old dataframe
        old_df = pd.read_csv('data/posts/'+r_name+'.csv')

        # write to csv
        postdf.to_csv('data/posts/'+r_name+'.csv',index=False,mode='a')

        # new dataframe
        new_df = pd.read_csv('data/posts/'+r_name+'.csv')

        # print success
        print('Successfully appended',len(new_df)-len(old_df),'pulled posts to data/posts/'+r_name+'.csv')

        mins = np.random.randint(low=4, high=10)

        # print delay

        print('Delaying',mins,'minutes')

        # delay before next pull
        time.sleep(60*mins)