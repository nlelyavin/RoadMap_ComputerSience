def merge_sort(lst: list) -> list:
    """Сортировка слиянием.

    1. Рекурсивно делим массив, пока не дойдем до 1 элемента
    2. Потом склеиваем обратно-рекурсивно, сравнивания элементы из каждого массива
    Пример: [1,3], [2,4] ->
        1. Сравниваем 1 и 2 -> [1]
        2. Сравниваем 3 и 2 -> [1, 2]
        3. Сравниваем 3 и 4 -> [1, 2, 3, 4]
    """
    if len(lst) <= 1:
        return lst

    half = len(lst) // 2
    half_1 = lst[:half]
    half_2 = lst[half:]

    sorted_1 = merge_sort(lst=half_1)
    sorted_2 = merge_sort(lst=half_2)

    i = j = 0
    result = []

    while True:
        if sorted_1[i] <= sorted_2[j]:
            result.append(sorted_1[i])
            i += 1
        else:
            result.append(sorted_2[j])
            j += 1

        if i == len(sorted_1) :
            result.extend(sorted_2[j:])
            break

        if j == len(sorted_2):
            result.extend(sorted_1[i:])
            break
    return result


def main():
    lst = [-100, 1, 2, 3, 6, 4, 5, 15, 3, 2, 100, 75, -1000, 50005]
    result = merge_sort(lst=lst)
    print(result)


if __name__ == '__main__':
    main()
