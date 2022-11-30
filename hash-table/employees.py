# Create a hash table to manage employee records
# Each employee will have a last name, first name, and ID of letters and numbers

def hash_function(id: str):
    # Find a way to convert id to a number 1 to 10
    return 0


class Employee:
    def __init__(self, lname, fname, id):
        self.last_name = lname
        self.first_name = fname
        self.id = id

    def __str__(self):
        return self.id + ": " + self.first_name + " " + self.last_name

    def __hash__(self):
        # We will use a table of 10 slots, so hash function must return a value 1 to 10
        return hash_function(self.id)


class HashTable:
    def __init__(self):
        self.table = [[] for x in range(10)]

    def add(self, e: Employee):
        h = hash(e)
        # Check if employee already in the list
        self.table[h].append(e)

    def find(self, id: str) -> Employee:
        h = hash_function(id)
        # look for the employee in the h list and put it in e
        e = None
        return e


if __name__ == '__main__':
    e = Employee("Does", "John", "abc45")
    print(e)
    print(hash(e))

    ht = HashTable()
    print(ht.table)

    ht.add(e)
    ht.add(e)
    print(ht.table)
