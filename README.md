# Collaborative Filtering Book Recommendation System

This is a book recommendation system built using Streamlit and Pandas. The application allows users to select their preferred genres and specify the number of book recommendations they would like to receive based on those genres.
To Visit the App Follow the [Link](https://collaborative-filtering-book-recommendation-appgit-k2ua8ygzf7h.streamlit.app/)
## What is Collaborative Filtering?

Collaborative Filtering is a technique used in recommendation systems to make predictions about a user's interests by collecting preferences from many users. The basic idea is that if two users have similar preferences in the past, they are likely to have similar preferences in the future. There are two main types of collaborative filtering:

1. **User-based Collaborative Filtering**: Recommends items based on the preferences of similar users.
2. **Item-based Collaborative Filtering**: Recommends items that are similar to items the user has liked in the past.

In the context of this application, the recommendation system is based on matching genres selected by the user with genres associated with books in the dataset. Although not a traditional collaborative filtering method, it follows a similar principle of recommending items based on user preferences.

## How the App Works

1. **Select Genres**: 
   Users can choose one or more genres from a provided list.

2. **Set the Number of Recommendations**:
   Users can specify how many book recommendations they want to receive (between 1 and 20).

3. **View Recommendations**:
   The app processes the selected genres and provides a list of book recommendations that match the selected genres.
