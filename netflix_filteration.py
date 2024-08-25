import pandas as pd
import numpy as np

pd.set_option('display.max_columns', None)

# Read in the Netflix CSV as a DataFrame
netflix_df = pd.read_csv("netflix_data.csv")

# Filter for movies only
movies_only = netflix_df[netflix_df["type"] == "Movie"]
movies_of_selected_year = movies_only[(movies_only["release_year"] > 1989) & (movies_only["release_year"] < 2000)]

Action_movies=movies_of_selected_year[movies_of_selected_year["genre"]=="Action"]
short_movie_coun=Action_movies[Action_movies["duration"]<90]
short_movie_count=short_movie_coun["title"].count()

# Filter movies with a duration greater than 90 minutes
long_movie_coun = movies_of_selected_year[movies_of_selected_year["duration"] > 90]
# Filter movies released between 1990 and 1999

# Find the most frequent movie duration in the 1990s
duration = int(long_movie_coun["duration"].mode()[0])

print("The most frequent movie duration in the 1990s:", duration)
