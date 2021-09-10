import sqlalchemy

# создаем подключение к базе данных
engine = sqlalchemy.create_engine('postgresql://naum_1:123456@localhost:5432/music_sait_2')
connection = engine.connect()

# заносим данные в таблицу жанры
lists_genres = ['hip-hop', 'jazz', 'blues', 'country', 'rock', 'pop', 'R&B']
i = 1
for name in lists_genres:
    connection.execute(f"""INSERT INTO genres(id, name) VALUES({i}, '{name}');""")
    i += 1

# заносим данные в таблицу исполнителя
lists_performers = ['Eminem', 'Coolio', 'Albert Ayler', 'Anthony Braxton', 'B.B. King', 'Ray Charles',
                    'Johnny Cash', 'Dolly Parton', 'Led Zeppelin', 'Queen', 'Justin Bieber', 'Taylor Swift']
i = 1
for name in lists_performers:
   connection.execute(f"""INSERT INTO performers(id, name) VALUES({i}, '{name}');""")
   i += 1

lists_performers_1 = [['Eminem', 'Coolio'], ['Albert Ayler', 'Anthony Braxton'], ['B.B. King', 'Ray Charles'],
                    ['Johnny Cash', 'Dolly Parton'], ['Led Zeppelin', 'Queen']]
# заносим данные в таблицу исполнителижанры
i = 1
j = 1
for list_1 in lists_performers_1:
    for list_2 in range(len(list_1)):
        connection.execute(f"""INSERT INTO performersgenres(genres_id, performers_id) VALUES({j}, {i});""")
        i += 1
    j += 1

lists_performers_2 = [[11, 6], [11, 7], [12, 6], [12, 4]]
for list_3 in lists_performers_2:
    connection.execute(f"""INSERT INTO performersgenres(genres_id, performers_id) VALUES({list_3[1]}, {list_3[0]});""")


# заносим данные в таблицу альбомы
lists_albums = [['Kamikaze', 2018], ['The Very Best', 2001], ['Something Different!!!!!!', 1963],
                ['Donna Lee', 2004], ['King Of The Blues', 1960], ['Hall Of Fame', 2004], ['At Folsom Prison', 1968],
                ["Hello, I''m Dolly", 1967], ['Led Zeppelin III', 1970], ['Innuendo', 1991],
                ['Changes', 2020], ['Lover', 2019]]
i = 1
for list in lists_albums:
    connection.execute(f"""INSERT INTO albums(id, title, year_of_issue) VALUES({i}, '{list[0]}', {list[1]});""")
    i += 1


# заносим данные в таблицу альбомыисполнители
i = 1
for list_1 in range(len(lists_albums)):
    connection.execute(f"""INSERT INTO albumsperformers(albums_id, performers_id) VALUES({i}, {i});""")
    i += 1

# заносим данные в таблицу треки
lists_tracks = [[['The Ringer', 337], ['Normal', 222]],
                [["Gangsta''s Paradise", 240], ['DOoh La La La', 246]],
                [['Tune Up', 333], ["I''ll Remember April", 1061]],
                [['Donna Lee - Instrumental', 550], ["You Got To My Head - Part 1", 378]],
                [['What A Way To Go', 185], ['Good Man Gone Bad', 170]],
                [['Kiss Me Baby', 184], ["I''m Movin'' On", 136]], [['The Wall', 68], ['I Got Stripes', 125]],
                [['I Wasted My Tears', 138], ['The Little Things', 145]],
                [['Immigrant Song', 143], ['Out on the Tiles', 245]],
                [["Innuendo", 389], ['The Show Must Go On', 264]],
                [['All Around Me', 136], ['Confirmation', 170]],
                [['I Think He Knows', 173]]]
i = 1
j = 1
for list in lists_tracks:
    for list_1 in list:
        connection.execute(f"""INSERT INTO tracks(id, name_track, duration, albums_id) VALUES({j}, 
        '{list_1[0]}', {list_1[1]}, {i});""")
        j += 1
    i += 1

# заносим данные в таблицу сборники
lists_collections = [['collections_1', 2018], ['collections_2', 2019], ['collections_3', 2020],
                     ['collections_4', 2020], ['collections_5', 2020], ['collections_6', 2017],
                     ['collections_7', 2021], ["collections_8", 2021]]
i = 1
for list in lists_collections:
    connection.execute(f"""INSERT INTO collections(id, title, year_of_issue) VALUES({i}, '{list[0]}', {list[1]});""")
    i += 1

# формируем список id треков в сборниках
l = []
for list in lists_tracks:
    for list_1 in list:
        l.append(list_1[0])
list_tracks_for_collections = [[1, 4, 10, 11, 20], [5, 6, 8, 16], [3, 7, 14, 15, 19],
                               [1, 2, 4, 12, 17,], [1, 8, 15, 18, 23], [3, 5, 8, 11, 16],
                               [1, 4, 7, 12, 14, 20], [3, 5, 12, 17, 18, 19, 22]]

# заносим данные в таблицу трекисборники
i = 1
for list in list_tracks_for_collections:
    for list_1 in list:
        connection.execute(f"""INSERT INTO trackscollections(tracks_id, collections_id) VALUES({list_1}, {i});""")
    i += 1

