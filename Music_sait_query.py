import sqlalchemy

# создаем подключение к базе данных
engine = sqlalchemy.create_engine('postgresql://naum_1:123456@localhost:5432/music_sait_2')
connection = engine.connect()

# запрос - количество исполнителей в каждом жанре
print(connection.execute("""SELECT g.name, COUNT(p.id) FROM genres g 
LEFT JOIN performersgenres pg ON g.id = pg.genres_id
LEFT JOIN performers p ON pg.performers_id = p.id
GROUP BY g.name
;""").fetchall())

# запрос - количество треков, вошедших в альбомы 2019-2020 годов
print(connection.execute("""SELECT COUNT(t.id) FROM albums a 
LEFT JOIN tracks t ON  a.id = t.albums_id
WHERE a.year_of_issue BETWEEN 2019 AND 2020
;""").fetchall())

# запрос - средняя продолжительность треков по каждому альбому
print(connection.execute("""SELECT a.title, AVG(t.duration) FROM albums a 
LEFT JOIN tracks t ON  a.id = t.albums_id
GROUP BY a.title
;""").fetchall())

# запрос - все исполнители, которые не выпустили альбомы в 2020 году
print(connection.execute("""SELECT p.name FROM performers p 
LEFT JOIN albumsperformers ap ON  p.id = ap.performers_id
LEFT JOIN albums a ON  ap.albums_id = a.id
WHERE a.year_of_issue != 2020
;""").fetchall())

# запрос - названия сборников, в которых присутствует конкретный исполнитель Coolio
print(connection.execute("""SELECT c.title FROM collections c 
LEFT JOIN trackscollections tc ON  c.id = tc.collections_id
LEFT JOIN tracks t ON  tc.tracks_id = t.id
LEFT JOIN albums a ON  t.albums_id = a.id
LEFT JOIN albumsperformers ap ON  a.id = ap.albums_id
LEFT JOIN performers p ON  ap.performers_id = p.id
WHERE p.name = 'Coolio'
;""").fetchall())

# запрос - название альбомов, в которых присутствуют исполнители более 1 жанра
print(connection.execute("""SELECT a.title FROM albums a
LEFT JOIN albumsperformers ap ON a.id = ap.albums_id
LEFT JOIN performers p ON ap.performers_id = p.id
LEFT JOIN performersgenres pg ON p.id = pg.performers_id
GROUP BY a.title
HAVING COUNT(pg.genres_id) > 1
;""").fetchall())

# запрос - наименование треков, которые не входят в сборники
print(connection.execute("""SELECT t.name_track FROM tracks t
LEFT JOIN trackscollections tc ON t.id = tc.tracks_id
GROUP BY t.name_track
HAVING COUNT(tc.collections_id) = 0
;""").fetchall())

# запрос - исполнитель(-и), написавший самый короткий по продолжительности трек
print(connection.execute("""SELECT p.name FROM performers p
LEFT JOIN albumsperformers ap ON p.id = ap.performers_id
LEFT JOIN albums a ON ap.albums_id = a.id
LEFT JOIN tracks t ON a.id = t.albums_id
WHERE t.duration = (SELECT MIN(duration) FROM tracks)
;""").fetchall())

# запрос - название альбомов, содержащих наименьшее количество треков.
print(connection.execute("""SELECT a.title FROM albums a
LEFT JOIN tracks t ON a.id = t.albums_id
GROUP BY a.title 
HAVING COUNT(t.id) = (SELECT COUNT(id) FROM tracks WHERE id = (SELECT MIN(id) FROM tracks) GROUP BY albums_id)
;""").fetchall())

