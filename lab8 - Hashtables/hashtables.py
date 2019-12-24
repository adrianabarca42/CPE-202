"""this file contains code for hash tables
Author: Adrian Abarca
"""
from linked_list import Node

def hash_string(string, size):
    hash = 0
    for c in string:
        hash = (hash * 31 + ord(c)) % size
    return hash

class HashTableSepchain:
    def __init__(self, table_size = 11):
        self.table_size = table_size
        self.num_items = 0
        self.num_collisions = 0
        self.hash_table = [None] * self.table_size

    def load_factor(self):
        return self.num_items / self.table_size

    def put(self, key, data):
        num = hash_string(key, self.table_size)
        load = self.load_factor()
        if load > 1.5:
            self.rehash()
        if self.hash_table[num] is None:
            self.num_items += 1
            self.hash_table[num] = Node(key, data)
        elif self.hash_table[num].key == key:
            self.hash_table[num].data = data 
        elif self.hash_table[num] is not None:
            self.num_collisions += 1
            temp = self.hash_table[num]
            while temp.next is not None:
                temp = temp.next
            temp.next = Node(key, data)
            self.num_items += 1

    def get(self, key):
        num = hash_string(key, self.table_size)
        done = False
        num_start = num
        if self.hash_table[num] is None:
            raise LookupError
        temp = self.hash_table[num]
        while temp is not None:
            if temp.key == key:
                return temp.data
            else:
                temp = temp.next
        raise LookupError

    def contains(self, key):
        num = hash_string(key, self.table_size)
        if self.hash_table[num] is None:
            return False
        if self.hash_table[num].key == key:
            return True
        temp = self.hash_table[num]
        while temp is not None:
            if temp.key == key:
                return True
            temp = temp.next
        return False

    def remove(self, key):
        self.num_items -= 1
        num = hash_string(key, self.table_size)
        if self.contains(key):
            if self.hash_table[num].next is None and self.hash_table[num].key == key:
                self.hash_table[num] = None
            elif self.hash_table[num].key == key:
                self.hash_table[num].next = self.hash_table[num]
            else:
                temp = self.hash_table[num]
                prev = temp
                while temp is not None:
                    if temp.key == key:
                        break
                    prev = temp
                    temp = temp.next
                prev.next = temp.next
                temp = None
        else:
            raise LookupError

    def size(self):
        return self.num_items

    def collisions(self):
        return self.num_collisions

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)

    def __contains__(self, key):
        return self.contains(key)

    def rehash(self):
        old_hash_table = self.hash_table
        self.num_items = 0
        self.num_collisions = 0
        self.table_size = (self.table_size * 2) + 1
        self.hash_table = [None] * self.table_size
        for item in old_hash_table:
            if item is not None:
                if item.next is None:
                    self.put(item.key, item.data)
                else:
                    temp = item
                    while temp is not None:
                        self.put(temp.key, temp.data)
                        temp = temp.next

def rehash_probe(num, step, size):
    return (num + step) % size            
            
class HashTableLinear:
    def __init__(self, table_size=11):
        self.table_size = table_size
        self.hash_table = [None] * self.table_size
        self.num_items = 0
        self.num_collisions = 0
        self.lin = 1

    def rehash(self):
        old_hash_table = self.hash_table
        self.num_items = 0
        self.num_collisions = 0
        self.table_size = (self.table_size * 2) + 1
        self.hash_table = [None] * self.table_size
        for item in old_hash_table:
            if item is not None:
                self.put(item.key, item.data)

    def put(self, key, data):
        num = hash_string(key, self.table_size)
        load = self.load_factor()
        if load > .75:
            self.rehash()
        if self.hash_table[num] is None:
            self.num_items += 1
            self.hash_table[num] = Node(key, data)
        elif self.hash_table[num].key == key:
            self.hash_table[num] = Node(key, data)
        else:
            self.num_items += 1
            self.num_collisions += 1
            num = rehash_probe(num, self.lin, self.table_size)
            while (self.hash_table[num] != None and self.hash_table[num].key != key):
                num = rehash_probe(num, self.lin, self.table_size)
            if self.hash_table[num] is None or self.hash_table[num].key == key:
                self.hash_table[num] = Node(key, data)

    def get(self, key):
        num = hash_string(key, self.table_size)
        done = False
        num_start = num
        if self.hash_table[num] is None:
            raise LookupError
        while not done:
            if self.hash_table[num].key == key:
                return self.hash_table[num].data
            else:
                num = rehash_probe(num, self.lin, self.table_size)
                if num == num_start or self.hash_table[num] is None:
                    raise LookupError

    def contains(self, key):
        num = hash_string(key, self.table_size)
        done = False
        num_start = num
        if self.hash_table[num] is None:
            return False
        while not done:
            if self.hash_table[num].key == key:
                return True
            else:
                num = rehash_probe(num, self.lin, self.table_size)
                if num == num_start or self.hash_table[num] is None:
                    return False

    def remove(self, key):
        self.num_items -= 1
        num = hash_string(key, self.table_size)
        if self.hash_table[num] is None:
            raise LookupError
        while key != self.hash_table[num].key:
            num = rehash_probe(num, self.lin, self.table_size)
        self.hash_table[num] = None
        num = rehash_probe(num, self.lin, self.table_size)
        while self.hash_table[num]:
            redo_key, redo_val = self.hash_table[num].key, self.hash_table[num].data
            self.hash_table[num] = None
            self.put(redo_key, redo_val)
            num = rehash_probe(num, self.lin, self.table_size)

    def size(self):
        return self.num_items

    def load_factor(self):
        return (self.num_items / self.table_size)

    def collisions(self):
        return self.num_collisions

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)

    def __contains__(self,key):
        return self.contains(key)

class HashTableQuadratic:
    def __init__(self, table_size=11):
        self.num_items = 0
        self.table_size = table_size
        self.num_collisions = 0
        self.hash_table = [None] * self.table_size

    def rehash(self):
        old_hash_table = self.hash_table
        self.num_items = 0
        self.num_collisions = 0
        self.table_size = (self.table_size * 2) + 1
        self.hash_table = [None] * self.table_size
        for item in old_hash_table:
            if item is not None:
                self.put(item.key, item.data)

    def put(self, key, data):
        num = hash_string(key, self.table_size)
        load = self.load_factor()
        if load > .75:
            self.rehash()
        if self.hash_table[num] is None:
            self.num_items += 1
            self.hash_table[num] = Node(key, data)
        elif self.hash_table[num].key == key:
            self.hash_table[num] = Node(key, data)
        else:
            self.num_items += 1
            self.num_collisions += 1
            start = 0
            num = (num + (start ** 2)) % self.table_size
            while (self.hash_table[num] != None and self.hash_table[num].key != key):
                start += 1
                num = (num + (start ** 2)) % self.table_size
            if self.hash_table[num] is None or self.hash_table[num].key == key:
                self.hash_table[num] = Node(key, data)

    def get(self, key):
        num = hash_string(key, self.table_size)
        done = False
        num_start = num
        start = 0
        if self.hash_table[num] is None:
            raise LookupError
        while not done:
            if self.hash_table[num].key == key:
                return self.hash_table[num].data
            else:
                start += 1
                num = (num + (start ** 2)) % self.table_size
                if num == num_start or self.hash_table[num] is None:
                    raise LookupError

    def contains(self, key):
        num = hash_string(key, self.table_size)
        done = False
        num_start = num
        start = 0
        if self.hash_table[num] is None:
            return False
        while not done:
            if self.hash_table[num].key == key:
                return True
            else:
                start += 1
                num = (num + (start ** 2)) % self.table_size
                if num == num_start or self.hash_table[num] is None:
                    return False

    def remove(self, key):
        self.num_items -= 1
        num = hash_string(key, self.table_size)
        start = 0
        if self.hash_table[num] is None:
            raise LookupError
        while key != self.hash_table[num].key:
            start += 1
            num = (num + (start ** 2)) % self.table_size
        self.hash_table[num] = None
        start = 1
        num += 1
        while self.hash_table[num]:
            redo_key, redo_val = self.hash_table[num].key, self.hash_table[num].data
            self.hash_table[num] = None
            self.put(redo_key, redo_val)
            start += 1
            num = (num + (start ** 2)) % self.table_size

    def size(self):
        return self.num_items

    def load_factor(self):
        return self.num_items / self.table_size

    def collisions(self):
        return self.num_collisions

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)

    def __contains__(self, key):
        return self.contains(key)

def import_stopwords(filename, hashtable):
    with open(filename, 'r') as infile:
        list1 = []
        for line in infile:
            list1 = line.split()
            print(list1)
            for item in list1:
                if item != '/n':
                    hashtable.put(item, 0)
    return hashtable
