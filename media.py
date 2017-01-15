import webbrowser


# movie class
class Movie():
    """ This class provies a way to store movie related information

    Attributes:
        title (str): This is the title of the movie
        storyline (str): This is the storyline of the movie
        poster_image_url (str): This is the movie poster as an URL
        trailer_youtube_url (str): This is the trailer video URL

    Method:
        show_trailer(): open the movie trailer in the browser
    """

    # movie constructor
    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # open a webbrowser to play trailer of the movie
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
