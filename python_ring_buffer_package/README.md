# リングバッファ

Pythonでリングバッファを実装する例を提供します。この例では、リングバッファを独自に実装して、その動作を示すいくつかの関数を含むサンプルプログラムを作成します。Pythonには標準ライブラリとしてリングバッファに相当する直接の実装は含まれていませんが、`collections.deque` を使用して効率的なリングバッファの動作を実現することができます。

リングバッファは、固定サイズのバッファで、一度に最大限度まで要素を保持し、新しい要素が追加されると最も古い要素が削除されるデータ構造です。この性質は、例えばリアルタイムデータ処理やキャッシングメカニズムに有効です。

以下に示すのは、`collections.deque` を使用してリングバッファを実装し、その動作をテストするサンプルコードです。各処理（リングバッファの作成、要素の追加、要素の削除、バッファの内容の表示）は、`main` 関数から呼び出されます。

## サンプルプログラム
```python
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

```

このプログラムでは、まずサイズ5のリングバッファを作成し、その後、7つの要素を順番に追加しています。バッファのサイズが5であるため、5つ以上の要素を追加すると、最も古い要素から順に削除されます。この動作は、`display_buffer` 関数を通じて各ステップで確認できます。

