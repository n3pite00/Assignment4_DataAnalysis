import streamlit as st
import pandas as pd


st.title("Netflix titles: Movies and TV-shows")

data = pd.read_csv("netflix_titles.csv")
st.write(data)

movie_data = data[data["type"] == "Movie"]
TV_Show_data = data[data["type"] == "TV Show"]



st.header("Netflix content summary")
col1, col2, col3 = st.columns(3)
col1.metric("Total Titles", len(data), border=True)
col2.metric("Total Movies", len(movie_data), border=True)
col3.metric("Total TV shows", len(TV_Show_data), border=True)

Movie_per_year = movie_data["release_year"].value_counts().reset_index()
Movie_per_year.columns = ["Year", "Movies"]
Movie_per_year = Movie_per_year.sort_values("Year")


st.header("Most movies offered by release year")
st.bar_chart(Movie_per_year, x="Year", y="Movies")

data["date_added"] = pd.to_datetime(data["date_added"], errors='coerce')
ReleaseYear = data["date_added"].dt.year.dropna().astype(int)


AddedYears = ReleaseYear.value_counts().reset_index()
AddedYears.columns = ["Year", "Amount"]
AddedYears = AddedYears.sort_values("Year")



st.header("Netflix content growth over the years")
is_clicked = st.button("Click for line chart")
if is_clicked:
    st.line_chart(AddedYears, x="Year", y="Amount")



st.header("Filter data!") 

filtered_type = st.radio("Choose type", 
        ["All", "Movie", "TV Show"], 
        index=0)
if filtered_type == "All":
    filter_data = data
    
else:
    filter_data = data[data["type"] == filtered_type]
    
st.write(filter_data)