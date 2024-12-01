# Import Statements
import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "movies_user",
    "password": "popcorn",
    "host": "127.0.0.1",
    "database": "movies",
    "raise_on_warnings": True
}


def show_films(cursor, title):
    # method to execute an inner join on all tables
    #   iterate over the dataset and output the results to the termial window

    # inner join query
    cursor.execute(
        "SELECT film_name AS Name, film_director AS Director, genre_name AS Genre, studio_name AS 'Studio Name' "
        "FROM film "
        "INNER JOIN genre ON film.genre_id = genre.genre_id "
        "INNER JOIN studio ON film.studio_id = studio.studio_id ")
    # get the results from the cursor
    films = cursor.fetchall()
    print(f"\n -- {title} --")

    # iterate over the film data set and display the results
    for film in films:
        print("Film Name: {}\nDirector: {}\nGenre Name ID: {}\nStudio Name: {}\n".format(film[0], film[1], film[2], film[3]))


try:
    db = mysql.connector.connect(**config)
    cursor = db.cursor()

    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"],
                                                                                      config["database"]))

    input("\n\n Press any key to continue...")

    #  call the show_films
    show_films(cursor, "DISPLAYING FILMS")

    # Insert a new record into the film
    cursor.execute("INSERT INTO film (film_name, film_releaseDate, film_runtime, film_director, studio_id, genre_id)"
                   " VALUES ('A Cinderella Story', '2004', 81, 'Mark Rosman', 1, 2 ) ")
    db.commit()
    show_films(cursor, "DISPLAYING FILMS AFTER INSERTING A NEW RECORD")


    # Update 'Alien' to being a Horror film
    cursor.execute("UPDATE film "
                   "SET genre_id = 1 "
                   "WHERE film_name = 'Alien' ")
    db.commit()
    show_films(cursor, "DISPLAYING FILMS AFTER UPDATING 'ALIEN' TO HORROR")

    print()
    # Delete the movie 'Gladiator'
    cursor.execute("DELETE FROM film "
                   "WHERE film_name = 'Gladiator'")
    db.commit()
    show_films(cursor, "DISPLAYING FILMS AFTER DELETING 'GLADIATOR'")


except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

finally:
    db.close()
