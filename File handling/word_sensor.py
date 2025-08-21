word="donkey"

with open("sensoring_file.txt", "r") as f:
    content=f.read()


newcontent=content.replace(word,"######")

with open("sensoring_file.txt", "w") as f:
    f.write(newcontent)