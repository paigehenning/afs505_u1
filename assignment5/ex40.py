class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)
happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])
bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])
teen_spirit=Song(["With the lights out, it's less dangerous",
                    "Here we are now, entertain us",
                    "I feel stupid, and contagious",
                    "Here we are now, entertain us"])
all_apologies=Song(["I wish I was like you",
                    "Easily amused",
                    "Find my nest of salt",
                    "Everythings my fault",])
happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

nirvana={                         #I tried to use dictionaries, but failed :(
        "1991":"teen_spirit",
        "1993":"all_apologies"
}
popular91=teen_spirit
print(" ")
print("Here's ",nirvana['1991'],"by Nirvana!")
print(" ")
popular91.sing_me_a_song()
print(" ")
print("Following their 1991 classic ",nirvana['1991']," Nirvana produced",nirvana['1993'],":")
print(" ")
popular93=all_apologies
popular93.sing_me_a_song()
