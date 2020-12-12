import sqlite3
import datetime

database_name = "button_press.db"

def add_button_press(press_begin: datetime.datetime, press_duration: datetime.timedelta):
    write_to_database("INSERT INTO [pushings] ([press_begin], [press_duration]) VALUES (?, ?)", (press_begin, press_duration)) # Die Zeit und Dauer des Knopfdrucks in die Datenbank schreiben


def get_presses_since(date: datetime.datetime) -> dict:
    return read_from_database("SELECT * FROM [pushings] WHERE [press_begin] >= ?", date)


def write_to_database(SQL_String: str, values: list):
    with sqlite3.connect(database_name) as connection:
        connection.execute(SQL_String, values)

         # Änderungen an der Datenbank speichern
        connection.commit()


def read_from_database(SQL_String: str, comperator: list):
    with sqlite3.connect(database_name) as connection:
        return connection.execute(SQL_String, comperator).fetchall()


