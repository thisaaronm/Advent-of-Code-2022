
def get_puzzle_input(filename: str) -> list[str]:
    """
    - returns puzzle input as list
    """
    with open(filename, 'r') as f:
        values = f.read().splitlines()

    return values


def create_grid(data: list[str]) -> list[list[int]]:
    # grid = [[int(i) for i in row] for row in data]
    grid = []
    for row in data:
        grid_row = []
        for item in row:
            grid_row.append(int(item))
        grid.append(grid_row)

    return grid


def check_visibility(grid: list[list[int]]) -> int:
    '''
    x => horizontal => columns
    y => vertical   => rows
    '''
    visible = []

    for row in enumerate(grid):
        r_idx, r_data = row ## (row_index / grid[row_index])
        row_check     = []

        for column in enumerate(r_data):
            c_idx, c_data = column ## (column_index / grid[row_index][column_index])
            column_check  = []

            ## left to right
            c_idx_lr   = 0
            left_right = []
            if c_idx == c_idx_lr: left_right.append(True)
            while c_idx_lr < c_idx:
                left_right.append(grid[r_idx][c_idx_lr] < c_data)
                c_idx_lr += 1
            column_check.append(all(left_right))

            ## right to left
            c_idx_rl   = len(r_data) - 1
            right_left = []
            if c_idx == c_idx_rl: right_left.append(True)
            while c_idx_rl > c_idx:
                right_left.append(grid[r_idx][c_idx_rl] < c_data)
                c_idx_rl -= 1
            column_check.append(all(right_left))

            ## top to bottom
            r_idx_tb   = 0
            top_bottom = []
            if r_idx == r_idx_tb: top_bottom.append(True)
            while r_idx_tb < r_idx:
                top_bottom.append(grid[r_idx_tb][c_idx] < c_data)
                r_idx_tb += 1
            column_check.append(all(top_bottom))

            ## bottom to top
            r_idx_bt   = len(grid) - 1
            bottom_top = []
            if r_idx == r_idx_bt: bottom_top.append(True)
            while r_idx_bt > r_idx:
                bottom_top.append(grid[r_idx_bt][c_idx] < c_data)
                r_idx_bt -= 1

            column_check.append(all(bottom_top))
            row_check.append(any(column_check))

        visible.append(row_check)
    
    visibility = 0
    for row in visible:
        for item in row:
            if item:
                visibility += 1

    return visibility        


def main():
    # filename = '08_example.txt'  # p1: 21 || p2: ?
    filename = '08_input.txt'

    puzzle_input = get_puzzle_input(filename)
    grid         = create_grid(puzzle_input)
    visibility   = check_visibility(grid)
    print(visibility)


if __name__ == '__main__':
    main()
