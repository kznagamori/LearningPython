# スタック構造

Pythonでスタック構造を実装する場合、リストの基本操作を利用して容易に実現できます。スタックは「後入れ先出し」（ `LIFO: Last In, First Out` ）の性質を持ち、要素の追加（プッシュ）と削除（ポップ）がリストの末尾で行われます。以下はそのサンプルプログラムです。

## サンプルプログラム
```python
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

```

この実装では、`push` メソッドでスタック（リスト）の末尾に要素を追加し、`pop` メソッドでスタックの末尾から要素を取り出します。`is_empty` メソッドはスタックが空かどうかを判定し、`size` メソッドはスタックの現在のサイズを返します。`display` メソッドはスタックの現在の内容を表示します。

`main` 関数では、スタックへの要素の追加、一つの要素の取り出し、スタックの内容とサイズの表示を行っています。このサンプルプログラムを実行することで、Pythonでパッケージを使用せずにスタック構造を実装する方法を理解することができます。
