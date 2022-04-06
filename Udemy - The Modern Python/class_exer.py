class Music:

    music_playlist = 0

    def __init__(self, artist, title, year):
        self.artist = artist
        self.title = title
        self.year = year
        Music.music_playlist += 1
    
    def info(self):
        return f"Artist: {self.artist}\nTitle: {self.title}\nYear Released: {self.year}"

    def style(self, genre):
        return f"{self.artist} - {genre}"

song1 = Music('Radiohead', 'Ful Stop', 2016)
song2 = Music('Muse', "Won't Stand Down", 2022)
song3 = Music('Atoms for peace', 'AMOK', 2014)

# print(song1.info())
# print(song2.info())
# print(Music.music_playlist)
print(song3.style('Electronic'))
