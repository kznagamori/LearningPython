def sort_examples():
    # 文字列のリストをその長さに基づいてソート
    words = ["Python", "is", "awesome"]
    sorted_words = sorted(words, key=lambda x: len(x))
    print(sorted_words)

    # タプルのリストを第二要素に基づいてソート
    tuples = [(1, 'apple'), (2, 'orange'), (3, 'banana')]
    sorted_tuples = sorted(tuples, key=lambda x: x[1])
    print(sorted_tuples)

def apply_to_elements():
    numbers = [1, 2, 3, 4, 5]
    squared_numbers = list(map(lambda x: x**2, numbers))
    print(squared_numbers)

def filter_elements():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
    print(even_numbers)

def main():
    print("Sorting examples:")
    sort_examples()

    print("\nApplying lambda to elements:")
    apply_to_elements()

    print("\nFiltering elements with lambda:")
    filter_elements()

if __name__ == "__main__":
    main()
