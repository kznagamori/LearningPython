# キュー構造

Pythonでキュー構造を実装する場合、リストを基にして自分でエンキュー（追加）とデキュー（取り出し）の操作を定義できます。ただし、リストの先頭からの要素の削除は効率が良くないため、この実装ではリストの末尾に要素を追加し、先頭から取り出す形でキューの動作を模借します。以下はそのサンプルプログラムです。

## サンプルプログラム
```python
class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, item):
        self.queue.append(item)  # リストの末尾に要素を追加
    
    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.queue.pop(0)  # リストの先頭から要素を取り出し
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)
    
    def display(self):
        print("Queue:", self.queue)

def main():
    q = Queue()
    
    # キューにデータを追加
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print("Queue after enqueues:")
    q.display()
    
    # キューからデータを取得
    try:
        dequeued = q.dequeue()
        print(f"Dequeued: {dequeued}")
    except Exception as e:
        print(e)
    
    print("Queue after one dequeue:")
    q.display()

    # キューの現在のサイズ
    print("Current queue size:", q.size())

if __name__ == "__main__":
    main()
```

この実装では、`enqueue` メソッドでキュー（リスト）の末尾に要素を追加し、`dequeue` メソッドでキューの先頭から要素を取り出します。`is_empty` メソッドはキューが空かどうかを判定し、`size` メソッドはキューの現在のサイズを返します。 `display`メソッドはキューの現在の内容を表示します。

`main` 関数では、キューへの要素の追加、一つの要素の取り出し、キューの内容とサイズの表示を行っています。このサンプルプログラムを実行することで、Pythonでパッケージを使用せずにキュー構造を実装する方法を理解することができます。

