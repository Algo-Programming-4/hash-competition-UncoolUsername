from bucket import Bucket

# I name this program the Maurice Flitcroft hash, because there is no way
# this would have a low score. 
class hashTable:
    def __init__(self, initial_capacity = 100):
        self.hash = [Bucket() for _ in range(initial_capacity)]
        self.size = initial_capacity

        self.LOAD_FACTOR = 0
        self.FULL_BUCKETS = 0

        self.collisions = 0


    def hash_key(self, key):
        return int(str(hash(key))[0 : 2])
    

    def insert(self, key, value):
        index = self.hash_key(key)

        if not self.hash[index].size == 0:
            self.collisions += 1
        else:
            self.FULL_BUCKETS += 1

        self.hash[index].push(value)

        self.size += 1
        self.LOAD_FACTOR = self.size // self.size


    def remove(self, key, value):
        index = self.hash_key(key)

        if not self.hash[index].size == 0:
            self.collisions += 1
        else:
            self.FULL_BUCKETS += 1

        self.hash[index].remove(value)

        self.size -= 1
        self.LOAD_FACTOR = self.size // self.size


    def __str__(self):
        hashSTR = ""
        for list_item in self.hash:
            if type(list_item) == Bucket:
                hashSTR +=  str(list_item)

        if self.LOAD_FACTOR > 60:
            return f"!/{hashSTR}/!"
        else:
            return f"/{hashSTR}/"


    def words_in(self, words):
        for word in words:
            self.insert(word, word)

        return self.FULL_BUCKETS, self.collisions


    def lookup_word_count(self, word):
        index = self.hash_key(word)
        word_count = 0
        lookup_steps = 0
        
        bucket = self.hash[index]
        print(bucket)

        for item in bucket.array:
            lookup_steps += 1
            if item == word:
                word_count += 1

        return word_count, lookup_steps
    