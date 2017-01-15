import media
import fresh_tomatoes

# create movie instances sequentially
star_wars_1 = media.Movie("Star Wars: Episode I - The Phantom Menace",
                          "Anakin started to show talent for the force",
                          "https://upload.wikimedia.org/wikipedia/en/4/40/Star_Wars_Phantom_Menace_poster.jpg",  # NOQA
                          "https://www.youtube.com/watch?v=bD7bpG-zDJQ")

star_wars_2 = media.Movie("Star Wars: Episode II - Attack of the Clones",
                          "Romantic meeting beween Anakin and Padme",
                          "https://upload.wikimedia.org/wikipedia/en/3/32/Star_Wars_-_Episode_II_Attack_of_the_Clones_%28movie_poster%29.jpg",  # NOQA
                          "https://www.youtube.com/watch?v=CO2OLQ2kiq8")

star_wars_3 = media.Movie("Star Wars: Episode III - Revenge of the Sith",
                          "Jedi Knight was corrupted to become Sith",
                          "https://upload.wikimedia.org/wikipedia/en/9/93/Star_Wars_Episode_III_Revenge_of_the_Sith_poster.jpg",  # NOQA
                          "https://www.youtube.com/watch?v=5UnjrG_N8hU")

star_wars_4 = media.Movie("Star Wars: Episode IV - A New Hope",
                          "Luke Skywalker destroyed the Death Star",
                          "https://upload.wikimedia.org/wikipedia/en/8/87/StarWarsMoviePoster1977.jpg",  # NOQA
                          "https://www.youtube.com/watch?v=vZ734NWnAHA")

star_wars_5 = media.Movie("Star Wars: Episode V - The Empire Strikes Back",
                          "Father and Son fought for belief",
                          "https://upload.wikimedia.org/wikipedia/en/3/3c/SW_-_Empire_Strikes_Back.jpg",  # NOQA
                          "https://www.youtube.com/watch?v=JNwNXF9Y6kY")

star_wars_6 = media.Movie("Star Wars: Episode VI - Return of the Jedi",
                          "Bye bye, Darth Vader",
                          "https://upload.wikimedia.org/wikipedia/en/b/b2/ReturnOfTheJediPoster1983.jpg",  # NOQA
                          "https://www.youtube.com/watch?v=CsDwpF3uiZI")

# create a list to store all the movie instances
movies = [star_wars_1, star_wars_2, star_wars_3,
          star_wars_4, star_wars_5, star_wars_6]

# create the web page, passing movie list as the parameter
fresh_tomatoes.open_movies_page(movies)
