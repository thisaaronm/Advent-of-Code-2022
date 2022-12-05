'''
Explanation of why I'm doing it this way:

I know this has to do with LILO queuing, and I think
`collections` has a `queue` module, but:

- 1) I've never used it
- 2) For no good reason whatsoever, I'm trying to do
     AoC without any imports.
'''


'''
        [G]         [D]     [Q]    
[P]     [T]         [L] [M] [Z]    
[Z] [Z] [C]         [Z] [G] [W]    
[M] [B] [F]         [P] [C] [H] [N]
[T] [S] [R]     [H] [W] [R] [L] [W]
[R] [T] [Q] [Z] [R] [S] [Z] [F] [P]
[C] [N] [H] [R] [N] [H] [D] [J] [Q]
[N] [D] [M] [G] [Z] [F] [W] [S] [S]
 1   2   3   4   5   6   7   8   9 
'''

stacks = {
    '1': ['N', 'C', 'R', 'T', 'M', 'Z', 'P'],
    '2': ['D', 'N', 'T', 'S', 'B', 'Z'],
    '3': ['M', 'H', 'Q', 'R', 'F', 'C', 'T', 'G'],
    '4': ['G', 'R', 'Z'],
    '5': ['Z', 'N', 'R', 'H'],
    '6': ['F', 'H', 'S', 'W', 'P', 'Z', 'L', 'D'],
    '7': ['W', 'D', 'Z', 'R', 'C', 'G', 'M'],
    '8': ['S', 'J', 'F', 'L', 'H', 'W', 'Z', 'Q'],
    '9': ['S', 'Q', 'P', 'W', 'N']
}


def get_puzzle_input(filename: str) -> list:
    """
    - returns puzzle input as list
    """
    with open(filename, 'r') as f:
        lines = f.read().splitlines()

    moves = [line for line in lines if 'move' in line]
    return moves


def parse_input(moves: list) -> list:
    """
    - splits incoming `moves` list
    - appends the following list of ints to `parsed_moves`
        - [0] num_of_crates : number of crates to move
        - [1] stack_from    : stack to move crates from
        - [2] stack_to      : stack to move crates to
    - returns `parsed_moves` list
    """
    parsed_moves = []
    for move in moves:
        split_move = move.split(' ')

        num_of_crates = int(split_move[1])
        stack_from    = split_move[3]
        stack_to      = split_move[5]

        parsed_moves.append([num_of_crates, stack_from, stack_to])

    return parsed_moves


def move_crates(stacks: dict, parsed_moves: list) -> str:
    for move in parsed_moves:
        num_of_crates = move[0]
        stack_from    = move[1]
        stack_to      = move[2]

        while num_of_crates > 0:
            stacks[stack_to].append(stacks[stack_from].pop())
            num_of_crates -= 1
    
    return stacks


def get_top_crates(stacks):
    top_crates = []
    for crate in stacks.values():
        top_crates.append(crate.pop())
    
    return ''.join(top_crates)


def main():
    filename = '05_input.txt'
    
    raw_moves    = get_puzzle_input(filename)
    parsed_moves = parse_input(raw_moves)
    moved_crates = move_crates(stacks, parsed_moves)
    top_crates   = get_top_crates(moved_crates)
    
    print(top_crates)


if __name__ == '__main__':
    main()
