import pandas as pd

def preprocess(url):
    url = url.replace("https://", "")
    url = url.replace("http://", "")
    url = url.replace("www.", "")

    slash_index = url.find("/")
    if slash_index != -1:
        url = url[:slash_index]

    qm_index = url.find("?")
    if qm_index != -1:
        url = url[:qm_index]

    return url

def load_dataset():
    # df 1 preprocessing
    df1 = pd.read_csv("data/urldata.csv")
    df1 = df1.drop('Unnamed: 0', axis=1)
    del df1["label"]
    df1.rename(columns={'result':'label'}, inplace=True)

    # df 2 preprocessing
    df2 = pd.read_csv("data/malicious_phish.csv")
    labels = [0 if label == "benign" else 1 for label in df2["type"] ]
    df2["label"] = labels
    del df2["type"]

    # concat
    df = df1.append(df2)
    df['url']= df['url'].apply(preprocess)

    # remove duplicate urls
    df = df.drop_duplicates(subset="url", keep="last")
    return df
    