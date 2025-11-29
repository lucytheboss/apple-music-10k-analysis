# ## Data Cleaning

# %%
df_raw = df.copy()
df = df.copy()   # working copy

# %%
df['releaseDate'] = pd.to_datetime(df['releaseDate'], errors='coerce')

# %%
df['releaseDate'].isna().sum()

# %%
df['primaryGenreName'] = df['primaryGenreName'].str.lower().str.strip()
df['primaryGenreName'].value_counts().head()

# %%
df['trackTimeSec'] = df['trackTimeMillis'] / 1000

# %% [markdown]
# ## NA cleaning

# %%
# Fill advisory rating
df['contentAdvisoryRating'] = df['contentAdvisoryRating'].fillna('clean')

# Fill prices with median
df['collectionPrice'] = df['collectionPrice'].fillna(df['collectionPrice'].median())
df['trackPrice'] = df['trackPrice'].fillna(df['trackPrice'].median())

# Fill isStreamable
df['isStreamable'] = df['isStreamable'].fillna('true')

# %% [markdown]
# ## converting to 0/1

# %%
df['isStreamable'] = df['isStreamable'].map({'true': 1, 'false': 0})
df['isStreamable'].value_counts()

# %%
df['trackTimeSec'] = df['trackTimeMillis'] / 1000
df['trackTimeMin'] = df['trackTimeSec'] / 60

# %%
df['releaseYear'] = df['releaseDate'].dt.year

# %%
df['isExplicit'] = df['trackExplicitness'].apply(lambda x: 1 if x == 'explicit' else 0)

# %%
df.isna().sum()
