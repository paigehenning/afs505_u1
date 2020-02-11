yourstuff={'apple':"I AM APPLES!"}
print(yourstuff['apple'])

import mystuff
mystuff.apple()
print(mystuff.tangerine)
#dictionary style
yourstuff['apple']
#module style
mystuff.apple()
mystuff.tangerine
class MyStuff(object):
    def __init__(self):
        self.tangerine="And now a thousand years between"
    def apple(self):
        print("I AM CLASSY APPLES!")
#class style
thing=MyStuff()
thing.apple()
print(thing.tangerine)
