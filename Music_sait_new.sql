CREATE TABLE IF NOT EXISTS genres (
id SERIAL PRIMARY KEY,
name VARCHAR(40) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS performers (
id SERIAL PRIMARY KEY,
name VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS PerformersGenres (
genres_id INTEGER REFERENCES genres(id),
performers_id INTEGER REFERENCES performers(id),
CONSTRAINT pk_pg PRIMARY KEY (genres_id, performers_id)
);

CREATE TABLE IF NOT EXISTS albums (
id SERIAL PRIMARY KEY,
title VARCHAR(40) NOT NULL,
year_of_issue INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS AlbumsPerformers (
albums_id INTEGER REFERENCES albums(id),
performers_id INTEGER REFERENCES performers(id),
CONSTRAINT pk_ap PRIMARY KEY (albums_id, performers_id)
);

CREATE TABLE IF NOT EXISTS tracks (
id SERIAL PRIMARY KEY,
name_track VARCHAR(40) NOT NULL,
duration INTEGER NOT NULL,
albums_id INTEGER REFERENCES  albums(id)
);

CREATE TABLE IF NOT EXISTS collections (
id SERIAL PRIMARY KEY,
title VARCHAR(40) NOT NULL,
year_of_issue INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS TracksCollections (
tracks_id INTEGER REFERENCES tracks(id),
collections_id INTEGER REFERENCES collections(id),
CONSTRAINT pk_tc PRIMARY KEY (tracks_id, collections_id)
)




