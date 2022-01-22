class HashTable:
    def __init__(self,size = 7):
        self.data_map = [None] * size

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) *23) % len(self.data_map)
            # 23/any number is prime number that increases the number of randomness.
            return my_hash

    def print_table(Self):
        for i, val in enumerate(Self.data_map):
            print(i, ":", val)

my_hast_table = HashTable()

my_hast_table.print_table()