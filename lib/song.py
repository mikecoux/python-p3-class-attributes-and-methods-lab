class Song:
    count = 0
    artists = set()
    genres = set()
    genre_count = dict()
    artist_count = dict()

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)

    @classmethod
    def add_song_to_count(cls):
        Song.count += 1

    @classmethod
    def add_to_artists(cls, name):
        Song.artists.add(name)

    @classmethod
    def add_to_genres(cls, genre):
        Song.genres.add(genre)

    @classmethod
    def add_to_genre_count(cls, genre):
        if Song.genre_count.get(genre):
            print('adding')
            Song.genre_count[genre] += 1
        else:
            print('new')
            Song.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls, artist):
        if Song.artist_count.get(artist):
            print('adding')
            Song.artist_count[artist] += 1
        else:
            print('new')
            Song.artist_count[artist] = 1

# out_of_touch = Song("Out of Touch", "Hall and Oates", "Pop")
# genre = 'Pop'
# print(genre in Song.genres)