class animal:
    def __init__(self):
        self.sound = "annoying"
    
class cat(animal):
    def __init__(self):
        super().__init__
        self.cat_voice()

    def cat_voice(self):
        self.sound = "meow"

asc = cat()
print(asc.sound)            