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
