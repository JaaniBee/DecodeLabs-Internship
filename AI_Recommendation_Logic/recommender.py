import math

# A built-in dataset of movies and their genres
MOVIES_DATA = [
    {"id": 1, "title": "The Matrix", "genres": ["Action", "Sci-Fi"]},
    {"id": 2, "title": "Inception", "genres": ["Action", "Adventure", "Sci-Fi", "Thriller"]},
    {"id": 3, "title": "The Dark Knight", "genres": ["Action", "Crime", "Drama", "Thriller"]},
    {"id": 4, "title": "Pulp Fiction", "genres": ["Crime", "Drama"]},
    {"id": 5, "title": "Forrest Gump", "genres": ["Drama", "Romance"]},
    {"id": 6, "title": "The Shawshank Redemption", "genres": ["Drama"]},
    {"id": 7, "title": "The Avengers", "genres": ["Action", "Adventure", "Sci-Fi"]},
    {"id": 8, "title": "Titanic", "genres": ["Drama", "Romance"]},
    {"id": 9, "title": "Toy Story", "genres": ["Animation", "Adventure", "Comedy", "Family"]},
    {"id": 10, "title": "The Lion King", "genres": ["Animation", "Adventure", "Drama", "Family"]},
    {"id": 11, "title": "Spirited Away", "genres": ["Animation", "Adventure", "Family", "Fantasy"]},
    {"id": 12, "title": "Interstellar", "genres": ["Adventure", "Drama", "Sci-Fi"]},
    {"id": 13, "title": "Gladiator", "genres": ["Action", "Adventure", "Drama"]},
    {"id": 14, "title": "Jurassic Park", "genres": ["Action", "Adventure", "Sci-Fi", "Thriller"]},
    {"id": 15, "title": "The Silence of the Lambs", "genres": ["Crime", "Drama", "Thriller"]},
    {"id": 16, "title": "Superbad", "genres": ["Comedy"]},
    {"id": 17, "title": "The Hangover", "genres": ["Comedy"]},
    {"id": 18, "title": "Knives Out", "genres": ["Comedy", "Crime", "Drama", "Mystery"]},
    {"id": 19, "title": "Mad Max: Fury Road", "genres": ["Action", "Adventure", "Sci-Fi"]},
    {"id": 20, "title": "La La Land", "genres": ["Comedy", "Drama", "Music", "Romance"]},
]

def get_all_genres():
    """Extracts a sorted list of all unique genres available in the dataset."""
    genres_set = set()
    for movie in MOVIES_DATA:
        for genre in movie["genres"]:
            genres_set.add(genre)
    return sorted(list(genres_set))

def calculate_jaccard_similarity(user_genres, movie_genres):
    """
    Calculates the Jaccard Similarity between user preferred genres and a movie's genres.
    Jaccard Similarity = (Intersection of sets) / (Union of sets)
    """
    set1 = set(user_genres)
    set2 = set(movie_genres)
    
    intersection = set1.intersection(set2)
    union = set1.union(set2)
    
    if not union:
        return 0.0
        
    return len(intersection) / len(union)

def recommend_movies(user_preferred_genres, top_n=5):
    """
    Recommends top N movies based on user's preferred genres.
    Returns a list of tuples: (movie_dict, similarity_score)
    """
    if not user_preferred_genres:
        return []

    # Standardize inputs to title case
    user_genres_standardized = [g.strip().title() for g in user_preferred_genres]
    
    scored_movies = []
    
    for movie in MOVIES_DATA:
        score = calculate_jaccard_similarity(user_genres_standardized, movie["genres"])
        if score > 0: # Only include movies that have at least some match
            scored_movies.append((movie, score))
            
    # Sort by score descending. If scores are equal, sort alphabetically by title.
    scored_movies.sort(key=lambda x: (-x[1], x[0]["title"]))
    
    return scored_movies[:top_n]
