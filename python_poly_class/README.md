# クラスのインタフェースを使用したポリモーフィズムの実現

Pythonではインタフェースの概念は抽象基底クラス（ `ABC` ）を通して実現されます。抽象クラスは、派生クラスが特定のメソッドを実装することを強制するために使用されます。この機能を使ってポリモーフィズムを実現することができます。ポリモーフィズムとは、異なるクラスのオブジェクトが同じインタフェース（メソッド）を共有しているが、それぞれ異なる動作をすることを指します。

以下のサンプルプログラムでは、`Animal` という抽象基底クラスを定義し、このクラスには `make_sound` という抽象メソッドがあります。次に、`Dog` と `Cat` クラスが `Animal` クラスを継承し、`make_sound` メソッドをオーバーライド（実装）します。main関数では、これらのクラスのインスタンスを作成し、同じインタフェースである `make_sound` メソッドを呼び出します。

## サンプルプログラム
```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

def main():
    animals = [Dog(), Cat()]
    for animal in animals:
        print(animal.make_sound())

if __name__ == "__main__":
    main()

```

このプログラムでは、`Animal` クラスは抽象基底クラスとして定義され、`make_sound` という抽象メソッドを持っています。`Dog` クラスとCatクラスはこの抽象クラスを継承し、`make_sound` メソッドをそれぞれ異なる方法で実装します。`main` 関数では、`Dog` と `Cat` のインスタンスを含むリストをループし、それぞれの `make_sound` メソッドを呼び出しています。これにより、同じインタフェースを通じて異なるクラスのオブジェクトが異なる動作をするポリモーフィズムの例を示しています。
