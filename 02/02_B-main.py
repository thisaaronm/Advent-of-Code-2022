
def get_puzzle_input(filename: str) -> list:
    """
    - takes in puzzle input
    - returns puzzle input as a `list`
    """
    with open(filename, 'r') as f:
        rounds = f.read().splitlines()

    return rounds


def parse_rounds(rounds: list) -> list:
    """
    - takes in `list` of rounds from the `encrypted study guide`
    - generated sorted list of unique rounds
    - iterates through sorted list, appending rounds and number of rounds to list
    - returns `list` of rounds and number of rounds
    """
    unique_rounds  = sorted(set(rounds))
    counted_rounds = []
    for round in unique_rounds:
        counted_rounds.append([round, rounds.count(round)])

    return counted_rounds


def calculate_score(opponent: str, player: str) -> int:
    """
    - takes in opponent's shape and player's outcome
    - returns the score as an `int`
    """

    '''
    Opponent's Shape:    ||    Player's Outcome:
        A == rock        ||        X == lose
        B == paper       ||        Y == draw
        C == scissors    ||        Z == win

    Points
        Shape            ||    Outcome
        rock     1       ||    win   6
        paper    2       ||    draw  3
        scissors 3       ||    lose  0
    
    Scoring:
        - rock (1) < paper (2) < scissors (3) < rock (1)
    '''
    ## rock
    if opponent == 'A':
        if player == 'X': return 0 + 3 ## lose + scissors
        if player == 'Y': return 3 + 1 ## draw + rock
        if player == 'Z': return 6 + 2 ## win  + paper
    
    ## paper
    if opponent == 'B':
        if player == 'X': return 0 + 1 ## lose + rock
        if player == 'Y': return 3 + 2 ## draw + paper
        if player == 'Z': return 6 + 3 ## win  + scissors

    ## scissors
    if opponent == 'C':
        if player == 'X': return 0 + 2 ## lose + paper
        if player == 'Y': return 3 + 3 ## draw + scissors
        if player == 'Z': return 6 + 1 ## win  + rock


def play_game(counted_rounds: list) -> int:
    """
    - takes in `list` of `counted_rounds`
    - sets `total_score` to 0
    - iterates through `list` of `counted_rounds`
        - sets `opponent` to their shape
        - sets `player` to their outcome
        - sets `rounds` to the number of rounds per unique o/p combination
        - calls `calcuate_score()`, passing it `opponent` and `player`
        - increments `total_score` by the `calculated_score` * `rounds`
    - returns `total_score` as an `int`
    """
    total_score = 0

    for counted_round in counted_rounds:
        opponent, player = counted_round[0].split(' ')
        rounds = counted_round[1]

        calculated_score = calculate_score(opponent, player)
        total_score      += (calculated_score * rounds)

    return total_score


def main():
    filename = '02_A-input.txt'

    puzzle_input   = get_puzzle_input(filename)
    counted_rounds = parse_rounds(puzzle_input)
    total_score    = play_game(counted_rounds)

    print(total_score)


if __name__ == '__main__':
    main()
