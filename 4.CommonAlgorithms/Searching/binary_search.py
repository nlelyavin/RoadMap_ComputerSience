def binary_search(arr: list, target: int) -> int:
    left, right = 0, len(arr) - 1

    while True:
        mid = (left + right) // 2
        print(mid)
        if arr[mid] == target:
            return mid
        elif left == right:
            return False
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1


def main():
    arr = [1, 2, 3, 4, 50, 105, 134, 145, 200, 205]
    target = 205
    print(binary_search(arr=arr, target=target))


main()
