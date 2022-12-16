
def get_puzzle_input(filename: str) -> list:
    """
    - returns puzzle input as list
    """
    with open(filename, 'r') as f:
        values = f.read().splitlines()

    return values


def get_positions(moves: list):
    ## HEAD = [HC, HR]
    ## TAIL = [TC, TR]

    HC, HR = 0, 0
    TC, TR = 0, 0
    START  = [0, 0]


    POS = []
    POS.append(START)

    for move in moves:
        DIR = move.split()[0]
        NUM = int(move.split()[1])

        while NUM > 0:
            if DIR == 'R':
                HC += 1
                if HC > TC + 1:
                    TC += 1
                    if HR != TR:
                        TR = HR
                    if [TC, TR] not in POS:
                            POS.append([TC, TR])

            if DIR == 'L':
                HC -= 1
                if HC < TC - 1:
                    TC -= 1
                    if HR != TR:
                        TR = HR
                    if [TC, TR] not in POS:
                            POS.append([TC, TR])

            if DIR == 'D':
                HR += 1
                if HR > TR + 1:
                    TR += 1
                    if HC != TC:
                        TC = HC
                    if [TC, TR] not in POS:
                            POS.append([TC, TR])

            if DIR == 'U':
                HR -= 1
                if HR < TR - 1:
                    TR -= 1
                    if HC != TC:
                        TC = HC
                    if [TC, TR] not in POS:
                            POS.append([TC, TR])

            NUM -= 1

    return POS


def main():
    # filename = '09_example1.txt' ## 13
    filename  = '09_input.txt'
    values    = get_puzzle_input(filename)
    positions = get_positions(values)
    print(len(positions))


if __name__ == '__main__':
    main()
