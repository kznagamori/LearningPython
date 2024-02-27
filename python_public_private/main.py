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
