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
