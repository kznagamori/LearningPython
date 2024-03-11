from collections import deque

class RingBuffer:
    def __init__(self, size):
        self.size = size
        self.buffer = deque(maxlen=size)

    def add(self, item):
        self.buffer.append(item)

    def get_all(self):
        return list(self.buffer)

def create_ring_buffer(size):
    return RingBuffer(size)

def add_item(ring_buffer, item):
    ring_buffer.add(item)

def display_buffer(ring_buffer):
    print("Buffer contents:", ring_buffer.get_all())

def main():
    # リングバッファの作成
    ring_buffer = create_ring_buffer(5)

    # 要素の追加
    for i in range(7):  # 7個の要素を追加して、バッファの動作を見る
        add_item(ring_buffer, i)
        display_buffer(ring_buffer)

if __name__ == "__main__":
    main()
