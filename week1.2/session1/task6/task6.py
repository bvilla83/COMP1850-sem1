# Week 1.2, Session 1: Task 6

from pprint import pprint

# Create music database, as a dictionary of strings mapped to lists
# (keys are artist names, values are lists of album names)

MUSIC_DATABASE = {
    "Post Malone": ["August 26", "F-1 Trillion: Long Bed", "AUSTIN", "Hollywood's Bleeding"],
    "keshi": ["Requiem", "GABRIEL"],
    "Pino": ["\'02", "introspect"],
    "Bruno Mars": ["The Romantic", "An Evening with Silk Sonic", "24K Magic", "Unorthodox Jukebox", "Doo-Wops & Hooligans"]
}

# Pretty-print the data structure

pprint(MUSIC_DATABASE)

# Display details of one album recorded by a specific artist

album_input = input("Enter an album name: ")

for artist, album_list in MUSIC_DATABASE.items():
    if album_input in album_list:
        print(f"{album_input} by {artist}")
        break