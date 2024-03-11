# ジェネリック機能

Pythonでジェネリック（テンプレート）を使用するには、`typing` モジュールの`Generic` クラスと型変数を使用します。これにより、クラスやメソッドに対して型パラメータを定義し、異なる型で再利用可能なコンポーネントを作成できます。以下の例では、ジェネリッククラスとジェネリック関数の使用方法を示します。

## ジェネリッククラスの例
ジェネリッククラスを定義し、異なる型のデータを扱うコンテナを作成します。
```python
from typing import TypeVar, Generic

T = TypeVar('T')

class Box(Generic[T]):
    def __init__(self, item: T):
        self._item = item

    def get_item(self) -> T:
        return self._item

def main():
    int_box = Box[int](123)
    print(int_box.get_item())  # 123

    str_box = Box[str]("hello")
    print(str_box.get_item())  # hello

if __name__ == "__main__":
    main()
```

この例では、`Box` クラスは任意の型Tのアイテムを保持できるジェネリッククラスです。`TypeVar` を使用して型変数Tを定義し、`Generic[T]` を継承してBoxクラスをジェネリックとしてマークします。

## ジェネリック関数の例
特定の型に依存しない関数を定義します。
```python
from typing import TypeVar, List

T = TypeVar('T')

def first_item(items: List[T]) -> T:
    return items[0]

def main():
    numbers = [1, 2, 3]
    print(first_item(numbers))  # 1

    words = ["apple", "banana", "cherry"]
    print(first_item(words))  # apple

if __name__ == "__main__":
    main()
```

この例では、`first_item` 関数は任意の型のリストから最初の要素を返します。型変数 `T` を使用して、関数が異なる型のリストで動作することを示しています。

## 結論
Pythonの `typing` モジュールを使用すると、ジェネリッククラスやジェネリック関数を定義できます。これにより、型安全性を保ちながら、異なる型での再利用性が高いコードを書くことが可能になります。
