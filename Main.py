import sqlite3 as lite
import os

# Class of person
class Person:
    """This class represent a person"""
    _name : str
    _last_name : str
    _age : int
    _profession: str

    # Constructor method
    def __init__(self, name: str, last_name: str, age: int, profession: str = "n/a"):
        super().__init__()
        self._name = name
        self._last_name = last_name
        self._age = age
        self._profession = profession

    # Get all data of person
    def get_all_data(self) -> dict:
        return {"name": self._name, "last_name": self._last_name, "age": self._age, "profession": self._profession}
    
    # Convert to string this object
    def __str__(self):
        return "Complete name: {0} {1}\nAge: {2}\nProfession: {3}".format(self._name, self._last_name, self._age, self._profession)


# Path database
path_db = "database.db"

def register_person(*person : Person):
    """Register a person to database"""
    with lite.connect(path_db) as connection:
        # Connection
        query = "CREATE TABLE IF NOT EXISTS person_tb(id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(50) NOT NULL, last_name VARCHAR(50) NOT NULL, age INTEGER NOT NULL, profession VARCHAR(60) NOT NULL);"
        cursor = connection.execute(query)

        for p in person:
             # Insert data to sqlite table
             insert_query = "INSERT INTO person_tb(name, last_name, age, profession) VALUES (\"{0}\", \"{1}\", {2}, \"{3}\");".format(p._name, p._last_name, p._age, p._profession)
             cursor.execute(insert_query)
             print("Successful registration!")

       
def get_all_persons() -> list:
    """Get all persons from database"""
    with lite.connect(path_db) as connection:
        query = "SELECT * FROM  person_tb"
        list = []
        try:
            cursor = connection.execute(query)
            for result in cursor:
                person = Person(result[1], result[2], result[3], result[4]) #[0]Id [1]Name [2]LastName [3]Age [4]Profession 
                list.append(person)

        except Exception:
            print("Ups! Empty database")

        finally:
            return list


# Start method
if __name__ == "__main__":
    while True:
        os.system("clear")
        print("Do you want to register a person or make a query?")
        select = input("1:Register 2:Query 3:Exit\n:")

        #Register a person
        if select == "1":
            #Input data
            name = input("Insert Name: ")
            last_name = input("Insert LastName: ")
            age = input("Insert Age: ")
            profession = input("Insert profession: ")
            # Create person object
            person = Person(name, last_name, age, profession)
            # Register database
            register_person(person)
            print("\n")
            input("Press any key to continue...")
        
        #Query all persons from database
        elif select == "2":
            for person in get_all_persons():
                print(person)
                print(50 * "-")
            print("\n")
            input("Press any key to continue...")
        
        # Program exit
        elif select == "3":
            print("Good bye!")
            exit()
        
        # Incorrect option
        else:
            print("Please select a correct option...")
            print("\n")
            input("Press any key to continue...")
