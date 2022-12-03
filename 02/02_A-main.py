
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
    - iterates through sorted list, appending turns and number of turns to list
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
    """

    '''
    Opponent // Player
        - A // X == rock
        - B // Y == paper
        - C // Z == scissors

    Points (choice):
        - rock     == 1
        - paper    == 2
        - scissors == 3
    
    Points (outcome)
        - win  == 6
        - draw == 3
        - lose == 0
    
    Scoring:
        - rock  < paper < scissors < rock
        - A/X/1 < B/Y/2 < C/Z/3    < A/X/1
    '''
    if opponent == 'A': opponent = 1
    if opponent == 'B': opponent = 2
    if opponent == 'C': opponent = 3

    if player == 'X': player = 1
    if player == 'Y': player = 2
    if player == 'Z': player = 3

    if opponent == player:
        return 3 + player ## draw
    elif player - opponent == 1 or player - opponent == -2:
        return 6 + player ## win
    else:
        return 0 + player ## lose


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
