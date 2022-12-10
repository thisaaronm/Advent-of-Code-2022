
def get_puzzle_input(filename: str) -> list:
    """
    - returns puzzle input as list
    """
    with open(filename, 'r') as f:
        values = f.read().splitlines()

    return values


def main():
    filename = '09_example.txt' ## p1: 13 // p2: ?
    # filename = '09_input.txt'
    values = get_puzzle_input(filename)
    print(values)


if __name__ == '__main__':
    main()
