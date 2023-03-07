from Data import movies
def foundamovies(Name):

    director = " "
    genre = " "
    year =  " "
    rating =  " "

    for i in range(len(movies)):
        if Name == movies[i].get("title"):
            print("The movies is collected in our data-base system and this is a list of recommended movies")
            director = movies[i].get("director")
            genre = movies[i].get("genre")
            year = movies[i].get("year")
            rating = movies[i].get("rating")
            movies[i].clear()
            # print(director , genre)
        else:
            print("we dont have a data depend on this movies ")
        break
    for i in range(len(movies)):
        if movies[i].get("director") == director:
            print(movies[i])
            movies[i].clear()
        if movies[i].get("genre") == genre:
            print(movies[i])
            movies[i].clear()
        if movies[i].get("rating") == rating:
            print(movies[i])
            movies[i].clear()
        if movies[i].get("year") == year:
            print(movies[i])
            movies[i].clear()