def tail_recursion(n: int):
    return tail_recursion(n - 1) if n > 0 else 0


def main():
    tail_recursion(10)


if __name__ == '__main__':
    main()
