class AlgoHashTable:

    def __init__(self, size):
        self.size = size
        self.hash_table = self.create_buckets()


    def create_buckets(self):
        return [[] for _ in range(self.size)]

    def set_val(self, key, value):
        hashed_key = hash(key) % self.size
        bucket = self.hash_table[hashed_key]
        found_key = False
        for index, value in enumerate(bucket):
            record_key, record_value = value
            if record_key == key:
                found_key = True
                break
        if found_key:
            bucket[index] = (key, value)
        else: 
            bucket.append((key, value))

    def get_val(self, key):
        hashed_key = hash(key) % self.size
        bucket = self.hash_table[hashed_key]
        found_key = False
        for index, value in enumerate(bucket):
            record_key, record_value = value
            if record_key == key:
                found_key = True
                break
        if found_key:
            return record_value
        else:
            return "No records found with that email address"

    def del_val(self, key):
        hashed_key = hash(key) % self.size
        bucket = self.hash_table[hashed_key]
        found_key = False
        for index, value in enumerate(bucket):
            record_key, record_value = value
            if record_key == key:
                found_key = True
                break
        if found_key:
            hashed_key.pop(index)
            return "Email address removed successfully."
        else:
            return "Email address not found."

    def __str__(self):
        return "".join(str(item) for item in self.hash_table)

hash_table = AlgoHashTable(256)
with open("data.txt") as f:
    for lines in f:
        key, value = lines.split(":")
        hash_table.set_val(key, value)

print(hash_table.get_val("aman@gmail.com"))
