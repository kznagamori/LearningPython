# リングバッファ構造

リングバッファ（または循環バッファ）は、固定サイズのバッファ（配列など）を用いて、先入れ先出し（ `FIFO` ）のキューを実装するデータ構造です。ここでは、Pythonを用いてリングバッファを実装し、`push` メソッドでデータを追加し、`pop` メソッドでデータを取得し、`get` メソッドでデータを参照するサンプルプログラムを示します。

## サンプルプログラム
```python
class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = [None] * capacity
        self.head = 0
        self.tail = 0
        self.count = 0

    def push(self, item):
        if self.count == self.capacity:
            raise Exception("Buffer is full")
        self.buffer[self.tail] = item
        self.tail = (self.tail + 1) % self.capacity
        self.count += 1

    def pop(self):
        if self.count == 0:
            raise Exception("Buffer is empty")
        item = self.buffer[self.head]
        self.buffer[self.head] = None
        self.head = (self.head + 1) % self.capacity
        self.count -= 1
        return item

    def get(self, index):
        if index >= self.count:
            raise Exception("Index out of bounds")
        return self.buffer[(self.head + index) % self.capacity]

def main():
    capacity = 5
    rb = RingBuffer(capacity)

    # データを追加
    for i in range(capacity):
        rb.push(i + 1)
        print(f"Pushed: {i + 1}")

    # データを参照
    for i in range(rb.count):
        print(f"Item at index {i}: {rb.get(i)}")

    # データを取得
    while rb.count > 0:
        item = rb.pop()
        print(f"Popped: {item}")

if __name__ == "__main__":
    main()

```
このプログラムでは、まず指定した容量でリングバッファを作成します。`push` メソッドでリングバッファにデータを追加し、`get` メソッドで指定したインデックスのデータを参照し、`pop` メソッドでデータを取得しています。バッファが満杯の場合には新しいデータを追加できず、バッファが空の場合にはデータを取得できないように例外を発生させています。これにより、リングバッファの基本的な挙動を実現しています。
