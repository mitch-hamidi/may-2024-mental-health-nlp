# Overview

This folder contains Gabe Khan's work on the mental health nlp project for the May 2024 cohort of the Erdos Institute. The goal of this was to find posts on r/bpd which discuss the medical management and treatment of Borderline Personality Disorder (BPD) and analyze the sentiments that users felt about various medications and therapy approaches.



# Methodology
1. Clean and perform exploratory data analysis with the Kaggle dataset. I restricted my attention to Reddit posts from r/bpd from 2012 through 2022, since there were some unusual shutdowns in the subreddit outside of these times. This showed that posts which do not contain any keywords are very unlikely to be relevant, but among posts with keywords, the majority are still not relevant.
2. Build a model to classify posts which are relevant to the treatment and medical management of r/bpd. One considerable challenge is that the vast majority of posts (~95%) are not relevant, so the data is very imbalanced. For this, five classes of models were attempted:
a. A baseline logistic regression model trained to a sample of manually coded posts using a vectorization of the text contents. At a threshold of .04, this had a recall of .75 and a precision of .14 on a split of the training data.
b. A model using keyword counts and a vectorization of the text contents. For this, I grouped keywords into several classes (such as medications or therapy modes) so that infrequently used words in these classes would affect the relevance probability when they appear. At a threshold of .04, this had a recall of .88 and a precision of .38 on a split of the training data. This was a significant improvement over the baseline model.
c. A zero-inflated version of the previous model which rejected all posts without any keywords and fit the classifier to the text containing keywords. For this model, I attempted various different combinations of keywords and statistical models. Occasionally, AdaBoostClassifier would outperform logistic regression, but for most random seeds, simple logistic regression was optimal. The final chosen model was of this class, and most of the time its performance was roughly equivalent to the models in class b. However, the major advantage is that there were certain random splits where all of the models would underperform. For these, the zero-inflated keyword models had the most stable performance, indicating fairly reliable performance.
d. A fine-tuning of DistilBert. Unfortunately, since the training data skewed to not being relevant, this model learned that posts discussing bpd were irrelevant. Text from other sources, such as 'The quick red fox jumps over the lazy dog' were returned as far more relevant. This was a limitation of the training data, and with more sophisticated modelling, this issue could have been addressed. However, each attempt to use this model took over an hour to train, and given the time constraints I did not feel like I could realistically get a working model using this approach with my laptop.
 e. Finally, I tried using a LLM (ollama dolphin and ollama dolphin-mistral) to return whether a post was relevant. The results of this were excellent, but each post took over 2 minutes to process and given that there were over 240,000 posts to process, this was not a feasible approach.

3. After selecting a model for finding relevant posts, I ran the model on all posts in r/bpd over an 8 year time span and collected the "most relevant" posts (i.e., those with relevance probability over .3 and .5). At this threshold, validation showed that the recall was very low, but the precision was extremely good. Therefore, the collection of 2557 posts were very high-quality and discuss the treatment of bpd in detail. Further exploration is required to determine whether these posts are representative of relevant posts. I then used an NER (found by Emilie Curl) to classify all the medications in the post and build a network of medications. For posts containing a particular medication, I ran a script to determine the sentiment towards that medication. I did not try to build my own sentiment analysis model but adapted instead used prompt engineering with a LLM. Since the dataset was too large to run with ollama on my computer, I instead used API calls to OpenAI using the GPT-4o model for this purpose. Doing so was not free, so a lot of effort was put into prompt engineering to ensure that all calls to the server would return useful responses. Processing the most frequently mentioned medication (Lamotrigine) cost $1.80 and the second most frequently mentioned medication (Sertraline) cost $1.56. However, doing so yielded detailed breakdown of the sentiments about these medications.


# Results:
The chosen relevancy model can be used to quickly return a collection of highly-relevance posts, with extremely good precision once the threshold is sufficiently large (e.g., .5). At these values, the recall is fairly small, but since there is a large number of posts, this still yields a high quality dataset. Further investigation is needed to determine whether these posts are representative of relevant posts. The dataset containing posts with threshold over .5 and all the medications in each post can be found in /data/highly_relevant_posts_descending_threshold_50_augmented.csv.

Due to time constraints and how difficult it is to determine sentiments towards a single aspect within a body of text, I did not attempt to design my own sentiment analysis model. However, the high-quality dataset was small enough to use GPT-4o and prompt engineering to generate these sentiments. For the most part, this analysis was highly accurate in determining positive or negative sentiments, although it did struggle to distinguish between cases where the sentiment was mixed or unclear (such as when the user had not yet taken the medication and was simply asking about it). From manual coding and comparison to the generated responses, the sentiment analysis was 76% accurate but 88.5% accurate in determining positive, negative and others. From validation, I found that the model tended to be a slightly optimistic.

I ran the sentiment analysis for the three most frequently referenced medications, which were Lamotrigine (aka Lamictal), Sertraline (aka Zoloft) and Quetiapine (aka Seroquel).

1. Lamotrigine (raw scores) : 196 positive (35.5%), 88 negative (16%),  268 unclear/mixed/not taken (48.5%)
2. Lamotrogine (200 manually corrected scores): 60 positive (30%), 35 negative (17.5%), 105 unclear/mixed/not taken (52.5%)
3. Sertraline: 107 positive (26%), 121 negative (30%), 178 unclear/mixed/not taken (44%)
4. Quetiapine: 118 positive (30%), 83 negative (21%), 195 unclear/mixed/not taken (49%)

Furthermore, I obtained wordclouds from the posts where users describe their experience with the medication. Of these, the most informative one was the one for Quetiapine.

![alt text](https://github.com/mitch-hamidi/may-2024-mental-health-nlp/blob/main/Gabe's_notebooks/relevant_post_analysis/Quetiapine_sentiments.png?raw=true)

From this, we can see the brand name for Quetiapine (i.e., Seroquel) as well as the fact it induces sleepiness. In fact, it is sometimes prescribed off-label as a sleeping pill. Furthermore, we see two common side effects (weight gain and dependency issues).

# Conclusions: 

This analysis could be used by pharmaceutical companies to assess the sentiments within social media communities towards various medications. Since the information is self-reported and its reliability cannot be determined, this data cannot be used to draw conclusions about the clinical effectiveness of medications. Nonetheless, this information could be used to inform marketing and advertising decisions. For example, the sentiment were overall positive towards Lamotrigine and there were a number of posts inquiring about its effectiveness.

### Limitations

Because the Kaggle dataset did not include much of the relevant metadata (such as username, post score and comments), the analysis I could perform was somewhat limited. In particular, many of the relevant posts contained questions about which medications others found effective, and knowing the responses to this would have provided a much richer dataset.

The models that I could run was limited in several ways. Since the topic was extremely specific, having more training data would have been very helpful for improving the performance of the models. Second, my computer was not powerful enough to run modern NLP techniques effectively. I believe that a model using zero-inflation and a transformer or LLM would greatly outperform my model.

### Future work 

For future work, it would be better to improve the model for evaluating post relevancy to determine whether the posts I obtain were representative of relevent posts. Furthermore, we have not attempted to understand whether the frequency or sentiments of relevant posts are affected by when they were posted.

 It would also be of interest to run these models on scraped data with more metadata (such as usernames, comments and upvotes) to get a better breakdown of the overall sentiment within the subreddit. Furthermore, it would be of interest to build models for the consensus of a large number of posts.

Finally, this model can be run for other mental health conditions as well, so long as one updates the keywords appropriately. It would be of interest to see its analysis for other datasets as well.



# Folder contents:

1_Initial_analysis_and_cleaning contains the initial cleaning of the data and some preliminary data analysis. At this point, a sample of posts were separated from the dataset for manual coding for relevance.

2_Analysis_of_manually_coded_data contains some preliminary analysis of the manual coded data, including trying to understand its breakdown and the performance of simple models to classify relevant. After this point, I started trying to build models with improved performance.

'data' contains all the relevant data and csv files generated by our analysis. I have not attempted to organize it in any way.

'keywords' contains several files listing keywords for the treatment and diagnosis of bpd, as well as code used to generate them. These are also not organized, and mostly just used as parameters in the model

'relevance_models' contains the main statistical analysis in this project. Here, I attempted to model which posts were relevant to the treatment of bpd. From manual coding, only about 5% of posts were relevant, so this dataset is quite noisy. Five classes of models were considered and a final version was decided on and validated.

'relevant_post_analysis' starts by taking the chosen statistical model and running it on a large portion of the Kaggle dataset (r/bpd posts from 1-1-2014 through 1-1-2022). With a threshold of .5, this yielded 2557 highly relevant posts, nearly all of which discuss the medical management of bpd in some form. I also used a named entity recognition (NER) for all the medications in these posts. 


# Notes:
1. Files in folders are numbered to explain their order.
2. 'keywords', 'relevancy_models' and 'relevant_post_analysis' contain Readme files with more details on their contents. 