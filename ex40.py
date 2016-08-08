class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        print "\n"
        for line in self.lyrics:
            print line

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

jake_bugg = (["I go back to Clifton to see my old friends", 
                    "The best people I could ever have met",
                    "Skin up a fat one, hide from the Feds", 
                    "Something is changing, changing, changing"])



happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

Song(jake_bugg).sing_me_a_song()