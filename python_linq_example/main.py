class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age})"

def filter_and_sort(people):
    # 年齢が30以上の人を見つけ、名前でソートする
    result = sorted(
        (p for p in people if p.age >= 30),
        key=lambda x: x.name
    )
    return result

def map_people(people):
    # 人々の名前のリストを取得
    names = [p.name for p in people]
    return names

def average_age(people):
    # 人々の平均年齢を計算
    avg = sum(p.age for p in people) / len(people)
    return avg

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
