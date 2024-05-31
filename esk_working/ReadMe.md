# Directory 
Overview of contents 
## Datafiles 
* Uncleaned scraped datafiles for r/BorderlinePDisorder and r/BPD were too large and are separated into compressed files labeled datafiles.zip (r/BorderlinePDisorder) and bpdcomments.zip(r/bpd)
  * r/bpd - 113997 comments scraped
  * r/BorderlinePDisorder - 98073 comments scraped
  * r/BPDmemes - 38281 comments scraped
* Cleaned datafiles - accounting for duplicates
  * cleaned_bpd - 65094 comments
  * cleaned_BorderlinePDisorder - 27676 comments
  * cleaned_BPDmemes - 38280 comments
* keywords.csv contains the keyword list I created for comment scraping. keywords include 89 bpd treatment relevant words. This file is used for the webscraping ipynb.
  * keywords file contains 3 columns
  * 1st column lists all 89 keywords
  * 2nd column contains information regarding type of treatment including drug class
  * 3rd column contains information whether it is a medication or behavioral based treatment
* combined_cleaned_df.zip contains the all 3 subreddit cleaned files combined
* combined_ner_df.zip contains NER, Nouns & adj, and Drugs Mentioned for all scraped comments
* val_ds.csv
  * contains 311 comments that were manually coded as relevant to treatment
* cleaned_coded_vset
  * roughly marked for relevance from posts in subreddit r/BorderlinePDisorder
  * cleaned for duplicates, deleted comments, and NaN authors 
## Webscraping, cleaning, and NLP Notebooks
* Data scraping notebooks are uploaded individually by subreddit labeled "subreddit_scraping-$subredditname-Copy1.ipynb".
* Contains steps from pulling from Reddit API (personal keys withheld), uploading keywords list, selecting subreddit, for loop to iterate through 89 keywords with delay for reddit API limitations and accounting for skips or no values for keywords, creating a csv for all combined comments in subreddit, can also search all comments within keyword dictionary.
* data cleaning notebook - modifying Mitch's comment cleaning function to not overwrite original data file
* data_cleaning-coded.ipynb
  * notebook for cleaning validation set
  * cleaned_coded_vset and val_ds.csv   
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
