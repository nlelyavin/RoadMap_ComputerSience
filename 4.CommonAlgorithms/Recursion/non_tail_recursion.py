def tail_recursion(n: int):
    result = tail_recursion(n - 1) if n > 0 else 0
    return result + 1


def main():
    result = tail_recursion(10)
    print(result)


if __name__ == '__main__':
    main()
