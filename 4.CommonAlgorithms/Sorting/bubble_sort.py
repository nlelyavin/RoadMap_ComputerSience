def change_elem(lst: list, elem: int, i: int) -> None:
    lst[i] = lst[i + 1]
    lst[i + 1] = elem


def bubble_sort(lst: list):
    """Проходимся по всем элементам и тащим самое большое число в конец. Повторяем n раз"""

    for _ in lst:
        for i in range(len(lst) - 1):
            elem = lst[i]

            if elem > lst[i + 1]:
                change_elem(lst, elem, i)


def main():
    lst = [1, 2, 3, 6, 4, 5, 15, 3, 2, 100, 75]
    bubble_sort(lst=lst)


if __name__ == '__main__':
    main()
