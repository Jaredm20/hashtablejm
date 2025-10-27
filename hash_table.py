class Contact:
    '''
    Contact class to represent a contact with a name and number.
    Attributes:
        name (str): The name of the contact.
        number (str): The phone number of the contact.
    '''
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def __str__(self):
        return f"{self.name}: {self.number}"


class Node:
    '''
    Node class to represent a single entry in the hash table.
    Attributes:
        key (str): The key (name) of the contact.
        value (Contact): The value (Contact object) associated with the key.
        next (Node): Pointer to the next node in case of a collision.
    '''
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    '''
    HashTable class to represent a hash table for storing contacts.
    Attributes:
        size (int): The size of the hash table.
        data (list): The underlying array to store linked lists for collision handling.
    Methods:
        hash_function(key): Converts a string key into an array index.
        insert(key, value): Inserts a new contact into the hash table.
        search(key): Searches for a contact by name.
        print_table(): Prints the structure of the hash table.
    '''
    def __init__(self, size):
        self.size = size
        self.data = [None] * size

    def hash_function(self, key):
        return sum(ord(char) for char in key) % self.size

    def insert(self, key, number):
        index = self.hash_function(key)
        new_contact = Contact(key, number)
        new_node = Node(key, new_contact)
        current = self.data[index]

        if current is None:
            self.data[index] = new_node
            return

        prev = None
        while current is not None:
            if current.key == key:
                current.value.number = number
                return
            prev = current
            current = current.next

        prev.next = new_node

    def search(self, key):
        index = self.hash_function(key)
        current = self.data[index]
        while current is not None:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def print_table(self):
        for i in range(self.size):
            print(f"Index {i}:", end=" ")
            current = self.data[i]
            if current is None:
                print("Empty")
            else:
                while current:
                    print(f"- {current.value}", end=" ")
                    current = current.next
                print()


if __name__ == "__main__":
    table = HashTable(10)
    table.print_table()

    print("\n Add contact names and numbers")
    table.insert("Liam", "314-590-8772")
    table.insert("Sophia", "636-821-0041")
    table.print_table()

    print("\n Search for existing contact ")
    contact = table.search("Liam")
    print("Search result:", contact)

    print("\n collisions and duplicates")
    table.insert("Ethan", "417-233-9044")
    table.insert("Nathan", "618-202-5541")
    table.insert("Lauren", "999-555-9999")
    table.print_table()

    print("\nSearch for non existent contact")
    print(table.search("Ali"))


'''
A hash table is the right structure for fast lookups because it does not have to check through a list, each hash has its own number in an index and can then be pinpointed easily by searching said hash in an index.

In regard to collisions, I decided to use a chaining method as mentioned in the "README". Essentially since each data entry is converted into a specific hash #, and if the data collides it is put into a linked list so that both data entries can exist at once.

A hash table may be used over a list or a tree if the order of the stored data does not matter. Hash tables also allow for slightly quicker execution times and take a lot less effort to structure when entering data once the program is initially created. 
'''
