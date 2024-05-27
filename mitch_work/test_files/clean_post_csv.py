import pandas as pd

def clean_post_csv(filepath):

    post_df = pd.read_csv(filepath)

    # drop duplicates by post index
    cleaned_df = post_df.drop_duplicates(
    subset = ['ID'],
    keep = 'last').reset_index(drop = True)

    print(len(post_df)-len(cleaned_df),'duplicates dropped from',filepath)

    # remove duplicate of column headers
    cleaned_df = cleaned_df[cleaned_df.ID != 'ID']

    cleaned_df.to_csv(filepath, index=False)