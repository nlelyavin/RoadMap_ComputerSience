import random


def partition(arr: list, left: int, right: int) -> (int, int):
    """Переставляем значения в массива от опорного элемента (рандомного)


    :param arr:
    :param left:
    :param right:
    :return:
    """

    pivot = arr[random.randint(left, right)]

    i, j = left, right
    while i <= j:
        while arr[i] < pivot:
            i += 1
        while arr[j] > pivot:
            j -= 1

        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i, j = i + 1, j - 1

    return i, j


def quick_sort(arr: list, left: int, right: int) -> None:
    """Сортировка является рекурсивной. Является доработанной версией, не используя доп. память

    1. Выбираем опорный элемент в partition(в среднем случае без разницы какой)
    2. От опорного элемента перестраиваем массив так, чтобы максимальное кол-во элементов меньших, оказалось слева,
       а больших справа (в partition)
    3. Так делаем пока не перестроим весь массив

    Важный момент, что тут две ссылки, идем пока они не пересекутся

    """

    if left >= right:
        return

    pivot = arr[random.randint(left, right)]
    print(arr, pivot)

    i, j = left, right
    i, j = partition(arr=arr, left=i, right=j)

    quick_sort(arr=arr, left=left, right=j)
    quick_sort(arr=arr, left=i, right=right)


def main():
    arr = [1, 2, -5, 6, 100, -100, 200, -203]
    # arr = [2, 1, -1]
    quick_sort(arr=arr, left=0, right=len(arr) - 1)
    print(arr)


if __name__ == '__main__':
    main()
