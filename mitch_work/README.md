# README

`mitch_work` contains Mitch's notebooks for Reddit scraping, and soon, EDA and models for post classification.

## Reddit scraping

### Directories

* `data/` contains:
    * `posts/` containing 9058 reddit posts
    * `comments/` containing 42597 comments associated to the posts in `posts/`

* `test_files/` contains:
    * `data_merge` notebook -- development of csv merging and duplicate cleaning of scraped posts

### Main Notebooks

* `post_scrape.ipynb` is the **MAIN** notebook for scraping each subreddit in `subreddit_list.py` **AND** cleaning the appended csv's in `data/`
* `scrape_tester.ipynb` is a Jupyter notebook that: 
    1. creates a dataframe of dataframes containing posts indexed by the subreddit,
    2. totals the number of posts scraped from each subreddit and totals the total number of posts,
    3. creates a dataframe of dataframes containing comments indexed by the subreddit, and
    4. totals the number of posts scraped from each subreddit and totals the total number of posts.

*Note: these notebooks require the below functions.*

### Functions

* `subreddit_list.py` contains a function that returns the list of subreddits to be scraped
* `clean_comments_csv.py` and `clean_post_csv.py` contain functions to clean duplicates of scraped data from each of the `data/` files
* `reddit_scrape.py` and `comment_scrape.py` contain the **MAIN** functions to scrape subreddit posts from `subreddit_list.py` and the associated comments, respectively.
* `my_praw_info_template.py` is a template for a function that returns the reddit authentication info to use the Reddit API. **Fill in your info then resave the file as `my_praw_info.py`. You can use the function in your notebooks but your info will not be uploaded as `my_praw_info.py` is in the `.gitignore` file.**

### Development Notebooks

* `reddit_scrape.ipynb` is the first development notebook for what would become `post_scrape.ipynb`
    * *Note:* This notebook contains documentation and links for getting started scraping Reddit.

