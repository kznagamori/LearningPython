# クラスのプロパティを定義、使用

Pythonでは、プロパティを使用して、クラスの属性にアクセスする際のゲッター（取得メソッド）、セッター（設定メソッド）、デリーター（削除メソッド）を定義できます。これにより、C# のようにクラスのプロパティをより制御下で扱うことができます。

## サンプルプログラム
以下の例では、`Person` クラスに `name` と `age` プロパティを定義し、外部からこれらのプロパティへのアクセスを制御する方法を示します。

```python
class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        """ゲッターメソッド: nameプロパティの値を取得"""
        return self._name

    @name.setter
    def name(self, value):
        """セッターメソッド: nameプロパティの値を設定"""
        self._name = value

    @property
    def age(self):
        """ゲッターメソッド: ageプロパティの値を取得"""
        return self._age

    @age.setter
    def age(self, value):
        """セッターメソッド: ageプロパティの値を検証し、設定"""
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value

def main():
    person = Person("Alice", 30)

    # プロパティを通じて値を取得
    print(person.name)  # Alice
    print(person.age)   # 30

    # プロパティを通じて値を設定
    person.name = "Bob"
    person.age = 25

    # 新しい値を表示
    print(person.name)  # Bob
    print(person.age)   # 25

    # 不正な年齢を設定しようとすると例外が発生
    try:
        person.age = -1
    except ValueError as e:
        print(e)  # Age cannot be negative

if __name__ == "__main__":
    main()
```

このプログラムでは、`Person` クラスに `name` と `age` の両方のプロパティが定義されています。各プロパティには、それぞれのゲッターとセッターが定義されており、`age` プロパティのセッターでは値が負の数でないか検証しています。これにより、属性の値がクラスの外部から直接変更されることを防ぎつつ、値の検証と設定を行うことができます。
