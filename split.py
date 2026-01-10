import pandas as pd

seed = 19

df1 = pd.read_csv('tatoeba-processed.tsv', delimiter='\t', header = None, names=['en', 'kw'])
df2 = pd.read_csv('Cornwall Council TM (2025 09 17) cc0.csv', delimiter=',', header = None, names=['en', 'kw'])

# Remove NAs
df1 = df1.dropna()
df2 = df2.dropna()

# Mark the source
df1['source'] = 'tatoeba'
df2['source'] = 'akademi'

df = pd.concat([df1, df2], ignore_index=True)
df = df.drop_duplicates(subset=['en','kw'])

# Split evenly between the two sources
train = df.groupby('source', group_keys=False).apply(
    lambda x: x.sample(frac=0.95, random_state=seed)
)
test = df.drop(train.index)

train[['en', 'kw']].to_csv('train.tsv', sep='\t', index=False)
test[['en', 'kw']].to_csv('test.tsv', sep='\t', index=False)
