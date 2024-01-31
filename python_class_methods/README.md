# クラスを使う

Pythonでクラスを使用する基本的な例を紹介します。この例では、簡単なCarクラスを定義し、そのクラスのインスタンスを作成して、いくつかの属性とメソッドを使ってみます。

## `Car` クラスの定義
`Car` クラスには、車のモデル名と色を表す属性（ `model` と `color` ）があり、`describe_car` メソッドを使用してこれらの情報を出力します。さらに、`drive` メソッドを使って車が「走行中」であることを示します。

```python
class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color

    def describe_car(self):
        print(f"This car is a {self.color} {self.model}.")

    def drive(self):
        print(f"The {self.model} is now driving.")
```

## インスタンスの作成とメソッドの使用
次に、`Car`クラスのインスタンスを作成し、そのメソッドを使用してみます。

```python
def main():
    # Carクラスのインスタンスを作成
    my_car = Car("Toyota Corolla", "blue")
    
    # 車に関する情報を出力
    my_car.describe_car()
    
    # 車を「走行」させる
    my_car.drive()

if __name__ == "__main__":
    main()
```
このプログラムを実行すると、次のような出力が得られます。

```csharp
This car is a blue Toyota Corolla.
The Toyota Corolla is now driving.
```

## 解説
- `__init__` メソッドは、クラスのインスタンスが作成されたときに自動的に呼び出される特別なメソッドです。これをコンストラクタと呼びます。
- `self` パラメータは、メソッド呼び出しに使用されるインスタンス自体を参照します。クラス内のメソッドを定義するときは、常に最初のパラメータとして `self` を使用する必要があります。
- `describe_car` と `drive` メソッドは、クラスのインスタンスで呼び出すことができる動作（メソッド）を定義しています。

この例は、Pythonでのクラスの基本的な使用方法を示しています。クラスは、関連する属性とメソッドを一緒にグループ化する強力な方法を提供し、オブジェクト指向プログラミングの基礎を形成します。
