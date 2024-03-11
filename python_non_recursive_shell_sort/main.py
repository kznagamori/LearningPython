def shell_sort(arr):
    n = len(arr)
    gap = n // 2  # 初期ギャップ値を配列長の半分に設定

    # ギャップの縮小を繰り返し
    while gap > 0:
        # ギャップから配列の末尾まで繰り返し
        for i in range(gap, n):
            temp = arr[i]
            j = i
            # ソートされたサブリスト内で要素を後方にシフト
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            # シフトした位置に現在の要素を挿入
            arr[j] = temp
        gap //= 2  # ギャップを半分に縮小

def main():
    arr = [12, 34, 54, 2, 3]
    print("Original array:", arr)
    shell_sort(arr)
    print("Sorted array:", arr)

if __name__ == "__main__":
    main()
