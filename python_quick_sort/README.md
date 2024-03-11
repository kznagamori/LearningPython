# クイックソート

クイックソートは分割統治アルゴリズムの一種で、平均計算時間が `O(n log n)` と効率的です。基本的なアイデアは、配列から一つの「ピボット」要素を選び、ピボットより小さい要素はピボットの左側に、大きい要素は右側に移動させることで、ピボットを正しい位置に配置します。このプロセスを再帰的に繰り返して配列をソートします。

以下にPythonでのクイックソートの実装例を示します。この例では、最後の要素をピボットとして選択しています。

## サンプルプログラム
```python
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr.pop()
        less_than_pivot = []
        greater_than_pivot = []
        for x in arr:
            if x <= pivot:
                less_than_pivot.append(x)
            else:
                greater_than_pivot.append(x)
        return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)

def main():
    arr = [10, 7, 8, 9, 1, 5]
    sorted_arr = quicksort(arr)
    print("Sorted array is:", sorted_arr)

if __name__ == "__main__":
    main()
```

このプログラムの `quicksort` 関数は、与えられた配列をピボットを使って2つのサブリストに分割し、それぞれを再帰的にソートします。ピボットより小さい要素のリストと、ピボットより大きい要素のリストを作成し、それらのリストを同様にソートした後、結合して全体としてソートされたリストを形成します。

`main` 関数では、ソートしたい配列を定義し、`quicksort` 関数を呼び出してソートを実行し、ソートされた配列を出力しています。このシンプルな実装により、Pythonでクイックソートアルゴリズムを理解しやすくなっています。
