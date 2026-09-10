import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pd.options.display.max_columns = 20

sns.set_style('whitegrid')

df = pd.read_csv('netflix_titles.csv')

print('First 5 rows:')
print(df.head())

print('\nDataset info:')
print(df.info())

print('\nMissing values:')
print(df.isnull().sum())

def clean_data(df):

    # fill the missing values with 'Unknown'
    for col in ['director', 'cast', 'country', 'rating']:
        df[col] = df[col].fillna('Unknown')

    # remove rows with missing important values
    df = df.dropna(subset=['date_added', 'duration'])

    # convert data_added to datetime
    df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')

    # extract year
    df['year_added'] = df['date_added'].dt.year

    return df

df = clean_data(df)

print('\nCleaned dataset shape:', df.shape)

df.to_csv('netflix_cleaned.csv', index=False)

# Movies vs TV show

plt.figure(figsize=(6,4))
sns.countplot(data=df, x='type')
plt.title('Movies vs TV Shows')
plt.xlabel('Type')
plt.ylabel('Count')
plt.show()

# Top 10 countries
top_countries = df['country'].value_counts().head(10)

plt.figure(figsize=(10,5))
sns.barplot(x=top_countries.values, y=top_countries.index)
plt.title('Top 10 Countries Producing Content')
plt.xlabel('Number of Titles')
plt.show()

# Top 10 genres
top_genres = df['listed_in'].value_counts().head(10)

fig, ax = plt.subplots(figsize=(14,8))
ax.barh(top_genres.index[::-1], top_genres.values[::-1])
ax.set_title('Top 10 Genres on Netflix')
ax.set_xlabel('Number of Titles')
plt.ylabel('Genre')
plt.tight_layout()
plt.show()

# Number of titles added per year
titles_per_year = df.groupby('year_added').size()

plt.figure(figsize=(10,5))
titles_per_year.plot(marker='o')
plt.title("Number of Titles Added to Netflix Per Year")
plt.xlabel("Year")
plt.ylabel("Number of Titles")
plt.show()

# Top 10 actors
actors = df['cast'].str.split(', ').explode()
top_actors = actors.value_counts().head(10)

plt.figure(figsize=(10,5))
sns.barplot(x=top_actors.values, y=top_actors.index)
plt.title('Top 10 Actors Appearing on Netflix')
plt.xlabel('Number of Titles')
plt.ylabel('Actor')
plt.show()

# Content rating distribution
plt.figure(figsize=(10,5))

sns.countplot(
    data = df,
    x = 'rating',
    order = df['rating'].value_counts().index
)
plt.xticks(rotation=45)
plt.title('Distribution of Content Rating on Netflix')
plt.xlabel('Rating')
plt.ylabel('Count')
plt.show()

# Movie duration analysis

movies = df[df['type'] == 'Movie'].copy()

movies['duration'] = movies['duration'].str.replace(' min', '')
movies['duration'] = movies['duration'].astype(int)

plt.figure(figsize=(10,5))
sns.histplot(movies['duration'], bins=30)
plt.title('Distribution of Movie Durations')
plt.xlabel('Minutes')
plt.ylabel('Count')
plt.show()

print('\nAverage movie duration:', movies['duration'].mean())

# Movies vs TV Shows per year
content_by_year = df.groupby(['year_added', 'type']).size().unstack()

content_by_year.plot(figsize=(10,6))
plt.title('Movies vs TV Shows Added Per Year')
plt.xlabel('Year')
plt.ylabel('Number of Titles')
plt.show()

# Heatmap
pivot = df.pivot_table(index='year_added', columns='type', aggfunc='size')

pivot = pivot[pivot.sum(axis=1) > 0]

pivot = pivot.fillna(0).astype(int)

pivot.index = pivot.index.astype(int)
pivot = pivot.sort_index()

plt.figure(figsize=(10,6))

sns.heatmap(pivot,cmap='YlGnBu', annot=True, fmt='d', linewidths=0.5)
plt.title('Netflix Content by Type and Year')
plt.xlabel('Type')
plt.ylabel('Year Added')
plt.show()

# Insights
print('\nKEY INSIGHTS')

print('\nTop country producind Netflix content:')
print(top_countries.head(1))

print('\nMost common rating:')
print(df['rating'].value_counts().idxmax())

print('\nAverage movie duration:')
print(round(movies['duration'].mean(), 2))

print('\nTotal number of titles:')
print(len(df))

print('\nAnalysis completed.')