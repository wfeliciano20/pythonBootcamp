movies = []


def add_movies(movie):
    movies.append(movie)


def list_movies():
    if len(movies) == 0:
        print("There are no movies in the collection.")
    else:
        for movie in movies:
            print_movie(movie)


def print_movie(movie):
    print(
        f'{movie["name"]} was directed by {movie["director"]} in the year {movie["release_year"]}.')


def find_movie(name):
    exist = False
    for movie in movies:
        if movie["name"].lower() == name.lower():
            exist = True
            print_movie(movie)
    if not exist:
        print('The movie is not in the collection')


MENU_PROMPT = "\nEnter 'a' to add a movie,'l' to see your movies,'f' to find a movie by title, or 'q' to quit "


def menu():
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection == 'a':
            movie_name = input("Enter the movie name: ")
            movie_director = input("Enter the movie director: ")
            movies_release_year = input("Enter the movie release year: ")

            movie = {
                "name": movie_name,
                "director": movie_director,
                "release_year": movies_release_year
            }
            add_movies(movie)
        elif selection == 'l':
            list_movies()
        elif selection == 'f':
            movie_to_find = input(
                "Enter the name of the movie you want to look up: ")
            find_movie(movie_to_find)
        else:
            print('Unknown command. Please try again.')
        selection = input(MENU_PROMPT)


menu()
