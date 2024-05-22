import pandas as pd

def clean_comments_csv(filepath):

    comment_df = pd.read_csv(filepath)

    # drop duplicates by post index
    cleaned_df = comment_df.drop_duplicates(
    subset = ['ID','Comment'],
    keep = 'last').reset_index(drop = True)

    # print duplicate count
    print(len(comment_df)-len(cleaned_df),'duplicates dropped from',filepath)

    cleaned_df = cleaned_df[cleaned_df.Comment != 'Comment']

    cleaned_df.to_csv(filepath, index=False)