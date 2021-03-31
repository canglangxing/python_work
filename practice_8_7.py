def make_album(singer_name, album_name, song_quantity=None):
    album_info = {'singer': singer_name, 'album': album_name}
    if song_quantity:
        album_info['quantity'] = song_quantity
    return album_info

Jay = make_album('Jay Chou', 'Jay')
print(Jay)

Scary_Hours_2 = make_album('Drake', 'Scary Hours 2', 3)
print(Scary_Hours_2)

Bad = make_album('Michael Jackson', 'Bad')
print(Bad)