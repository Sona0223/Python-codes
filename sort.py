def selection_sort(arr, ascending=True):
    n = len(arr)
    for i in range(n - 1):
        sel = i
        for j in range(i + 1, n):
            if ascending:
                if arr[j] < arr[sel]:
                    sel = j
            else:
                if arr[j] > arr[sel]:
                    sel = j
        if sel != i:
            arr[i], arr[sel] = arr[sel], arr[i]
    return arr

if __name__ == "__main__":
    try:
        nums = list(map(int, input("Enter numbers separated by space: ").strip().split()))
    except ValueError:
        print("Invalid input. Please enter integers separated by spaces.")
    else:
        print("Ascending:", selection_sort(nums.copy(), ascending=True))
        print("Descending:", selection_sort(nums.copy(), ascending=False))
#