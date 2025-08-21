
# __str__() method
# This method is used when you print an object. It gives a nice readable string instead of default memory location.


class Student:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Student Name: {self.name}"

s = Student("Ali")
print(s)



# 3. __len__() Method
# Used when you call len() on an object. You can define what length means for your object.

class Playlist:
    def __init__(self, songs):
        self.songs = songs

    def __len__(self):
        return len(self.songs)

p = Playlist(["Song1", "Song2", "Song3"])
print(len(p))