import streamlit as st
import pandas as pd

# Load the dataset
df = pd.read_csv('books_and_genres.csv')

# Genre Parsing Function
def parse_genre_string(genre_string):
    genre_string = genre_string.strip('[]')  # Remove brackets
    genre_string = genre_string.replace("'", "")  # Remove single quotes
    genre_string = genre_string.strip()  # Remove any leading/trailing whitespace
    genres_list = genre_string.split(", ")  # Split into individual genres
    return genres_list

# Book Recommendation Function
def book_response(user_inputs, num_books):
    user_inputs = [input.lower() for input in user_inputs]
    list_of_titles = []

    for index, row in df.iterrows():
        row_genres = parse_genre_string(row['genres'])  # Parse genres for the current row
        for user_input in user_inputs:
            if any(user_input in genre for genre in row_genres):
                list_of_titles.append(row['title'])
                break  # Break the inner loop if a match is found for the current user input

    return list_of_titles[:num_books]  # Return the specified number of recommendations

# Streamlit App
st.title("Collaborative Filtering Book Recommendation System")

# Genre Options
genre_options = [
    'school', 'mystery-thriller', 'manga', 'sports', 'action', 'amazon', 'sociology', 'realistic-fiction', 
    'urban-fantasy', 'self-help', 'theology', 'supernatural', 'relationships', 'comedy', 'historical-fiction', 
    'writing', 'drama', 'unfinished', 'young-adult', 'vampires', '21st-century', 'roman', 'new-adult', 'economics', 
    'essays', 'fiction', 'politics', 'death', 'suspense', 'erotica', 'horror', 'short-stories', 'magic', 'novella', 
    'paranormal-romance', 'teen', 'science-fiction', 'religion', 'dystopia', 'biography', 'love', 'literary-fiction', 
    'historical-romance', 'war', 'graphic-novels', 'coming-of-age', 'thriller', 'crime', 'fantasy', 'dark', 'plays', 
    'music', 'adventure', 'comics', 'read-for-school', 'spirituality', 'cookbooks', 'business', 'family', 'christmas', 
    'adult', 'reference', 'childrens', 'poetry', 'contemporary-romance', 'psychology', 'contemporary', 'science', 
    'picture-books', 'christian', 'literature', 'history', 'chick-lit', 'animals', 'bdsm', 'feminism', 'historical', 
    'mythology', 'romance', 'romantic-suspense', 'mystery', 'classics', 'paranormal', 'humor', 'education', 'modern', 
    'non-fiction', 'college', 'speculative-fiction', 'lgbt', '20th-century', 'middle-grade', 'adult-fiction', 'art', 
    'philosophy', 'memoir', 'novels', 'high-school', 'american', 'travel'
]

# User selects genres
selected_genres = st.multiselect("Select Genres", genre_options)

# User inputs the number of books to recommend
num_books = st.number_input("Number of books to recommend", min_value=1, max_value=20, value=10, step=1)

# Get recommendations based on selected genres
if selected_genres:
    recommendations = book_response(selected_genres, num_books)
    if recommendations:
        st.write("Top book recommendations:")
        for title in recommendations:
            st.write(f"- {title}")
    else:
        st.write("No recommendations found for the selected genres.")

