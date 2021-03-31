def make_album(singer_name, album_name, song_quantity=None):
    album_info = {'singer': singer_name, 'album': album_name}
    if song_quantity:
        album_info['quantity'] = song_quantity
    return album_info

while True:
    print("\nPlease tell me your favorite singer and his/her album:")
    print("(enter 'esc' to quit at any time)")

    s_name = input("your favorite singer name: ")
    if s_name == 'esc':
        break
    a_name = input("his/her album: ")
    if a_name == 'esc':
        break

    user_album = make_album(s_name,a_name)
    print(user_album)