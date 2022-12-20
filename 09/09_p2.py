def get_puzzle_input(filename: str) -> list:
    """
    - returns puzzle input as list
    """
    with open(filename, 'r') as f:
        values = f.read().splitlines()

    return values


def chk_pos(idx, hdx, rope, cr):
    if   cr == 'c': j = 0
    elif cr == 'r': j = 1

    if rope[idx][j] != rope[hdx][j]:
        rope[hdx][j] = rope[idx][j]


def add_pos(t_pos, pos):
    if t_pos not in pos:
        pos.append([t_pos[0], t_pos[1]])


def get_positions(moves: list):
    ROPE = [[0, 0] for _ in range(10)]
    POS  = [[0, 0]]
    print(ROPE[9])

    for move in moves:
        DIR = move.split()[0]
        NUM = int(move.split()[1])

        while NUM > 0:
            if DIR == 'R':
                ROPE[0][0] += 1
                for i in range(len(ROPE[:-1])):
                    h = i + 1

                    if ROPE[i][0] > ROPE[h][0] + 1:
                        ROPE[h][0] += 1
                        if h == 9:
                            print(ROPE)
                            # print(ROPE[h])
                        chk_pos(idx=i, hdx=h, rope=ROPE, cr='r')

                    if ROPE[i][1] > ROPE[h][1] + 1:
                        ROPE[h][1] += 1
                        if h == 9:
                            print(ROPE)
                            # print(ROPE[h])
                        chk_pos(idx=i, hdx=h, rope=ROPE, cr='c')
                    if i == 8:
                        add_pos(t_pos=ROPE[h], pos=POS)

            if DIR == 'L':
                ROPE[0][0] -= 1
                for i in range(len(ROPE[:-1])):
                    h = i + 1

                    if ROPE[i][0] < ROPE[h][0] - 1:
                        ROPE[h][0] -= 1
                        if h == 9:
                            print(ROPE)
                            # print(ROPE[h])
                        chk_pos(idx=i, hdx=h, rope=ROPE, cr='r')

                    if ROPE[i][1] < ROPE[h][1] - 1:
                        ROPE[h][1] -= 1
                        if h == 9:
                            print(ROPE)
                            # print(ROPE[h])
                        chk_pos(idx=i, hdx=h, rope=ROPE, cr='c')
                    if i == 8:
                        add_pos(t_pos=ROPE[h], pos=POS)

            if DIR == 'D':
                ROPE[0][1] += 1
                for i in range(len(ROPE[:-1])):
                    h = i + 1

                    if ROPE[i][1] > ROPE[h][1] + 1:
                        ROPE[h][1] += 1
                        if h == 9:
                            print(ROPE)
                            # print(ROPE[h])
                        chk_pos(idx=i, hdx=h, rope=ROPE, cr='c')

                    if ROPE[i][0] > ROPE[h][0] + 1:
                        ROPE[h][0] += 1
                        if h == 9:
                            print(ROPE)
                            # print(ROPE[h])
                        chk_pos(idx=i, hdx=h, rope=ROPE, cr='r')
                    if i == 8:
                        add_pos(t_pos=ROPE[h], pos=POS)

            if DIR == 'U':
                ROPE[0][1] -= 1
                for i in range(len(ROPE[:-1])):
                    h = i + 1

                    if ROPE[i][1] < ROPE[h][1] - 1:
                        ROPE[h][1] -= 1
                        if h == 9:
                            print(ROPE)
                            # print(ROPE[h])
                        chk_pos(idx=i, hdx=h, rope=ROPE, cr='c')
                    
                    if ROPE[i][0] < ROPE[h][0] - 1:
                        ROPE[h][0] -= 1
                        if h == 9:
                            print(ROPE)
                            # print(ROPE[h])
                        chk_pos(idx=i, hdx=h, rope=ROPE, cr='r')
                    if i == 8:
                        add_pos(t_pos=ROPE[h], pos=POS)
            NUM -= 1
    return POS


def main():
    # filename = '09_example1.txt' ## 1
    filename = '09_example2.txt' ## 36
    # filename  = '09_input.txt'
    values    = get_puzzle_input(filename)
    positions = get_positions(values)
    # print(len(positions))

    too_high = [2710]
    too_low  = []
    if len(positions) in too_high:
        print(f'\n{len(positions)} is too high')
    elif len(positions) in too_low:
        print(f'\n{len(positions)} is too low')
    else:
        print(f'\n{len(positions)}: Try it out')


if __name__ == '__main__':
    main()