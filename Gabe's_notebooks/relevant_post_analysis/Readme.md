This folder applies the relevant analysis to obtain a collection of posts which are labeled as relevant by the final keyword/decision-tree model and runs statistical analysis on these posts.


The creating_dataframe notebook does the following.
    1. We import and clean all the subreddit posts from r/bpd between 1/1/2014 and 1/1/2022. This process was originally done in the initial analysis. We also combine the title and text of the posts.
    2. We import and train the keyword model on the entire training data (leaving out the testing set, which was manually coded separately and not in the date ranges shown here). Doing so, we obtain a model for determining whether a post is relevant to the treatment of borderline personality disorder.
    3. We run our model on the cleaned text from all of the subreddit posts obtained in step 1. We then drop the posts whose relevance value is very small (less than .04) to obtain ~58,000 posts, which are far more likely to be relevant in general.
    4. We create a new dataframe which is ordered by relevance. By cutting off the relevance value at a much higher threshold, we obtain the posts of extremely high quality for the research question. I chose to include two cut-offs (.5 and .3), and going through these csv files all of the posts appear to be extremely relevant to the question (see 'highly_relevant_posts_descending_threshold_30.csv').

After this, I tried to generate sentiment analysis by running ollama with a carefully scripted prompt. These experiments are contained in ollama_experiments and ollama_experiments_2. This code requires access to the terminal to run correctly. My graphics card is only 1536 MB, so even when these models worked, they were too slow to be of use.

The next idea was to repeat this approach using a ChatGPT model by making calls to the API. I started with gpt-3.5-turbo-instruct, but the results were fairly poor. Furthermore, the number of tokens per post was severely limited, restricting the quality of our analysis. Although it was a bit more expensive, gpt-4o worked much better and I ran this code in the OpenAI_text_analysis_4o. This yielded several CSV files. Most notably, Lamotrigine_sentiments_4o contains the sentiments of the posts containing this medication. There is a cleaned version of this file, which converts some of the output to columns and also a coded version. Furthermore, I manually verified that the sentiment analysis was appropriate and made changes to the sentiment/reason where it was incorrect.

It is possible to validate the outcomes of the sentiment analysis by comparing the coded and uncoded versions of the Lamotrigine sentiment. There are 101 instances where the coded and generated values disagree (82% accuracy). However, 81 of these are switches between '0' and '-'. Therefore, if we group mixed, unclear and no experience, there are only 20 examples the sentiment switching (and no example of a positive sentiment becoming negative or vice-versa). For 552 posts, this is roughly 95% accuracy. With better prompt engineering, it should be possible to improve this perfomance.

The fake_text_analysis was written to produce the code needed to run sentiment analysis without making unnecessary and expensive calls to the API. Note that for both the OpenAI notebooks, the API key has been removed and will need to be put back in to get a running model.

Generating_Lamotrigine_images is a notebook to create graphs associated to the sentiment analysis and drug network. The other files in this folder are images created in this process.

The same analysis used for Lamotrigine was then run for Sentraline (i.e., Zoloft), which was the second most common medication. The sentiments in the high-quality dataset were less positive towards Zoloft compared to Lamotrigine.

