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
