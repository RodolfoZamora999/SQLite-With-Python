import sqlite3 as lite

# Class of person
class Person:
    """This class represent a person"""
    __name : str
    __last_name : str
    __age : int
    __profession: str

    # Constructor method
    def __init__(self, name: str, last_name: str, age: int, profession: str = "n/a"):
        super().__init__()
        self.__name = name
        self.__last_name = last_name
        self.__age = age
        self.__profession = profession

    # Get all data of person
    def get_all_data(self) -> dict:
        return {"name": self.__name, "last_name": self.__last_name, "age": self.__age, "profession": self.__profession}
    
    # Convert to string this object
    def __str__(self):
        return "Complete name: {0} {1} Age: {2} Profession: {3}".format(self.__name, self.__last_name, self.__age, self.__profession)


# Path database
path_db = "database.db"
with lite.connect(path_db) as connection:
    # Connection
    cursor = connection.execute("CREATE TABLE IF NOT EXISTS person_tb(id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(50) NOT NULL, last_name VARCHAR(50) NOT NULL, age INTEGER NOT NULL, profession VARCHAR(60) NOT NULL);")

    # Data input
    name = input("Insert Name: ")
    last_name = input("Insert LastName: ")
    age = int(input("Insert Age: "))
    profession = input("Insert profession: ")

    # Insert data to sqlite table
    insert_query = "INSERT INTO person_tb(name, last_name, age, profession) VALUES (\"{0}\", \"{1}\", {2}, \"{3}\");".format(name, last_name, str(age), profession)
    cursor.execute(insert_query)

