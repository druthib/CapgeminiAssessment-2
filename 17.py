from abc import ABC, abstractmethod
class IDatabaseOperations(ABC):
    @abstractmethod
    def insert(self, data):
        pass
    @abstractmethod
    def update(self, data):
        pass
    @abstractmethod
    def delete(self, data):
        pass

class SQLDatabase(IDatabaseOperations):
    def insert(self, data):
        print(f"SQL-Inserting {data}")
    def update(self, data):
        print(f"SQL-Updating {data}")
    def delete(self, data):
        print(f"SQL-Deleting {data}")

class NoSQLDatabase(IDatabaseOperations):
    def insert(self, data):
        print(f"NoSQL-Adding document {data}")
    def update(self, data):
        print(f"NoSQL-Modifying document {data}")
    def delete(self, data):
        print(f"NoSQL-Removing document {data}")

sql = SQLDatabase()
nosql = NoSQLDatabase()

sql.insert("employee1")
nosql.update("employee1")
sql.delete("employee1")