# LINQ機能

PythonにはC#の `LINQ`（ `Language Integrated Query` ）に直接相当する機能はありませんが、リスト内包表記や `map` 、`filter` 、`sorted` などの組み込み関数を組み合わせることで、類似のデータ処理を実現できます。以下のサンプルプログラムは、Pythonでこれらの機能を使用して、C#の `LINQ` に似た操作を行う例を示しています。

## サンプルデータ
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age})"
```

## フィルタリングとソーティング
```python
def filter_and_sort(people):
    # 年齢が30以上の人を見つけ、名前でソートする
    result = sorted(
        (p for p in people if p.age >= 30),
        key=lambda x: x.name
    )
    return result
```

## マッピング（変換）
```python
def map_people(people):
    # 人々の名前のリストを取得
    names = [p.name for p in people]
    return names
```

## 集約
```python
def average_age(people):
    # 人々の平均年齢を計算
    avg = sum(p.age for p in people) / len(people)
    return avg
```


## main関数
```python
def main():
    people = [
        Person("Alice", 30),
        Person("Bob", 25),
        Person("Carol", 32),
        Person("Dave", 20)
    ]

    print("Filtered and sorted people:")
    filtered_sorted = filter_and_sort(people)
    for person in filtered_sorted:
        print(person)

    print("\nPeople names:")
    names = map_people(people)
    for name in names:
        print(name)

    print("\nAverage age of people:")
    avg_age = average_age(people)
    print(avg_age)

if __name__ == "__main__":
    main()
```

このプログラムは、Pythonで `LINQ` に類似したデータ処理を行う方法を示しています。リスト内包表記、`map`、`filter`、`sorted` 関数を使用して、フィルタリング、ソーティング、マッピング（変換）、集約操作を行います。これらの機能はPythonでのデータ処理において非常に強力で、C#の `LINQ` に匹敵する表現力を提供します。

