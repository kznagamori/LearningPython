# リンクドリスト構造

Pythonでリンクドリストを実装し、いくつかの基本的な操作（挿入、検索、削除）を行うサンプルプログラムを以下に示します。この実装では、単方向リンクドリストを使用します。

まずは、ノードクラスとリンクドリストクラスを定義します。ノードクラスはデータと次のノードへの参照（ポインタ）を保持します。リンクドリストクラスは、リストの先頭を指すヘッドと、リストに対する操作を行うメソッドを持ちます。

## サンプルプログラム
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def search(self, key):
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False

    def delete(self, key):
        current = self.head
        prev = None
        while current:
            if current.data == key:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return True
            prev = current
            current = current.next
        return False

    def display(self):
        current = self.head
        while current:
            print(current.data, end=' -> ')
            current = current.next
        print('None')

def main():
    llist = LinkedList()
    # リストにデータを挿入
    llist.insert_at_beginning(10)
    llist.insert_at_beginning(20)
    llist.insert_at_beginning(30)
    # リストの内容を表示
    llist.display()
    # リストからデータを検索
    if llist.search(20):
        print("20 found in list")
    else:
        print("20 not found in list")
    # リストからデータを削除
    if llist.delete(20):
        print("20 deleted from list")
    else:
        print("20 not found in list")
    # 削除後のリストの内容を表示
    llist.display()

if __name__ == "__main__":
    main()
```

このプログラムは、`main` 関数からリンクドリストの各操作を呼び出しています。リストの先頭に要素を追加し、リスト内の要素を検索し、要素を削除し、そしてリストの内容を表示しています。このように、リンクドリストの基本的な操作を行うことができます。

