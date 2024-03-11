from typing import TypeVar, Generic
from typing import TypeVar, List

T = TypeVar('T')

class Box(Generic[T]):
    def __init__(self, item: T):
        self._item = item

    def get_item(self) -> T:
        return self._item

def first_item(items: List[T]) -> T:
    return items[0]

def main():
    int_box = Box[int](123)
    print(int_box.get_item())  # 123

    str_box = Box[str]("hello")
    print(str_box.get_item())  # hello

    numbers = [1, 2, 3]
    print(first_item(numbers))  # 1

    words = ["apple", "banana", "cherry"]
    print(first_item(words))  # apple

if __name__ == "__main__":
    main()
