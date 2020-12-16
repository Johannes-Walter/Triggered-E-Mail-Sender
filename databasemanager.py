import sqlite3
import datetime

# Die Datenbank enthält eine Tabelle [pushings], welche die 3 Datenreihen [id], [press_begin] und [press_duration] enthält
__database_name = "button_press.db"

def add_button_press(press_begin: datetime.datetime, press_duration: datetime.timedelta) -> None:
    # Druckzeitpunkt und -dauer in die Datenbank speichern.
    __write_to_database("INSERT INTO [pushings] ([press_begin], [press_duration]) VALUES (?, ?)", (press_begin.isoformat(), str(press_duration))) # Die Zeit und Dauer des Knopfdrucks in die Datenbank schreiben


def get_presses_since(date: datetime.datetime) -> list:
    # Alles aus der Datenbank seit dem gegebenen Zeitpunkt auslesen
    # Der String zum Vergleich muss in einer Liste sein, da der String selbst sonst als Liste betrachtet wird -> zu viele Elemente.
    data = __read_from_database("SELECT * FROM [pushings] WHERE [press_begin] >= ?", (str(date),))
    
    # Da die ehemaligen Zeiteinheiten jetzt "nur" Strings sind, müssen diese wiederhergestellt werden.
    return __restore_datetime_and_timedelta(data)


def __write_to_database(SQL_String: str, values: list) -> None:
    # Blind einen gegebenen SQL-String ausführen 
    with sqlite3.connect(__database_name) as connection:
        connection.execute(SQL_String, values)

         # Änderungen an der Datenbank speichern
        connection.commit()


def __read_from_database(SQL_String: str, comperator: list) -> list:
    # Blind einen gegebenen SQL-String ausführen und das gelsene zurückgeben.
    with sqlite3.connect(__database_name) as connection:
        return connection.execute(SQL_String, comperator).fetchall()


def __restore_datetime_and_timedelta(data: list) -> list:
    # Aus der gegebenen Liste aus Strings wird eine neue aus Datetimeobjekten gemacht
    new_data = list()
    for row in data:
        list.append(new_data, (
            row[0],
            __string_to_datetime(row[1]),
            __string_to_timedelta(row[2])))
    return new_data


def __string_to_datetime(string: str) -> datetime.datetime:
    #  Da die Zeit in der Datenbank im ISO-Format gespeichert ist, kann sie auch einfach so wieder eingelesen werden.
    return datetime.datetime.fromisoformat(string)


def __string_to_timedelta(string: str) -> datetime.timedelta:
    # Ersetzt in dem gegebenen String den Punkt (trennt die Sekunde von der Mikrosekunde) damit die Trennzeichen identisch sind
    string = string.replace(".", ":")
    
    # Trennt den String jetzt in die verschiedenen Zeiteinheiten
    string = string.split(":")

    # Übersetzt den zerteilten String in eine timedelta
    return datetime.timedelta(hours=float(string[0]), 
                minutes=float(string[1]), 
                seconds=float(string[2]), 
                microseconds=float(string[3]))
