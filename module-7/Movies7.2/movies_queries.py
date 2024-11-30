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

try:
    db = mysql.connector.connect(**config)

    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"],
                                                                                      config["database"]))

    input("\n\n Press any key to continue...")

    # select all fields from the studio table
    cursor = db.cursor()
    cursor.execute("SELECT * FROM studio;")
    studios = cursor.fetchall()
    print("--DISPLAYING Studio RECORDS-- ")
    for studio in studios:
        print(f"Studio ID: {studio[0]}\nStudio Name: {studio[1]}\n")
    print()
    # select all fields from the genre table
    cursor.execute("SELECT * FROM genre;")
    genres = cursor.fetchall()
    print("--DISPLAYING Genre RECORDS-- ")
    for genre in genres:
        print(f"Genre ID: {genre[0]}\nGenre Name: {genre[1]}\n")
    print()

    # select the movie names for those movies that have a run time of less than two hours.
    cursor.execute("SELECT film_name, film_runtime FROM film WHERE film_runtime < 120;")
    films = cursor.fetchall()
    print("--DISPLAYING Short Film Records--")
    for film in films:
        print(f"Film Name: {film[0]}\nRuntime: {film[1]}\n ")

    # get a list of film names, and directors grouped by director
    cursor.execute("SELECT film_director, GROUP_CONCAT(film_name) AS films "
                   "FROM film "
                   "GROUP BY film_director;")
    results = cursor.fetchall()
    print("--DISPLAYING Director RECORDS In Order--")
    for result in results:
        director, films = result
        print(f"File Name: {films}\nDirector: {director}\n")
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

finally:
    db.close()
