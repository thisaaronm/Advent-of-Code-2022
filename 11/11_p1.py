
def get_puzzle_input(filename: str) -> list:
    """
    - returns puzzle input as list
    """
    with open(filename, 'r') as f:
        values = f.read().splitlines()

    return values


def p():
    pass


def main():
    filename = '##_example.txt' ## p1: ? || p2: ?
    # filename = '##_input.txt'
    values = get_puzzle_input(filename)


if __name__ == '__main__':
    main()
