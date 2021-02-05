class HashTable(object):

    def __init__(self, starting_capacity=64):
        self.table = []
        for i in range(starting_capacity):
            self.table.append([])

    def get_hash(self, key):
        hash_num = 0
        for letter in key:
            hash_num += ord(str(letter))
        return hash_num % len(self.table)

    def insert(self, item):
        find_hash = self.get_hash(item[1])
        bucket_list = self.table[find_hash]
        if len(bucket_list) == 0:
            bucket_list.append(item)
            return
        elif len(bucket_list) >= 1:
            if bucket_list[0][1] == item[1]:
                bucket_list.append(item)
            elif bucket_list[0][1] != item[1]:
                i = 1
                while i < len(self.table):
                    bucket_list_index = self.table[find_hash + i % 64]
                    if len(bucket_list_index) == 0:
                        bucket_list_index.append(item)
                        return
                    elif len(bucket_list_index) >= 1:
                        if bucket_list_index[0][1] == item[1]:
                            bucket_list_index.append(item)
                            return
                    else:
                        i += 2

    def search(self, key):
        get_hash = self.get_hash(key)
        bucket = self.table[get_hash]

        if len(bucket) == 0:
            return
        if bucket[0][1] == key:
            return bucket
        else:
            i = 0
            while i < len(self.table):
                next_bucket = self.table[get_hash + i % 64]
                if len(next_bucket) == 0:
                    return bucket
                if next_bucket[0][1] == key:
                    return next_bucket
                else:
                    i += 1

    def remove(self, key):
        bucket = self.get_hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        if key in bucket_list:
            bucket_list.remove(key)

    def print(self, title):
        print('---' + title + '---')
        for item in self.table:
            print(item)

    def print_item(self, key):
        for item in self.table:
            if len(item) >= 1:
                if key == str(item[0][1]):
                    print("\n")
                    print("Item index is " + str(self.table.index(item)))
                    print("Package Id: " + str(item[0][0]))
                    print("Package Address: " + str(item[0][1]))
                    print("The Deadline for Delivery is: " + str(item[0][5]))
                    print("Details for this package are: " + str(item[0][7]))
                    return
