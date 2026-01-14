class HashTable:
    
    def __init__(self):
        self.collection = {}

    def hash(self, string):
        # if String is empty do nothing
        if not string:
            return
        # Initialice sum variable
        sum_unicode=0
        # Sum all the ASCII values of each letter
        for char in string:
            sum_unicode += ord(char)
        # Return the sum
        return sum_unicode

    def add(self, key, value):
        # If the hashed key IS NOT in the collection
        if not self.hash(key) in self.collection:
            # Add the new key value pair to the hashed key in the coolection
            self.collection[self.hash(key)] = {key:value} 
        # If the hashed key IS in the collection
        else:
            # Add (nested) the new key value pair to the existed hashed key
            self.collection[self.hash(key)][key] = value

    def remove(self, key):
        # Cheking if the key exist in the collection
        if self.hash(key) in self.collection:
            # Cheking if there is more elements nested in the same key
            if key in self.collection[self.hash(key)] and len(self.collection[self.hash(key)])>1:
                # Deleting the nested Element
                del self.collection[self.hash(key)] [key]
            else:
                # Deleteing the key
                del self.collection[self.hash(key)]

    def lookup(self, key):
        # Cheking if the key exist in the collection
        if self.hash(key) in self.collection:
            # If key in a hashed key element of the collection 
            if key in self.collection[self.hash(key)]:
                # Return the key value in the hashed element key of the collection.
                return self.collection[self.hash(key)][key]
            else:
                return None
        else:
            return None

if __name__ == '__main__':
    lista = HashTable() 
    lista.add('dear','friend')
    lista.add('read','friend')
    lista.add('hola','friend')
    print(lista.collection)
    lista.remove('read')
    print(lista.collection)
    print(lista.lookup('read'))