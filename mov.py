import json
def read_movie_data(filename):
    with open(filename, 'r') as file:
        return json.load(file)

def analyze_movies(movies):
    print("Movie Titles:", [movie['title'] for movie in movies])

    print("............................................................................")

    print("\nChristopher Nolan Movies:", [movie['title'] for movie in movies if (movie['director']['first_name'], movie['director']['last_name']) == ('Christopher', 'Nolan')])
    
    print("............................................................................")
    
    print("\nMovies Released After 2000:", [movie['title'] for movie in movies if movie['year'] > 2000])

    print("............................................................................")
    
    genres = set(genre for movie in movies for genre in movie['genres'])
    print("\nUnique Genres:", genres)
    
    print("............................................................................")
    
    directors = set(f"{movie['director']['first_name']} {movie['director']['last_name']}" for movie in movies)
    print("\nDirectors:", directors)
    
    print("............................................................................")

    cast_members = {movie['title']: [f"{actor['actor']} as {actor['role']}" for actor in movie['cast']] for movie in movies}
    print("\nCast Members:")
    for title, cast in cast_members.items():
        print(title, cast)
        print("............................................................................")

    genre_counts = {}
    for movie in movies:
        for genre in movie['genres']:
            genre_counts[genre] = genre_counts.get(genre, 0) + 1
    print("\nGenre Movie Counts:", genre_counts)

    print("............................................................................")

    print("\nMovies with Multiple Genres:", [movie['title'] for movie in movies if len(movie['genres']) > 1])
    
    print("............................................................................")

    actors_and_roles = {}
    for movie in movies:
        for actor in movie['cast']:
            actors_and_roles.setdefault(actor['actor'], []).append(actor['role'])
    print("\nActors and Roles:")
    for actor, roles in actors_and_roles.items():
        print(actor, roles)
    print("............................................................................")
    
    print("\nMovies in 1990s:", [movie['title'] for movie in movies if 1990 <= movie['year'] <= 1999])

    print("............................................................................")
    
    print("\nMovies with Drama Genre:", [movie['title'] for movie in movies if 'Drama' in movie['genres']])
    
    print("............................................................................")
    
    print("\nMovies and Release Years:", [(movie['title'], movie['year']) for movie in movies])

filename='movies.json'
movies =read_movie_data(filename)
analyze_movies(movies)
