from playsound import playsound
import os


#Path of music folder 
root = r'F:\Novels'

songs = os.listdir(path=root)

for x in songs:
    print(x)

ch = int(input("Enter your choice"))

songPath = root + '\\' + songs[ch-1]

playsound(songPath)
