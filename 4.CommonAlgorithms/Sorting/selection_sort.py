def selection_sort(lst: list) -> None:
    """Сортировка выбором"""

    for i in range(len(lst)):
        local_min = lst[i]

        for j in range(i, len(lst)):
            if lst[j] < local_min:
                local_min = lst[j]
                lst[j] = lst[i]
                lst[i] = local_min


def main():
    lst = [10000, -100, 1000000, 1, 2, 3, 6, 4, 5, 15, 3, 2, 100, 75]
    selection_sort(lst=lst)
    print(lst)


if __name__ == '__main__':
    main()
