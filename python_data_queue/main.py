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
