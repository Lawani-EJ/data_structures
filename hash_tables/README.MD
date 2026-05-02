## Hash Table
A hash table is a data structure that stores data and information in key-value pairs using the hash function "hashing concept" to decide where to store each value.

Index:   0      1      2      3      4
       +------+------+------+------+------+
Value: |      | "cat" |      | "dog" |      |
       +------+------+------+------+------+

hash("cat") → 1
hash("dog") → 3

### Hash Functions
A hash fucntion is a function that takes an input 'key' and converts it into a fixed-size number, usually an index which can be used to store or retrieve data from a hash table.

Input Key: "apple"
        ↓
  Hash Function
        ↓
   Index: 3
        ↓
Hash Table[3] = "apple"

### Hashing
Hashing is a technique used to convert data 'key; into a fixed size called a "hash" or "index" which is used to store or retrive data quickly.

Key: "cat"
        ↓
  Hash Function
        ↓
   Index: 2
        ↓
Hash Table[2] = "cat"

### Collision
A collision is when two keys can map to the same index. There are methods in solving collisions

1. Open adressing
2. Seperate addressing

1. Seperate addressing: Seperate addressing stores multiple items at the same index using a list or linked list.


