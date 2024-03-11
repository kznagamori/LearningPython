# キュー

Pythonの標準ライブラリ `queue` は、スレッドセーフなキュー実装を提供します。このライブラリは、複数のプロデューサーとコンシューマー間でのデータのやり取りに最適です。ここでは、`queue.Queue` クラスを使用した、基本的なキューの使用法を示すサンプルプログラムを提供します。このプログラムでは、アイテムの追加（エンキュー）、アイテムの削除（デキュー）、およびキューの内容の表示を行います。

## サンプルプログラム
```python
import queue

def create_queue():
    """新しいキューの作成"""
    return queue.Queue()

def enqueue(q, item):
    """キューにアイテムを追加"""
    q.put(item)

def dequeue(q):
    """キューからアイテムを削除し、そのアイテムを返す"""
    if not q.empty():
        return q.get()
    else:
        print("Queue is empty.")
        return None

def display_queue(q):
    """キューの内容を表示（デバッグ用）"""
    # Queueの内容を一時的に保持するリスト
    temp_list = []
    while not q.empty():
        temp_item = q.get()
        print(temp_item, end=" ")
        temp_list.append(temp_item)
    
    # キューの内容を再度キューに戻す
    for item in temp_list:
        q.put(item)
    print()  # 改行

def main():
    q = create_queue()
    
    # キューにアイテムを追加
    enqueue(q, "Item 1")
    enqueue(q, "Item 2")
    enqueue(q, "Item 3")
    
    print("Queue after enqueues:")
    display_queue(q)
    
    # キューからアイテムを削除
    print("Dequeued item:", dequeue(q))
    
    print("Queue after one dequeue:")
    display_queue(q)

if __name__ == "__main__":
    main()

```

このサンプルでは、まず `create_queue` 関数を使って新しいキューを作成します。次に、`enqueue` 関数を使用してキューに複数のアイテムを追加します。`dequeue` 関数を呼び出してキューからアイテムを削除し、そのアイテムを表示します。最後に、 `display_queue` 関数を使用してキューの現在の内容を表示します。`display_queue` 関数の実装はデバッグ目的のみに使用されることに注意してください。この関数はキューの内容を変更しませんが、実際のアプリケーションではキューの内容を直接覗き見る方法を提供しないかもしれません。
