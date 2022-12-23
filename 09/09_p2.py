'''
This answer was HEAVILY inspired by:
https://github.com/hyper-neutrino/advent-of-code/blob/main/2022/day09p2.py

I had mixed up the tail movement from P1. In P1, for the diagonal tail motion,
I could just move the tail into the row or column of the head.

However, for some reason, it didn't click that the "head" in P2 could also move
in a diagonal motion away from the "tail". I kept getting the wrong answer
because I was still trying to move the tail into the same row/col as the head.

        My wrong movement in P2 based off of my P1 logic
        * * *      * * H      * T H
        * H *  =>  * * *  =>  * * *
        T * *      T * *      * * *

        The correct movement:
        * * *      * * H      * * H
        * H *  =>  * * *  =>  * T *
        T * *      T * *      * * *
'''


def get_puzzle_input(filename: str) -> list:
    """
    - returns puzzle input as list
    """
    with open(filename, 'r') as f:
        values = f.read().splitlines()

    return values


def get_positions(moves: list, knots: int):
    POS   = [[0, 0]]
    ROPE  = [[0, 0] for _ in range(knots)]

    ## For each move (direction and number of moves in that direction)...
    for move in moves:
        DIR, NUM = move.split(' ')
        NUM = int(NUM)

        ## Move the head of the rope the number of moves specified
        for num in range(NUM):
            if DIR == 'R': ROPE[0][0] += 1
            if DIR == 'L': ROPE[0][0] -= 1
            if DIR == 'D': ROPE[0][1] += 1
            if DIR == 'U': ROPE[0][1] -= 1

            ## Move each knot based on the rules in the problem statement
            ## and set H(ead) and T(ail) as their respective indices in ROPE.
            for KNOT in range(knots - 1):
                H = KNOT
                T = KNOT + 1

                ## CHECK COLUMNS
                ## If the "head" (front) knot more than 2 spaces away from
                ## the "tail" (back) knot, move the tail towards the head.
                if abs(ROPE[H][0] - ROPE[T][0]) > 1:

                    ## If the column positions are positive, 
                    ## move the tail in a positive direction.
                    if ROPE[H][0] - ROPE[T][0] > 0:
                        ROPE[T][0] += 1

                    ## If the column positions are negative, 
                    ## move the tail in a negative direction.
                    else:
                        ROPE[T][0] -= 1

                    ## If the knots are in different rows, move the tail
                    ## knot TOWARDS (***NOT INTO***) the head knot row
                    if ROPE[H][1] != ROPE[T][1]:
                        if ROPE[H][1] - ROPE[T][1] > 0:
                            ROPE[T][1] += 1
                        else:
                            ROPE[T][1] -= 1

                ## Check rows
                ## If the "head" (front) knot is 2 spaces away from the "tail"
                ## (back) knot, move the tail towards the head.
                if abs(ROPE[H][1] - ROPE[T][1]) > 1:

                    ## If the row positions are positive, 
                    ## move the tail in a positive direction.
                    if ROPE[H][1] - ROPE[T][1] > 0:
                        ROPE[T][1] += 1
                    ## If the row positions are negative, 
                    ## move the tail in a negative direction.
                    else:
                        ROPE[T][1] -= 1

                    ## If the knots are in different columns, move the tail
                    ## knot TOWARDS (***NOT INTO***) the head knot column
                    if ROPE[H][0] != ROPE[T][0]:
                        if ROPE[H][0] - ROPE[T][0] > 0:
                            ROPE[T][0] += 1
                        else:
                            ROPE[T][0] -= 1

                ## Check last knot (tail) position
                ## If its position is not in POS,
                ## append it to the list.
                if T == knots - 1:
                    last_knot = [ROPE[T][0], ROPE[T][1]]
                    if last_knot not in POS:
                        POS.append(last_knot)
    return POS


def main():
    ## Test Cases
    # filename, knots = ['09_example1.txt', 2]  ## P1
    # filename, knots = ['09_example2.txt', 10] ## P2

    ## Puzzle Input
    # filename, knots = ['09_input.txt', 2]     ## P1
    filename, knots = ['09_input.txt', 10]    ## P2

    puzzle_input = get_puzzle_input(filename)
    positions = get_positions(puzzle_input, knots)
    print(len(positions))


if __name__ == '__main__':
    main()
