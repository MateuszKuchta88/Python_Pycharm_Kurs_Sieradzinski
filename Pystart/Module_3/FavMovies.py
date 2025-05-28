movies =    [
                {
                    "title" : "The Lord of the Rings",
                    "director" : "Peter Jackson",
                    "year" : 2003
                },
                {
                    "title" : "IO",
                    "director" : "Jerzy Skolimowski",
                    "year" : 2022
                },
                {
                    "title" : "Alien",
                    "director" : "Steven Spielberg",
                    "year" : 2001
                }
            ]

for movie in movies:
    print(movie["director"])
    if movie["director"] == "Steven Spielberg":
        del movie["director"]
        del movie["title"]
        del movie["year"]
print(movies)