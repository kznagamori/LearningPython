class HashTableNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.table = [None] * capacity

    def hash_function(self, key):
        return hash(key) % self.capacity

    def insert(self, key, value):
        index = self.hash_function(key)
        if self.table[index] is None:
            self.table[index] = HashTableNode(key, value)
        else:
            current = self.table[index]
            while current.next:
                if current.key == key:
                    current.value = value  # Update existing key
                    return
                current = current.next
            if current.key == key:
                current.value = value  # Update existing key
            else:
                current.next = HashTableNode(key, value)  # Handle collision

    def get(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def remove(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        prev = None
        while current:
            if current.key == key:
                if prev:
                    prev.next = current.next
                else:
                    self.table[index] = current.next
                return
            prev = current
            current = current.next

def main():
    ht = HashTable()
    # ハッシュテーブルへのデータの挿入
    ht.insert("key1", "value1")
    ht.insert("key2", "value2")
    ht.insert("key3", "value3")

    # データの取得
    print("key1:", ht.get("key1"))
    print("key2:", ht.get("key2"))
    print("key3:", ht.get("key3"))

    # データの削除
    ht.remove("key2")
    print("After removing key2:")
    print("key2:", ht.get("key2"))

if __name__ == "__main__":
    main()
