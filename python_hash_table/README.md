# ハッシュテーブル


Pythonでハッシュテーブル構造を実装するには、配列（リスト）と連結リスト（またはその他の衝突解決技術）を組み合わせて使用します。以下のサンプルプログラムでは、単純なハッシュ関数を使用してキーを配列のインデックスにマッピングし、連結リストを使用して衝突を解決する簡単なハッシュテーブルを実装します。

## サンプルプログラム
```python
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
```

この実装では、`HashTableNode` クラスを用いて、キー、値、および次のノードへの参照を保持する連結リストのノードを定義しています。`HashTable` クラスでは、指定された容量の配列（テーブル）を初期化し、キーをハッシュ関数を通じて配列のインデックスに変換しています。挿入、取得、削除の各操作では、このインデックスを使用してデータを操作しています。このサンプルプログラムを実行することで、Pythonでハッシュテーブル構造を実装する方法を理解することができます。
