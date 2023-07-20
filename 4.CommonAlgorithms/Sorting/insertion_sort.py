def get_insertion_index(lst, elem):
    """Получить индекс, куда вставляем"""

    for i in range(len(lst), 0, -1):
        i = i - 1
        if lst[i] <= elem:
            return i + 1

    # В случае, если прошли все элементы, то вставляем число в самое начало, т.к. оно самое маленькое
    return 0


def insertion_sort(lst: list):
    sorted_lst = []

    for elem in lst:
        index = get_insertion_index(lst=sorted_lst, elem=elem)
        sorted_lst.insert(index, elem)

    print(sorted_lst)


def main():
    lst = [10000, -100, 1000000, 1, 2, 3, 6, 4, 5, 15, 3, 2, 100, 75]
    insertion_sort(lst=lst)


if __name__ == '__main__':
    main()
