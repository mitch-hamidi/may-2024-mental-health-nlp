# Directory 
Overview of contents 
## Datafiles 
* Uncleaned scraped datafiles for r/BorderlinePDisorder and r/BPD were too large and are separated into compressed files labeled datafiles.zip (r/BorderlinePDisorder) and bpdcomments.zip(r/bpd)
  * r/bpd - 113997 comments scraped
  * r/BorderlinePDisorder - 98073 comments scraped
  * r/BPDmemes - 38281 comments scraped
* Cleaned datafiles - accounting for duplicates
  * 
* keywords.csv contains the keyword list I created for comment scraping. keywords include 89 bpd treatment relevant words. This file is used for the webscraping ipynb.
## Webscraping Notebooks
* Data scraping notebooks are uploaded individually by subreddit labeled "subreddit_scraping-$subredditname-Copy1.ipynb".
* Contains steps from pulling from Reddit API (personal keys withheld), uploading keywords list, selecting subreddit, for loop to iterate through 89 keywords with delay for reddit API limitations and accounting for skips or no values for keywords, creating a csv for all combined comments in subreddit, can also search all comments within keyword dictionary.
## See Readme in main project directory for proposal details
* Commits/Sections I included
  * Goal
  * Problem
  * Methodology
  * Stakeholders of the project
  * Key Performance Indicators (KPIs)
  * Data Sources
  * Reddit List
  * Keywords
