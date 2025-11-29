# ## Genre Distribution

# %%
plt.figure(figsize=(12,6))
df['primaryGenreName'].value_counts().head(15).plot(kind='bar', color='skyblue')
plt.title("Top 15 Genres in Apple Music Dataset", fontsize=14)
plt.ylabel("Count")
plt.xlabel("Genre")
plt.xticks(rotation=45)
plt.show()

# %% [markdown]
# - Pop completely dominates the dataset Followed by Country, Rock, Alternative, Hip-hop/Rap
# - A long tail of niche genres (R&B/Soul, Christian, Dance, Metal, Holiday, Musical Soundtracks)

# %%
plt.figure(figsize=(12,6))
df['releaseYear'].value_counts().sort_index().plot(kind='line')
plt.title("Number of Tracks Released Per Year", fontsize=14)
plt.ylabel("Count")
plt.xlabel("Release Year")
plt.grid(True)
plt.show()

# %% [markdown]
# -  Almost no data before 1940
# - Growth begins in the 1950s (modern pop era)
# - Explosive growth after 2000 (digital music era)
# - Decline after 2020 (due to sampled data)

# %%
plt.figure(figsize=(12,6))
sns.histplot(df['trackTimeMin'], bins=50, kde=True, color='salmon')
plt.title("Track Duration Distribution (Minutes)", fontsize=14)
plt.xlabel("Track Length (minutes)")
plt.ylabel("Count")
plt.show()

# %% [markdown]
# - Peak around 3.5–4 minutes
# - Long tail up to 10+ minutes
# - Very few tracks under 2 minutes
# - Shape is ~normal distribution

# %%
plt.figure(figsize=(14,6))
sns.boxplot(data=df, x='primaryGenreName', y='trackTimeMin')
plt.xticks(rotation=90)
plt.title("Track Duration by Genre")
plt.ylabel("Duration (minutes)")
plt.show()

# %% [markdown]
# - Classical, jazz, and soundtracks → consistently long tracks (6–10+ minutes)
# - Hip-hop/rap, pop, dance, country, rock → tightly clustered around 3–4 minutes
# - Comedy, holiday, musicals → more diverse durations
# - Some genres show extreme outliers (e.g., 15–16 minute tracks)

# %% [markdown]
# Track length is genre-dependent. Mainstream genres (pop, hip-hop, dance, rock) tightly center around 3–4 minutes, reflecting commercial formats optimized for high engagement and minimal skip risk. Classical, jazz, and soundtrack genres demonstrate significantly longer durations, which is consistent with the structure of extended compositions. Editorial teams should consider these differences when designing playlists, ensuring smooth pacing and predictable listening flow.

# %%
plt.figure(figsize=(6,6))
df['isExplicit'].value_counts().plot(kind='pie', autopct='%1.1f%%', labels=['Non-Explicit','Explicit'], colors=['lightgreen','lightcoral'])
plt.title("Explicit vs Non-Explicit Tracks", fontsize=14)
plt.ylabel("")
plt.show()

# %% [markdown]
# - only 14% are explicit
# - catalog skews toward general audience /. family-safe content

# %%
explicit_by_genre = df.groupby('primaryGenreName')['isExplicit'].mean().sort_values(ascending=False).head(15)

plt.figure(figsize=(14,6))
explicit_by_genre.plot(kind='bar', color='tomato')
plt.title("Explicit Content Ratio by Genre (Top 15)")
plt.ylabel("Percentage Explicit")
plt.show()

# %% [markdown]
# Explicit content is heavily concentrated in specific sub-genres of hip-hop and rap, where 80–100% of tracks include advisory labels. In contrast, pop, dance, and Latin music show low explicit ratios. This polarization has implications for parental controls, editorial playlist targeting, and content policies across age-sensitive regions.

# %%
top_artists = df['artistName'].value_counts().head(20)

plt.figure(figsize=(12,6))
top_artists.plot(kind='bar', color='steelblue')
plt.title("Top 20 Most Frequent Artists in Dataset")
plt.ylabel("Track Count")
plt.show()

# %% [markdown]
# The dataset highlights a strong representation of globally influential artists across pop, rock, and country genres. Taylor Swift, One Direction, and Ed Sheeran dominate the catalog sample, reflecting consistent consumer demand and high-volume discographies. Legacy artists like Michael Jackson, Elvis Presley, and Madonna provide deep catalog value that drives back-catalog streaming, a major contributor to Apple Music revenue.

# %%
album_track_counts = df.groupby('collectionId')['trackCount'].max()

plt.figure(figsize=(12,6))
sns.histplot(album_track_counts, bins=30, kde=True)
plt.title("Distribution of Number of Tracks Per Album")
plt.xlabel("Tracks in Album")
plt.ylabel("Count")
plt.show()

# %%
plt.figure(figsize=(12,6))
df['country'].value_counts().head(10).plot(kind='bar', color='orchid')
plt.title("Top Countries in Apple Music Dataset")
plt.ylabel("Track Count")
plt.show()

# %%
df['releaseMonth'] = df['releaseDate'].dt.month
plt.figure(figsize=(12,6))
df['releaseMonth'].value_counts().sort_index().plot(kind='bar', color='skyblue')
plt.title("Track Releases by Month")
plt.xlabel("Month")
plt.ylabel("Count")
plt.show()

# %% [markdown]
# - Biggest release spikes in January, October, November
# - Lowest in February, July, December
# - Strong mid-year consistency
# 
# Track releases peak in January and again in October–November, matching industry cycles: new year releases, fall album season, and pre-holiday ramps. Lower volumes in February and December reflect typical industry lulls. These seasonal trends are crucial for planning editorial promotions, new-music campaigns, and themed playlists.

# %%
genre_month = pd.crosstab(df['primaryGenreName'], df['releaseMonth'])

plt.figure(figsize=(14,10))
sns.heatmap(genre_month, cmap='YlGnBu')
plt.title("Genre Release Frequency by Month")
plt.xlabel("Month")
plt.ylabel("Genre")
plt.show()

# %% [markdown]
# - Pop dominates every month (consistent release volume)
# - Rock shows strong activity March–April & September–October
# - Hip-hop/rap peaks around March–June
# - Soundtrack spikes in late summer (likely tied to movie releases)
# - Christmas genres spike sharply in November–December
# 
# Seasonal genre patterns clearly emerge. Pop remains stable across the year, serving as an evergreen content category. Hip-hop/rap releases concentrate in spring and early summer, reflecting festival and touring seasons. Rock albums peak in early spring and fall, consistent with historical release cycles. Holiday genres predictably spike in November and December, reinforcing the need for timely editorial updates to seasonal playlists.
