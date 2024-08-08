# # # # import streamlit as st
# # # # import pickle
# # # # import pandas as pd
# # # # import requests

# # # # def fetch_poster(movies_id):
# # # #     response=requests.get(f'https://api.themoviedb.org/3/movie/{movies_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US')
# # # #     data = response.json()
# # # #     return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

# # # # def recommend(movie):
# # # #     movie_index = movies[movies['title'] == movie].index[0]
# # # #     distances = similarity[movie_index]
# # # #     movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

# # # #     recommended_movies = []
# # # #     recommended_movies_poster=[]
# # # #     for i in movies_list:
# # # #         movie_id = movies.iloc[i[0]].movie_id
# # # #         recommended_movies.append(movies.iloc[i[0]].title)
# # # #         # fetch poster from API
# # # #         recommended_movies_poster.append(fetch_poster(movie_id))
# # # #     return recommended_movies , recommended_movies_poster

# # # # movies_dict = pickle.load(open('movie_dict.pkl','rb'))
# # # # movies = pd.DataFrame(movies_dict)

# # # # similarity = pickle.load(open('similarity.pkl','rb'))

# # # # # Custom CSS styling for modern design
# # # # st.markdown("""
# # # #     <style>
# # # #         body {
# # # #             font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
# # # #             background-image: linear-gradient(120deg, #f6d365 0%, #fda085 100%);
# # # #             color: #333333;
# # # #         }
# # # #         .title {
# # # #             font-size: 36px;
# # # #             font-weight: bold;
# # # #             text-align: center;
# # # #             margin-bottom: 30px;
# # # #             color: #4CAF50;
# # # #         }
# # # #         .movie-title {
# # # #             font-size: 24px;
# # # #             font-weight: bold;
# # # #             text-align: center;
# # # #             margin-bottom: 10px;
# # # #             color: #333333;
# # # #         }
# # # #         .movie-image {
# # # #             display: block;
# # # #             margin-left: auto;
# # # #             margin-right: auto;
# # # #             margin-bottom: 20px;
# # # #             border-radius: 10px;
# # # #             box-shadow: 0px 0px 20px 0px rgba(0,0,0,0.2);
# # # #             transition: transform 0.3s ease-in-out;
# # # #             border: 2px solid #ccc;
# # # #             cursor: pointer;
# # # #         }
# # # #         .movie-image:hover {
# # # #             transform: scale(1.05);
# # # #         }
# # # #     </style>
# # # # """, unsafe_allow_html=True)

# # # # st.title('Movie Recommender System')
# # # # st.markdown("### A modern and visually vibrant movie recommender system using cosine similarity")

# # # # selected_movies_name = st.selectbox(
# # # #     'Select a movie:',
# # # #     movies['title'].values)

# # # # if st.button('Recommend'):
# # # #     names, posters = recommend(selected_movies_name)

# # # #     cols = st.columns(len(posters))

# # # #     for i, (name, poster) in enumerate(zip(names, posters)):
# # # #         with cols[i]:
# # # #             st.image(poster, caption=name, use_column_width=True, output_format='JPEG')
# # # #             st.markdown(f"<a href='https://www.google.com/search?q={'+'.join(name.split())}+movie+watch' target='_blank'><img class='movie-image' src='https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Google_2015_logo.svg/220px-Google_2015_logo.svg.png' width='100' height='100'></a>", unsafe_allow_html=True)
# # # # import streamlit as st
# # # # import pickle
# # # # import pandas as pd
# # # # import requests

# # # # def fetch_poster(movies_id):
# # # #     response=requests.get(f'https://api.themoviedb.org/3/movie/{movies_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US')
# # # #     data = response.json()
# # # #     return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

# # # # def recommend(movie):
# # # #     movie_index = movies[movies['title'] == movie].index[0]
# # # #     distances = similarity[movie_index]
# # # #     movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

# # # #     recommended_movies = []
# # # #     recommended_movies_poster=[]
# # # #     for i in movies_list:
# # # #         movie_id = movies.iloc[i[0]].movie_id
# # # #         recommended_movies.append(movies.iloc[i[0]].title)
# # # #         # fetch poster from API
# # # #         recommended_movies_poster.append(fetch_poster(movie_id))
# # # #     return recommended_movies , recommended_movies_poster

# # # # movies_dict = pickle.load(open('movie_dict.pkl','rb'))
# # # # movies = pd.DataFrame(movies_dict)

# # # # similarity = pickle.load(open('similarity.pkl','rb'))

# # # # # Custom CSS styling for modern design
# # # # st.markdown("""
# # # #     <style>
# # # #         body {
# # # #             font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
# # # #             background-image: linear-gradient(120deg, #f6d365 0%, #fda085 100%);
# # # #             color: #333333;
# # # #         }
# # # #         .title {
# # # #             font-size: 36px;
# # # #             font-weight: bold;
# # # #             text-align: center;
# # # #             margin-bottom: 30px;
# # # #             color: #4CAF50;
# # # #         }
# # # #         .movie-title {
# # # #             font-size: 24px;
# # # #             font-weight: bold;
# # # #             text-align: center;
# # # #             margin-bottom: 10px;
# # # #             color: #333333;
# # # #         }
# # # #         .movie-image {
# # # #             display: block;
# # # #             margin-left: auto;
# # # #             margin-right: auto;
# # # #             margin-bottom: 20px;
# # # #             border-radius: 10px;
# # # #             box-shadow: 0px 0px 20px 0px rgba(0,0,0,0.2);
# # # #             transition: transform 0.3s ease-in-out;
# # # #             border: 2px solid #ccc;
# # # #             cursor: pointer;
# # # #         }
# # # #         .movie-image:hover {
# # # #             transform: scale(1.05);
# # # #         }
# # # #     </style>
# # # # """, unsafe_allow_html=True)

# # # # st.title('Movie Recommender System')
# # # # st.markdown("### A modern and visually vibrant movie recommender system using cosine similarity")

# # # # selected_movies_name = st.selectbox(
# # # #     'Select a movie:',
# # # #     movies['title'].values)

# # # # if st.button('Recommend'):
# # # #     names, posters = recommend(selected_movies_name)

# # # #     cols = st.columns(len(posters))

# # # #     for i, (name, poster) in enumerate(zip(names, posters)):
# # # #         with cols[i]:
# # # #             st.image(poster, caption=name, use_column_width=True, output_format='JPEG')
# # # #             st.markdown(f"<a href='https://www.google.com/search?q={'+'.join(name.split())}+movie+watch' target='_blank'><img class='movie-image' src='https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Google_2015_logo.svg/220px-Google_2015_logo.svg.png' width='100' height='100'></a>", unsafe_allow_html=True)
# # # #             st.markdown(f"<a href='https://www.imdb.com/find?q={'+'.join(name.split())}' target='_blank'><img class='movie-image' src='https://upload.wikimedia.org/wikipedia/commons/6/69/IMDB_Logo_2016.svg' width='100' height='100'></a>", unsafe_allow_html=True)
# # # import streamlit as st
# # # import pickle
# # # import pandas as pd
# # # import requests

# # # def fetch_poster(movies_id):
# # #     response=requests.get(f'https://api.themoviedb.org/3/movie/{movies_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US')
# # #     data = response.json()
# # #     return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

# # # def recommend(movie):
# # #     movie_index = movies[movies['title'] == movie].index[0]
# # #     distances = similarity[movie_index]
# # #     movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

# # #     recommended_movies = []
# # #     recommended_movies_poster=[]
# # #     for i in movies_list:
# # #         movie_id = movies.iloc[i[0]].movie_id
# # #         recommended_movies.append(movies.iloc[i[0]].title)
# # #         # fetch poster from API
# # #         recommended_movies_poster.append(fetch_poster(movie_id))
# # #     return recommended_movies , recommended_movies_poster

# # # movies_dict = pickle.load(open('movie_dict.pkl','rb'))
# # # movies = pd.DataFrame(movies_dict)

# # # similarity = pickle.load(open('similarity.pkl','rb'))

# # # # Custom CSS styling for modern design
# # # st.markdown("""
# # #     <style>
# # #         body {
# # #             font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
# # #             background-image: linear-gradient(120deg, #f6d365 0%, #fda085 100%);
# # #             color: #333333;
# # #         }
# # #         .title {
# # #             font-size: 36px;
# # #             font-weight: bold;
# # #             text-align: center;
# # #             margin-bottom: 30px;
# # #             color: #4CAF50;
# # #         }
# # #         .movie-title {
# # #             font-size: 24px;
# # #             font-weight: bold;
# # #             text-align: center;
# # #             margin-bottom: 10px;
# # #             color: #333333;
# # #         }
# # #         .movie-image {
# # #             display: block;
# # #             margin-left: auto;
# # #             margin-right: auto;
# # #             margin-bottom: 20px;
# # #             border-radius: 10px;
# # #             box-shadow: 0px 0px 20px 0px rgba(0,0,0,0.2);
# # #             transition: transform 0.3s ease-in-out;
# # #             border: 2px solid #ccc;
# # #             cursor: pointer;
# # #         }
# # #         .movie-image:hover {
# # #             transform: scale(1.05);
# # #         }
# # #     </style>
# # # """, unsafe_allow_html=True)

# # # st.title('Movie Recommender System')
# # # st.markdown("### A modern and visually vibrant movie recommender system using cosine similarity")

# # # selected_movies_name = st.selectbox(
# # #     'Select a movie:',
# # #     movies['title'].values)

# # # if st.button('Recommend'):
# # #     names, posters = recommend(selected_movies_name)

# # #     cols = st.columns(len(posters))

# # #     for i, (name, poster) in enumerate(zip(names, posters)):
# # #         with cols[i]:
# # #             st.image(poster, caption=name, use_column_width=True, output_format='JPEG')
# # #             st.markdown(f"<a href='https://www.google.com/search?q={'+'.join(name.split())}+movie+watch' target='_blank'><img class='movie-image' src='https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Google_2015_logo.svg/220px-Google_2015_logo.svg.png' width='100' height='100'></a>", unsafe_allow_html=True)
# # #             st.markdown(f"<a href='https://www.imdb.com/find?q={'+'.join(name.split())}' target='_blank'><img class='movie-image' src='https://upload.wikimedia.org/wikipedia/commons/6/69/IMDB_Logo_2016.svg' width='100' height='100'></a>", unsafe_allow_html=True)
# # #             st.markdown(f"<a href='https://www.youtube.com/results?search_query={'+'.join(name.split())}+trailer' target='_blank'><img class='movie-image' src='https://upload.wikimedia.org/wikipedia/commons/4/42/YouTube_icon_%282013-2017%29.png' width='100' height='100'></a>", unsafe_allow_html=True)


# # import streamlit as st
# # import pickle
# # import pandas as pd
# # import requests

# # def fetch_poster(movies_id):
# #     response=requests.get(f'https://api.themoviedb.org/3/movie/{movies_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US')
# #     data = response.json()
# #     return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

# # def recommend(movie):
# #     movie_index = movies[movies['title'] == movie].index[0]
# #     distances = similarity[movie_index]
# #     movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

# #     recommended_movies = []
# #     recommended_movies_poster=[]
# #     for i in movies_list:
# #         movie_id = movies.iloc[i[0]].movie_id
# #         recommended_movies.append(movies.iloc[i[0]].title)
# #         # fetch poster from API
# #         recommended_movies_poster.append(fetch_poster(movie_id))
# #     return recommended_movies , recommended_movies_poster

# # movies_dict = pickle.load(open('movie_dict.pkl','rb'))
# # movies = pd.DataFrame(movies_dict)

# # similarity = pickle.load(open('similarity.pkl','rb'))

# # # Custom CSS styling for modern design
# # st.markdown("""
# #     <style>
# #         body {
# #             font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
# #             background-image: linear-gradient(120deg, #f6d365 0%, #fda085 100%);
# #             color: #333333;
# #         }
# #         .title {
# #             font-size: 36px;
# #             font-weight: bold;
# #             text-align: center;
# #             margin-bottom: 30px;
# #             color: #4CAF50;
# #         }
# #         .movie-title {
# #             font-size: 24px;
# #             font-weight: bold;
# #             text-align: center;
# #             margin-bottom: 10px;
# #             color: #333333;
# #         }
# #         .movie-image {
# #             display: block;
# #             margin-left: auto;
# #             margin-right: auto;
# #             margin-bottom: 20px;
# #             border-radius: 10px;
# #             box-shadow: 0px 0px 20px 0px rgba(0,0,0,0.2);
# #             transition: transform 0.3s ease-in-out;
# #             border: 2px solid #ccc;
# #             cursor: pointer;
# #         }
# #         .movie-image:hover {
# #             transform: scale(1.05);
# #         }
# #     </style>
# # """, unsafe_allow_html=True)

# # st.title('Movie Recommender System')
# # st.markdown("### A modern and visually vibrant movie recommender system using cosine similarity")

# # selected_movies_name = st.selectbox(
# #     'Select a movie:',
# #     movies['title'].values)

# # if st.button('Recommend'):
# #     names, posters = recommend(selected_movies_name)

# #     cols = st.columns(len(posters))

# #     for i, (name, poster) in enumerate(zip(names, posters)):
# #         with cols[i]:
# #             st.image(poster, caption=name, use_column_width=True, output_format='JPEG')
# #             st.markdown(f"<a href='https://www.google.com/search?q={'+'.join(name.split())}+movie+watch' target='_blank'><img class='movie-image' src='https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Google_2015_logo.svg/220px-Google_2015_logo.svg.png' width='100' height='100'></a>", unsafe_allow_html=True)
# #             st.markdown(f"<a href='https://www.imdb.com/find?q={'+'.join(name.split())}' target='_blank'><img class='movie-image' src='https://upload.wikimedia.org/wikipedia/commons/6/69/IMDB_Logo_2016.svg' width='100' height='100'></a>", unsafe_allow_html=True)
# #             st.markdown(f"<a href='https://www.youtube.com/results?search_query={'+'.join(name.split())}+trailer' target='_blank'><img class='movie-image' src='https://upload.wikimedia.org/wikipedia/commons/4/42/YouTube_icon_%282013-2017%29.png' width='100' height='100'></a>", unsafe_allow_html=True)
# #             st.markdown(f"<a href='https://olamovies.life/?s={'+'.join(name.split())}' target='_blank'><img class='movie-image' src='https://freepngimg.com/thumb/download_now_button/25474-1-download-now-button-for-website.png' width='100' height='100'></a>", unsafe_allow_html=True)



# #single option to all 5 recomendations

# # import streamlit as st
# # import pickle
# # import pandas as pd
# # import requests

# # def fetch_poster(movies_id):
# #     response=requests.get(f'https://api.themoviedb.org/3/movie/{movies_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US')
# #     data = response.json()
# #     return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

# # def recommend(movie):
# #     movie_index = movies[movies['title'] == movie].index[0]
# #     distances = similarity[movie_index]
# #     movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

# #     recommended_movies = []
# #     recommended_movies_poster=[]
# #     for i in movies_list:
# #         movie_id = movies.iloc[i[0]].movie_id
# #         recommended_movies.append(movies.iloc[i[0]].title)
# #         # fetch poster from API
# #         recommended_movies_poster.append(fetch_poster(movie_id))
# #     return recommended_movies , recommended_movies_poster

# # movies_dict = pickle.load(open('movie_dict.pkl','rb'))
# # movies = pd.DataFrame(movies_dict)

# # similarity = pickle.load(open('similarity.pkl','rb'))

# # # Custom CSS styling for modern design
# # st.markdown("""
# #     <style>
# #         body {
# #             font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
# #             background-image: linear-gradient(120deg, #f6d365 0%, #fda085 100%);
# #             color: #333333;
# #         }
# #         .title {
# #             font-size: 36px;
# #             font-weight: bold;
# #             text-align: center;
# #             margin-bottom: 30px;
# #             color: #4CAF50;
# #         }
# #         .movie-title {
# #             font-size: 24px;
# #             font-weight: bold;
# #             text-align: center;
# #             margin-bottom: 10px;
# #             color: #333333;
# #         }
# #         .movie-image {
# #             display: block;
# #             margin-left: auto;
# #             margin-right: auto;
# #             margin-bottom: 20px;
# #             border-radius: 10px;
# #             box-shadow: 0px 0px 20px 0px rgba(0,0,0,0.2);
# #             transition: transform 0.3s ease-in-out;
# #             border: 2px solid #ccc;
# #             cursor: pointer;
# #         }
# #         .movie-image:hover {
# #             transform: scale(1.05);
# #         }
# #         .search-options {
# #             display: flex;
# #             justify-content: space-around;
# #             align-items: center;
# #             margin-bottom: 20px;
# #         }
# #     </style>
# # """, unsafe_allow_html=True)

# # st.title('Movie Recommender System')
# # st.markdown("### A modern and visually vibrant movie recommender system using cosine similarity")

# # selected_movies_name = st.selectbox(
# #     'Select a movie:',
# #     movies['title'].values)

# # if st.button('Recommend'):
# #     names, posters = recommend(selected_movies_name)

# #     cols = st.columns(len(posters))

# #     for i, (name, poster) in enumerate(zip(names, posters)):
# #         with cols[i]:
# #             st.image(poster, caption=name, use_column_width=True, output_format='JPEG')

# #     st.markdown("<div class='search-options'>", unsafe_allow_html=True)
# #     st.markdown(f"<a href='https://www.google.com/search?q={'+'.join(selected_movies_name.split())}+movie+watch' target='_blank'><img class='movie-image' src='https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Google_2015_logo.svg/220px-Google_2015_logo.svg.png' width='100' height='100'></a>", unsafe_allow_html=True)
# #     st.markdown(f"<a href='https://www.imdb.com/find?q={'+'.join(selected_movies_name.split())}' target='_blank'><img class='movie-image' src='https://upload.wikimedia.org/wikipedia/commons/6/69/IMDB_Logo_2016.svg' width='100' height='100'></a>", unsafe_allow_html=True)
# #     st.markdown(f"<a href='https://www.youtube.com/results?search_query={'+'.join(selected_movies_name.split())}+trailer' target='_blank'><img class='movie-image' src='https://upload.wikimedia.org/wikipedia/commons/4/42/YouTube_icon_%282013-2017%29.png' width='100' height='100'></a>", unsafe_allow_html=True)
# #     st.markdown(f"<a href='https://olamovies.life/?s=avatar' target='_blank'><img class='movie-image' src='https://upload.wikimedia.org/wikipedia/commons/a/a0/Download_Button.png' width='100' height='100'></a>", unsafe_allow_html=True)
# #     st.markdown("</div>", unsafe_allow_html=True)



# # import streamlit as st
# # import pickle
# # import pandas as pd
# # import requests

# # def fetch_poster(movies_id):
# #     response=requests.get(f'https://api.themoviedb.org/3/movie/{movies_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US')
# #     data = response.json()
# #     return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

# # def recommend(movie):
# #     movie_index = movies[movies['title'] == movie].index[0]
# #     distances = similarity[movie_index]
# #     movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

# #     recommended_movies = []
# #     recommended_movies_poster=[]
# #     for i in movies_list:
# #         movie_id = movies.iloc[i[0]].movie_id
# #         recommended_movies.append(movies.iloc[i[0]].title)
# #         # fetch poster from API
# #         recommended_movies_poster.append(fetch_poster(movie_id))
# #     return recommended_movies , recommended_movies_poster

# # movies_dict = pickle.load(open('movie_dict.pkl','rb'))
# # movies = pd.DataFrame(movies_dict)

# # similarity = pickle.load(open('similarity.pkl','rb'))

# # # Custom CSS styling for modern design
# # st.markdown("""
# #     <style>
# #         body {
# #             font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
# #             background-image: linear-gradient(120deg, #f6d365 0%, #fda085 100%);
# #             color: #333333;
# #         }
# #         .title {
# #             font-size: 36px;
# #             font-weight: bold;
# #             text-align: center;
# #             margin-bottom: 30px;
# #             color: #4CAF50;
# #         }
# #         .movie-title {
# #             font-size: 24px;
# #             font-weight: bold;
# #             text-align: center;
# #             margin-bottom: 10px;
# #             color: #333333;
# #         }
# #         .movie-image {
# #             display: block;
# #             margin-left: auto;
# #             margin-right: auto;
# #             margin-bottom: 20px;
# #             border-radius: 10px;
# #             box-shadow: 0px 0px 20px 0px rgba(0,0,0,0.2);
# #             transition: transform 0.3s ease-in-out;
# #             border: 2px solid #ccc;
# #             cursor: pointer;
# #         }
# #         .movie-image:hover {
# #             transform: scale(1.05);
# #         }
# #         .search-options {
# #             display: flex;
# #             justify-content: space-around;
# #             align-items: center;
# #             margin-bottom: 20px;
# #         }
# #     </style>
# # """, unsafe_allow_html=True)

# # st.title('Movie Recommender System')
# # st.markdown("### A modern and visually vibrant movie recommender system using cosine similarity")

# # selected_movies_name = st.selectbox(
# #     'Select a movie:',
# #     movies['title'].values)

# # if st.button('Recommend'):
# #     names, posters = recommend(selected_movies_name)

# #     cols = st.columns(len(posters))

# #     for i, (name, poster) in enumerate(zip(names, posters)):
# #         with cols[i]:
# #             st.image(poster, caption=name, use_column_width=True, output_format='JPEG')

# #     st.markdown("<div class='search-options'>", unsafe_allow_html=True)
# #     st.markdown(f"<a href='https://www.google.com/search?q={'+'.join(selected_movies_name.split())}+movie+watch' target='_blank'><img class='movie-image' src='https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Google_2015_logo.svg/220px-Google_2015_logo.svg.png' width='100' height='100'></a>", unsafe_allow_html=True)
# #     st.markdown(f"<a href='https://www.imdb.com/find?q={'+'.join(selected_movies_name.split())}' target='_blank'><img class='movie-image' src='https://upload.wikimedia.org/wikipedia/commons/6/69/IMDB_Logo_2016.svg' width='100' height='100'></a>", unsafe_allow_html=True)
# #     st.markdown(f"<a href='https://www.youtube.com/results?search_query={'+'.join(selected_movies_name.split())}+trailer' target='_blank'><img class='movie-image' src='https://upload.wikimedia.org/wikipedia/commons/4/42/YouTube_icon_%282013-2017%29.png' width='100' height='100'></a>", unsafe_allow_html=True)
# #     st.markdown(f"<a href='https://www.netflix.com/search?q={'+'.join(selected_movies_name.split())}' target='_blank'><img class='movie-image' src='https://upload.wikimedia.org/wikipedia/commons/6/69/Netflix_icon.svg' width='100' height='100'></a>", unsafe_allow_html=True)
# #     st.markdown(f"<a href='https://olamovies.life/?s={'+'.join(selected_movies_name.split())}' target='_blank'><img class='movie-image' src='https://upload.wikimedia.org/wikipedia/commons/a/a0/Download_Button.png' width='100' height='100'></a>", unsafe_allow_html=True)
# #     st.markdown("</div>", unsafe_allow_html=True)



# # working on divs - dosent work as expected , try conteners




import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movies_id):
    response=requests.get(f'https://api.themoviedb.org/3/movie/{movies_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US')
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_poster=[]
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        # fetch poster from API
        recommended_movies_poster.append(fetch_poster(movie_id))
    return recommended_movies , recommended_movies_poster

movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

# Custom CSS styling for modern design
st.markdown("""
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-image: linear-gradient(120deg, #f6d365 0%, #fda085 100%);
            color: #333333;
        }
        .title {
            font-size: 36px;
            font-weight: bold;
            text-align: center;
            margin-bottom: 30px;
            color: #4CAF50;
        }
        .movie-title {
            font-size: 24px;
            font-weight: bold;
            text-align: center;
            margin-bottom: 10px;
            color: #FF5733;
        }
        .movie-image {
            display: block;
            margin-left: auto;
            margin-right: auto;
            margin-bottom: 20px;
            box-shadow: 0px 0px 20px 0px rgba(0,0,0,0.2);
            transition: transform 0.3s ease-in-out;
            cursor: pointer;
        }
        .movie-image:hover {
            transform: scale(1.2);
        }
    </style>
""", unsafe_allow_html=True)

st.image('logo.png', use_column_width=True)
st.markdown("### A modern and visually vibrant movie recommender system using cosine similarity")

selected_movies_name = st.selectbox(
    'Select a movie:',
    movies['title'].values)

if st.button('Recommend'):
    names, posters = recommend(selected_movies_name)

    cols = st.columns(len(posters))

    for i, (name, poster) in enumerate(zip(names, posters)):
        with cols[i]:
            st.image(poster, caption=name, use_column_width=True, output_format='JPEG')
            st.markdown(f"<a href='https://www.google.com/search?q={'+'.join(name.split())}+movie+watch' target='_blank'><img class='movie-image' src='https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Google_2015_logo.svg/220px-Google_2015_logo.svg.png' width='100' height='100'></a>", unsafe_allow_html=True)
            st.markdown(f"<a href='https://www.imdb.com/find?q={'+'.join(name.split())}' target='_blank'><img class='movie-image' src='https://upload.wikimedia.org/wikipedia/commons/6/69/IMDB_Logo_2016.svg' width='100' height='100'></a>", unsafe_allow_html=True)
            st.markdown(f"<a href='https://www.youtube.com/results?search_query={'+'.join(name.split())}+trailer' target='_blank'><img class='movie-image' src='https://upload.wikimedia.org/wikipedia/commons/4/42/YouTube_icon_%282013-2017%29.png' width='100' height='100'></a>", unsafe_allow_html=True)
            st.markdown(f"<a href='https://olamovies.life/?s={'+'.join(name.split())}' target='_blank'><img class='movie-image' src='https://freepngimg.com/thumb/download_now_button/25474-1-download-now-button-for-website.png' width='100' height='100'></a>", unsafe_allow_html=True)

# # working on posters