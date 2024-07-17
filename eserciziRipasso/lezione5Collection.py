# 1. Create a Playlist:

# Write a function called create_playlist() that accepts a playlist name and a variable number of song titles. 
# The function should return a dictionary with the playlist name and a set of songs. 
# Call the function with different numbers of songs to demonstrate flexibility.

# Example: create_playlist("Road Trip", {"Song 1", "Song 2"})

# Write a function called add_like() that accepts a dictionary, the name of a playlist, 
# and a boolean value indicating whether it is liked (True or False). This function should return an updated dictionary.

# Example: add_like(dictionary, “Road Trip”, liked=True)

def create_playlist(playlist_name:str, songs:list[str]):
    dict_playlist = {}
    dict_playlist[playlist_name] = {'songs':set(songs)}
    return dict_playlist

def add_like (dictionary:dict, playlist_name:str, liked:bool):
    if playlist_name in dictionary:
        dictionary[playlist_name]['like']=liked
    else:
        dictionary[playlist_name] = {'songs':set(), 'liked':liked}
    return dictionary

playlist1 = create_playlist('frenk', ['song 1', 'song 2', 'song  3'])
playlist2 = create_playlist('chill mood',['song 1', 'song 2'])

all_playlists = {}

all_playlists.update(playlist1)
all_playlists.update(playlist2)

all_playlists = add_like(all_playlists, 'frenk', liked=True)
all_playlists = add_like(all_playlists, 'chill mood', liked= False)

print(all_playlists)