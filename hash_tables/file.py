class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    # Simple hash function
    def hash_function(self, key):
        return len(key) % self.size

    # Insert key-value
    def insert(self, key, value):
        index = self.hash_function(key)
        self.table[index] = value

    # Get value
    def get(self, key):
        index = self.hash_function(key)
        return self.table[index]


ht = HashTable(5)

ht.insert("cat", 10)
ht.insert("dog", 20)

print(ht.get("cat"))  # 10