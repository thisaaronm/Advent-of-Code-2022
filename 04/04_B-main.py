
def get_puzzle_input(filename: str) -> list:
    """
    return puzzle input as list
    """
    with open(filename, 'r') as f:
        content = f.read().splitlines()

    return content


def parse_puzzle_input(puzzle_input: list) -> list:
    """
    
    """
    puzzle_input = [section.split(',') for section in puzzle_input]
    split_pairs  = [[pair[0].split('-'), pair[1].split('-')] for pair in puzzle_input]
    parsed_input = []
    for split_pair in split_pairs:
        pair1 = [int(split_pair[0][0]), int(split_pair[0][1])]
        pair2 = [int(split_pair[1][0]), int(split_pair[1][1])]
        parsed_input.append([pair1, pair2])

    return parsed_input


def get_overlap(data: list):
    overlap = 0
    for pairs in data:
        print(pairs)
        [p1, p2] = pairs

        for i in range(p1[0], p1[1] + 1):
            if i in range(p2[0], p2[1] + 1):
                overlap += 1
                break
    
    return overlap


def main():
    filename = '04_input.txt'
    
    puzzle_input   = get_puzzle_input(filename)
    parsed_input   = parse_puzzle_input(puzzle_input)
    total_overlaps = get_overlap(parsed_input)
    print(total_overlaps)


if __name__ == '__main__':
    main()
