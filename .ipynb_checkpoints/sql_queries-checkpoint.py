# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS fct_songplays;"
user_table_drop = "DROP TABLE IF EXISTS users;"
song_table_drop = "DROP TABLE IF EXISTS songs;"
artist_table_drop = "DROP TABLE IF EXISTS artists;"
time_table_drop = "DROP TABLE IF EXISTS time;"

# CREATE TABLES

songplay_table_create = ("create table if not exists fct_songplays\
(\
	songplay_id varchar,\
	start_time numeric,\
	user_id int,\
	level varchar,\
	song_id varchar,\
	artist_id varchar,\
	session_id varchar,\
	location varchar,\
	user_agent varchar);\
")

user_table_create = ("create table if not exists users\
(\
	user_id int\
		constraint users_pk\
			primary key,\
	first_name varchar,\
	last_name varchar,\
	gender varchar,\
	level varchar\
);\
")

song_table_create = ("create table if not exists songs\
(\
	song_id varchar\
		constraint songs_pk\
			primary key,\
	title varchar,\
	artist_id varchar,\
	year int,\
	duration decimal\
);\
")

artist_table_create = ("create table if not exists artists\
(\
	artist_id varchar\
		constraint artists_pk\
			primary key,\
	name varchar,\
	location varchar,\
	latitude decimal,\
	longitude decimal\
);\
")

time_table_create = ("create table time\
(\
	start_time numeric,\
	hour int,\
	day int,\
	week int,\
	month int,\
	year int,\
	weekday int\
);\
")

# INSERT RECORDS

songplay_table_insert = ("INSERT INTO fct_songplays VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)")

user_table_insert = ("INSERT INTO users VALUES(%s, %s, %s, %s, %s) ON CONFLICT DO NOTHING")

song_table_insert = ("INSERT INTO songs VALUES(%s, %s, %s, %s, %s) ON CONFLICT DO NOTHING")

artist_table_insert = ("INSERT INTO artists VALUES(%s, %s, %s, %s, %s) ON CONFLICT DO NOTHING")


time_table_insert = ("INSERT INTO time VALUES(%s, %s, %s, %s, %s, %s, %s)")

# FIND SONGS

song_select = ("SELECT s.song_id as songid, a.artist_id as artistid FROM songs s JOIN artists a ON s.artist_id=a.artist_id WHERE s.title=%s AND a.name=%s AND s.duration=%s")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]