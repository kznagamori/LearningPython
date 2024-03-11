class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)  # リストの末尾に要素を追加

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.stack.pop()  # リストの末尾から要素を取り出し

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

    def display(self):
        print("Stack:", self.stack)

def main():
    s = Stack()

    # スタックにデータを追加
    s.push(1)
    s.push(2)
    s.push(3)
    print("Stack after pushes:")
    s.display()

    # スタックからデータを取得
    try:
        popped = s.pop()
        print(f"Popped: {popped}")
    except Exception as e:
        print(e)

    print("Stack after one pop:")
    s.display()

    # スタックの現在のサイズ
    print("Current stack size:", s.size())

if __name__ == "__main__":
    main()
