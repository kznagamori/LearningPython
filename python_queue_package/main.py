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
