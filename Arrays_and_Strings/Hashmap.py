
class LinkedListNode:
    def __init__(self, k, v, next=None):
        self.key = k
        self.val = v
        self.next = None


class HashMap:
    def __init__(self) -> None:
        self.len = 1000
        self.array = [None] * self.len

    def compute_hash(self, txt: str):
        hash_val = 0
        for i, c in enumerate(txt):
            if i % 4 == 0:
                hash_val += ord(c)
            elif i % 4 == 1:
                hash_val -= ord(c)
            elif i % 4 == 2:
                hash_val *= ord(c)
            else:
                hash_val = hash_val // ord(c)
        return hash_val

    def compute_index(self, hash_val):
        return hash_val % self.len

    def store(self, key, val):
        hash_val = self.compute_hash(key)
        index = self.compute_index(hash_val)
        node = LinkedListNode(key, val)
        cur = self.array[index]

        prev = None
        while cur:
            if cur.key == key:
                cur.val = val
                return
            prev = cur
            cur = cur.next
        if prev:
            prev.key = key
            prev.val = val
        else:
            self.array[index] = node

    def load(self, key):
        hash_val = self.compute_hash(key)
        index = self.compute_index(hash_val)
        cur = self.array[index]
        if not cur:
            return "not found"
        while cur:
            if cur.key == key:
                return cur.val
        return "not_found"


if __name__ == "__main__":
    hashmap = HashMap()

    hashmap.store("harry", 40)
    print(hashmap.load("harry"))
    hashmap.store("tom", 30)
    print(hashmap.load("tom"))
    hashmap.store("harry", 20)
    print(hashmap.load("harry"))
