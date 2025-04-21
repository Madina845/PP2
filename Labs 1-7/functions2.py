movies = [
    {"name": "Usual Suspects", "imdb": 7.0, "category": "Thriller"},
    {"name": "Hitman", "imdb": 6.3, "category": "Action"},
    {"name": "Dark Knight", "imdb": 9.0, "category": "Adventure"},
    {"name": "The Help", "imdb": 8.0, "category": "Drama"},
    {"name": "The Choice", "imdb": 6.2, "category": "Romance"},
    {"name": "Colonia", "imdb": 7.4, "category": "Romance"},
    {"name": "Love", "imdb": 6.0, "category": "Romance"},
    {"name": "Bride Wars", "imdb": 5.4, "category": "Romance"},
    {"name": "AlphaJet", "imdb": 3.2, "category": "War"},
    {"name": "Ringing Crime", "imdb": 4.0, "category": "Crime"},
    {"name": "Joking muck", "imdb": 7.2, "category": "Comedy"},
    {"name": "What is the name", "imdb": 9.2, "category": "Suspense"},
    {"name": "Detective", "imdb": 7.0, "category": "Suspense"},
    {"name": "Exam", "imdb": 4.2, "category": "Thriller"},
    {"name": "We Two", "imdb": 7.2, "category": "Romance"}
]

# 1. Checks if a movie's IMDb rating is above 5.5
def is_high_rated(movie):
    return movie["imdb"] > 5.5

# Returns a list of movies with IMDb rating above 5.5
def high_rated_movies(movie_list):
    return [movie for movie in movie_list if movie["imdb"] > 5.5]

# Returns movies by category
def movies_by_category(category, movie_list):
    return [movie for movie in movie_list if movie["category"] == category]

# Calculates the average IMDb rating for a list of movies
def average_imdb(movie_list):
    if not movie_list:
        return 0  
    return sum(movie["imdb"] for movie in movie_list) / len(movie_list)

#  Calculates the average IMDb rating for a given category
def average_imdb_by_category(category, movie_list):
    filtered_movies = movies_by_category(category, movie_list)
    return average_imdb(filtered_movies)

# Print function outputs in a readable format
def print_results(results):
    for key, value in results.items():
        print(f"{key}:")
        print(value, "\n")

results = {
    "is_high_rated(Usual Suspects)": is_high_rated(movies[0]),  # True
    "is_high_rated(AlphaJet)": is_high_rated(movies[8]),  # False
    "high_rated_movies": high_rated_movies(movies),  # Все фильмы с imdb > 5.5
    "movies_by_category(Romance)": movies_by_category("Romance", movies),  # Все фильмы в категории "Romance"
    "average_imdb(movies)": average_imdb(movies),  # Средний рейтинг всех фильмов
    "average_imdb_by_category(Thriller)": average_imdb_by_category("Thriller", movies),  # Средний рейтинг в категории "Thriller"
}

print_results(results)