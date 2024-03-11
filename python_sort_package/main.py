def sort_numeric_list():
    numeric_list = [3, 1, 4, 1, 5, 9, 2, 6]
    sorted_list = sorted(numeric_list)
    print("Sorted numeric list:", sorted_list)

def sort_list_of_tuples():
    list_of_tuples = [(2, 'apple'), (1, 'banana'), (4, 'cherry'), (3, 'date')]
    sorted_list = sorted(list_of_tuples, key=lambda item: item[0])
    print("Sorted list of tuples by the first element:", sorted_list)

def sort_list_descending():
    list_to_sort = [3, 1, 4, 1, 5, 9, 2, 6]
    sorted_list = sorted(list_to_sort, reverse=True)
    print("List sorted in descending order:", sorted_list)

def sort_objects_by_custom_attribute():
    class Fruit:
        def __init__(self, name, count):
            self.name = name
            self.count = count

        def __repr__(self):
            return f"Fruit({self.name}, {self.count})"

    fruits = [Fruit('apple', 2), Fruit('banana', 5), Fruit('cherry', 3)]
    sorted_fruits = sorted(fruits, key=lambda fruit: fruit.count)
    print("Sorted fruits by count:", sorted_fruits)

def main():
    sort_numeric_list()
    sort_list_of_tuples()
    sort_list_descending()
    sort_objects_by_custom_attribute()

if __name__ == "__main__":
    main()
