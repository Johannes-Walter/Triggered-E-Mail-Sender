import sqlite3
import datetime

database_name = "button_press.db"

def add_button_press(press_begin: datetime.datetime, press_duration: datetime.timedelta) -> None:
    # Druckzeitpunkt und -dauer in die Datenbank speichern.
    write_to_database("INSERT INTO [pushings] ([press_begin], [press_duration]) VALUES (?, ?)", (str(press_begin), str(press_duration))) # Die Zeit und Dauer des Knopfdrucks in die Datenbank schreiben


def get_presses_since(date: datetime.datetime) -> list:
    # Alles aus der Datenbank seit dem gegebenen Zeitpunkt auslesen
    # Der String zum Vergleich muss in einer Liste sein, da der String selbst sonst als Liste betrachtet wird -> zu viele Elemente.
    return read_from_database("SELECT * FROM [pushings] WHERE [press_begin] >= ?", (str(date),))


def write_to_database(SQL_String: str, values: list) -> None:
    # Blind einen gegebenen SQL-String ausführen 
    with sqlite3.connect(database_name) as connection:
        connection.execute(SQL_String, values)

         # Änderungen an der Datenbank speichern
        connection.commit()


def read_from_database(SQL_String: str, comperator: list) -> list:
    # Blind einen gegebenen SQL-String ausführen und das gelsene zurückgeben.
    with sqlite3.connect(database_name) as connection:
        return connection.execute(SQL_String, comperator).fetchall()


