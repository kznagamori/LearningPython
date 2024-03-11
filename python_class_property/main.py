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
