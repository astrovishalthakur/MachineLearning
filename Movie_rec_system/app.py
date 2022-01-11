import streamlit as st
import pickle
import pandas as pd
import requests


api_key = "73326928ce817d080bf46bdc0bc675b2"
MOVIE_DB_IMAGE_URL = "http://image.tmdb.org/t/p/w185"
MOVIE_DB_INFO_URL = "https://api.themoviedb.org/3/movie"


def fetch_poster(m_id):
    response = requests.get(url=f"{MOVIE_DB_INFO_URL}/{m_id}?api_key={api_key}&language=en-US")
    data = response.json()
    image_url = f"{MOVIE_DB_IMAGE_URL}{data['poster_path']}"
    return image_url


movies_dict = pickle.load(open("movie_dict.pkl", "rb"))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open("similarity.pkl", "rb"))


def recommend(movie):
    movie_index = movies[movies.title == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    poster = []
    for k in movie_list:
        movie_id = movies.iloc[k[0]].movie_id
        # get movies names
        recommended_movies.append(movies.iloc[k[0]].title)
        # fetch poster names
        poster.append(fetch_poster(movie_id))
    return recommended_movies, poster


st.title("Movie Recommender System")

selected_movie_name = st.selectbox("Please select a movie.",
                                   movies["title"].values)

if st.button("Recommend"):
    names, posters = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(f'{names[0]}')
        st.image(f"{posters[0]}")

    with col2:
        st.text(f'{names[1]}')
        st.image(f"{posters[1]}")

    with col3:
        st.text(f'{names[2]}')
        st.image(f"{posters[2]}")

    with col4:
        st.text(f'{names[3]}')
        st.image(f"{posters[3]}")

    with col5:
        st.text(f'{names[4]}')
        st.image(f"{posters[4]}")

footer="""<style>
a:link , a:visited{
color: blue;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: black;
color: white;
text-align: center;
}

#love {
color: red;
}
</style>
<div class="footer">
<p>Developed with <span id="love">❤</span> by <a style='display: block; text-align: center;' href="https://github.com/astrovishalthakur" target="_blank">Vishal Thakur</a></p>
</div>
"""
st.markdown(footer, unsafe_allow_html=True)
