import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


@st.cache_data()
def load_and_preprocess_tracks():
    data=pd.read_csv(r'tracks.csv')
    data["duration"]= data["duration_ms"].apply(lambda x: round(x/1000))
    data.drop("duration_ms", inplace=True, axis=1)
    data.set_index('release_date',inplace=True)
    return data

@st.cache_data()
def load_and_preprocess_SpotifyFeatures():
    df_genre=pd.read_csv(r'SpotifyFeatures.csv')
    return df_genre


with st.spinner("Loading tracks dataset..."):
    data = load_and_preprocess_tracks()

st.title("Spotify Data Analysis:-")
st.header("First data:-")
st.dataframe(data)

with st.spinner("Loading tracks dataset..."):
    df_genre = load_and_preprocess_SpotifyFeatures()

st.header("Second data:-")
st.dataframe(df_genre)

st.divider()

st.title("Visualizations:-")
st.header("Comparing song features:-")
st.subheader("Loudness vs Energy")
sample_size = st.slider("0. Select sample size",0.0, 1.0, step=0.005, value=0.010)
sample_df = data.sample(int(sample_size*len(data))) 
fig, ax = plt.subplots(figsize=(10,6))
sns.regplot(data = sample_df, y= "loudness", x = "energy",ax=ax).set(title="Loudness vs Energy")
st.pyplot(fig, use_container_width=True)

st.divider()

st.subheader("Popularity vs Acousticness")
sample_size1 = st.slider("1. Select sample size",0.0, 1.0, step=0.005, value=0.010)
sample_df = data.sample(int(sample_size1*len(data))) 
fig, ax = plt.subplots(figsize=(10,6))
sns.regplot(data = sample_df, y= "popularity", x = "acousticness", color = "b").set(title="Popularity vs Acousticness")
st.pyplot(fig, use_container_width=True)

st.divider()

st.subheader("Liveness vs Valence")
fig, ax = plt.subplots(figsize=(10,6))
sns.scatterplot(x='valence',y='liveness',data=df_genre.head(50))
st.pyplot(fig, use_container_width=True)

st.divider()

st.subheader("Energy vs Danceability")
fig, ax = plt.subplots(figsize=(10,6))
fig,axs = plt.subplots(1,2)
data.head(20)['energy'].plot(
                               
                               kind='line',
                               
                               
                               figsize = (7,7),
                               
                               ax=axs[0],
                               title='energy',
                               )
data.head(20)['danceability'].plot(
                              kind='area'    ,   
                              figsize = (7,7),
                              ax=axs[1],
                              title='danceability',
                                              )

plt.show()
st.pyplot(fig, use_container_width=True)

st.divider()

st.subheader("Speechiness vs Tempo")
fig, ax = plt.subplots(figsize=(10,6))
fig,axs = plt.subplots(1,2)
data.head(20)['speechiness'].plot(
                               
                               kind='line',
                               
                               
                               figsize = (7,7),
                               
                               ax=axs[0],
                               title='speechiness',
                               )
data.head(20)['tempo'].plot(
                              kind='line'    ,   
                              figsize = (7,7),
                              ax=axs[1],
                              title='tempo',
                                              )

plt.show()
st.pyplot(fig, use_container_width=True)

st.divider()

st.subheader("Key vs Tempo")
fig, ax = plt.subplots(figsize=(10,6))
sns.lineplot(x='key',y='tempo',data=df_genre.head(50))
st.pyplot(fig, use_container_width=True)

st.divider()

st.header("Duration of the songs in different genres:-")
fig, ax = plt.subplots(figsize=(10,6))
plt.title("Duration of the Songs in Different Genres")
sns.color_palette("rocket", as_cmap= True)
sns.barplot (y='genre', x='duration_ms', data=df_genre)
plt.xlabel("Duration in milli seconds")
plt.ylabel("Genres")
st.pyplot(fig, use_container_width=True)

st.divider()

st.header("Top 5 genres by popularity:-")
fig, ax = plt.subplots(figsize=(10,6))
sns.set_style(style = "darkgrid")
famous=df_genre.sort_values("popularity", ascending = False).head(10)
sns.barplot(y= 'genre', x='popularity', data = famous).set(title= "Top 5 Genres by Popularity")
st.pyplot(fig, use_container_width=True)

st.divider()

st.header("Top Artists by popularity:-")
fig, ax = plt.subplots(figsize=(15,10))
sns.barplot(x='artist_name',y='popularity',data=df_genre.head(16))
st.pyplot(fig, use_container_width=True)  

st.divider()

















