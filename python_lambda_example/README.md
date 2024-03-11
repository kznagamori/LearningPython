# ラムダ式

Pythonのラムダ式は、小さな無名関数を作成するのに便利です。一般的に、ラムダ式は単一の式からなり、`lambda` キーワードを使用して定義されます。以下のプログラムでは、さまざまなシナリオでラムダ式を使用する方法を示します。

## ラムダ式を使用してリストをソート
リストの要素をカスタム基準（例えば、文字列の長さや数値の大小）でソートします。
```python
def sort_examples():
    # 文字列のリストをその長さに基づいてソート
    words = ["Python", "is", "awesome"]
    sorted_words = sorted(words, key=lambda x: len(x))
    print(sorted_words)

    # タプルのリストを第二要素に基づいてソート
    tuples = [(1, 'apple'), (2, 'orange'), (3, 'banana')]
    sorted_tuples = sorted(tuples, key=lambda x: x[1])
    print(sorted_tuples)

```

## ラムダ式を使用してリストの各要素に操作を適用
リストの各要素に対して特定の操作（例えば、各要素の二乗を計算）を適用します。
```python
def apply_to_elements():
    numbers = [1, 2, 3, 4, 5]
    squared_numbers = list(map(lambda x: x**2, numbers))
    print(squared_numbers)
```

## ラムダ式をフィルター条件として使用
特定の条件（例えば、偶数のみを選択）に基づいてリストから要素をフィルタリングします。
```python
def filter_elements():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
    print(even_numbers)
```


## `main` 関数からの呼び出し
これらの関数を `main` 関数から呼び出して、ラムダ式の使用例を実行します。

```python
def main():
    print("Sorting examples:")
    sort_examples()
    
    print("\nApplying lambda to elements:")
    apply_to_elements()
    
    print("\nFiltering elements with lambda:")
    filter_elements()

if __name__ == "__main__":
    main()
```

このプログラムは、ラムダ式を使用してリストをソート、リストの要素に操作を適用、およびリストから要素をフィルタリングする方法を示しています。ラムダ式は、短くて読みやすい一時的な関数を必要とする場合に特に有用です。

