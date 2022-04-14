import sqlite3

con = sqlite3.connect("movies.db")
cur = con.cursor()
cur.execute("CREATE TABLE movie (movie_name VARCHAR(50), actor VARCHAR(20), actress VARCHAR(20), year INT(4), director_name VARCHAR(20));")
while true:
    movie_name=str(input("Enter the name of the movie name: "))
    actor=str(input("Actor: "))
    actress=str(input("Actress: "))
    year=int(input("Year Of Release: "))
    director_name=str(input("Director_name :"))
    cur.execute(f"INSERT INTO movie VALUES ('{movie_name}', '{actor}', '{actress}', '{year}','{director_name}');")
    x=str(input("Enter STOP to STOP: "))
    if x=='stop':
        break
cur.execute("Select * from movie")
for i in cur.fetchall():
    print(i)
