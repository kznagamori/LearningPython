# パブリックなクラスのメンバ、メソッドを定義とプライベートなクラスのメンバ、メソッドを定義する

Pythonでは、クラスのメンバ（属性やメソッド）のアクセス制御は、命名規則によって行われます。具体的には、名前の前にアンダースコアを1つ (`_`) または2つ (`__`) を付けることで、メンバの公開範囲を変更します。

1. パブリックメンバ: どこからでもアクセス可能。
2. プライベートメンバ (`__`で始まる): クラス内からのみアクセス可能。外部から直接アクセスすることはできません。

## サンプルプログラム
以下のプログラムでは、`Person` クラスを定義し、パブリックメンバとプライベートメンバを持たせます。

```python
class Person:
    def __init__(self, name, age):
        self.name = name  # パブリック属性
        self.__age = age  # プライベート属性

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.__age}")

    def __display_secret(self):  # プライベートメソッド
        print("This is a private method.")

    def access_private_method(self):
        self.__display_secret()  # クラス内からプライベートメソッドを呼び出す

def main():
    # インスタンスの作成
    person = Person("Alice", 30)

    # パブリック属性へのアクセス
    print(person.name)  # Alice

    # プライベート属性への直接アクセスはエラーを引き起こす
    # print(person.__age)  # AttributeError: 'Person' object has no attribute '__age'

    # パブリックメソッドを通じてプライベート属性にアクセス
    person.display_info()  # Name: Alice, Age: 30

    # プライベートメソッドへの直接アクセスはエラーを引き起こす
    # person.__display_secret()  # AttributeError

    # パブリックメソッドを通じてプライベートメソッドにアクセス
    person.access_private_method()  # This is a private method.

if __name__ == "__main__":
    main()
```

この例では、`name` はパブリック属性で、クラスの外部から直接アクセスできます。一方、`__age` はプライベート属性で、クラスの外部から直接アクセスしようとするとエラーになります。プライベートメソッド`__display_secret` も同様に、クラスの内部からのみアクセス可能です。

プライベートメンバに外部からアクセスする必要がある場合は、パブリックメソッドを介して間接的にアクセスします（この例では `display_info` と `access_private_method` メソッドを使用）。これにより、クラスの実装の詳細を隠蔽し、より安全なコードを書くことができます。

