
def get_puzzle_input(filename: str) -> list:
    """
    - takes in puzzle input
    - returns puzzle input as a `list`
    """
    with open(filename, 'r') as f:
        turns = f.read().splitlines()

    return turns


def parse_turns(turns: list) -> list:
    """
    - takes in `list` of turns from the `encrypted study guide`
    - generated sorted list of unique turns
    - iterates through sorted list, appending turs and number of turns to list
    - returns `list` of turns and number of turns
    """
    unique_turns  = sorted(set(turns))
    counted_turns = []
    for turn in unique_turns:
        counted_turns.append([turn, turns.count(turn)])

    return counted_turns


def calculate_score(opponent: str, player: str) -> int:
    """
    - takes in opponent choice and player choice
    - returns the score as an `int`

    Opponent:
        A == rock
        B == paper
        C == scissors
    
    Player:
        X == rock
        Y == paper
        Z == scissors
    
    Points:
        rock     = 1
        paper    = 2
        scissors = 3
    
        win  = 6
        lose = 0
        draw = 3
    
    Scoring:
        rock < paper < scissors < rock
    """
    ## rock
    if opponent == 'A':
        if player == 'X': return 4 ## draw
        if player == 'Y': return 8 ## win
        if player == 'Z': return 3 ## lose
    
    ## paper
    if opponent == 'B':
        if player == 'X': return 1 ## lose
        if player == 'Y': return 5 ## draw
        if player == 'Z': return 9 ## win

    ## scissors
    if opponent == 'C':
        if player == 'X': return 7 ## win
        if player == 'Y': return 2 ## lose
        if player == 'Z': return 6 ## draw


def play_game(counted_turns: list) -> int:
    """
    - takes in `list` of `counted_turns`
    - sets `total_score` to 0
    - iterates through `list` of `counted_turns`
        - sets `opponent` and `player` to their respective choices
        - sets `rounds` to the number of rounds per unique o/p combination
        - calls `calcuate_score()`, passing it `opponent` and `player`
        - increments `total_score` by the `calculated_score` * `rounds`
    - returns `total_score` as an `int`
    """
    total_score = 0

    for counted_turn in counted_turns:
        opponent, player = counted_turn[0].split(' ')
        rounds = counted_turn[1]
        # print(opponent, player, rounds)

        calculated_score = calculate_score(opponent, player)
        total_score      += (calculated_score * rounds)

    return total_score


def main():
    filename = '02_A-input.txt'

    puzzle_input  = get_puzzle_input(filename)
    counted_turns = parse_turns(puzzle_input)
    total_score   = play_game(counted_turns)

    print(total_score)


if __name__ == '__main__':
    main()
