
def get_puzzle_input(filename: str) -> list:
    """
    - returns puzzle input as list
    """
    with open(filename, 'r') as f:
        characters = f.read()

    return characters


def parse_buffer(datastream: str) -> int:
    marker_start = 0
    marker_end   = 4

    while marker_end < len(datastream):
        nibble = datastream[marker_start:marker_end]

        if len(set(nibble)) == 4: 
            return marker_end
        else:
            marker_start += 1
            marker_end   += 1

    return 1


def main():
    filename = '06_input.txt'

    characters      = get_puzzle_input(filename)
    start_of_packet = parse_buffer(characters)
    print(start_of_packet)

if __name__ == '__main__':
    main()
