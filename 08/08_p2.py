
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
    max_scenic_score = 0
    for row in enumerate(grid):
        r_idx, row_data = row ## (row_index / grid[row_index])

        for column in enumerate(row_data):
            tree_idx, curr_tree = column ## (column_index / grid[row_index][column_index])

            VIEW_LEFT   = 0
            VIEW_RIGHT  = 0
            VIEW_TOP    = 0
            VIEW_BOTTOM = 0

            ## Tree to Left
            if tree_idx == 0:
                pass
            else:
                left_tree_idx = tree_idx - 1
                check = True
                while check:
                    print(f'[{r_idx}, {tree_idx}], [{curr_tree}], {left_tree_idx}, {grid[r_idx][left_tree_idx]}')
                    tree_to_the_left = grid[r_idx][left_tree_idx]
                    if tree_to_the_left < curr_tree:
                        VIEW_LEFT += 1
                    else:
                        VIEW_LEFT += 1
                        check = False

                    if left_tree_idx <= 0:
                        check = False
                    left_tree_idx -= 1
            print(f'\nVIEW_LEFT: {VIEW_LEFT}')
            
            # ## Tree to Right
            if tree_idx == len(row_data) - 1:
                pass
            else:
                right_tree_idx = tree_idx + 1
                check = True
                while check:
                    print(f'[{r_idx}, {tree_idx}], [{curr_tree}], {right_tree_idx}, {grid[r_idx][right_tree_idx]}')
                    tree_to_the_right = grid[r_idx][right_tree_idx]
                    if tree_to_the_right < curr_tree:
                        VIEW_RIGHT += 1
                    else:
                        VIEW_RIGHT += 1
                        check = False
                    
                    if right_tree_idx >= len(row_data) - 1:
                        check = False
                    right_tree_idx += 1
            print(f'VIEW_RIGHT: {VIEW_RIGHT}')

            # ## Tree to Bottom
            if r_idx == len(row_data) - 1:
                pass
            else:
                bottom_tree_idx = r_idx + 1
                check = True
                while check:
                    print(f'[{r_idx}, {tree_idx}], [{curr_tree}], {bottom_tree_idx}, {grid[r_idx][bottom_tree_idx]}')
                    tree_to_the_bottom = grid[bottom_tree_idx][tree_idx]
                    if tree_to_the_bottom < curr_tree:
                        VIEW_BOTTOM += 1
                    else:
                        VIEW_BOTTOM += 1
                        check = False
                    if bottom_tree_idx >= len(row_data) - 1:
                        check = False
                    bottom_tree_idx += 1
            print(f'VIEW_BOTTOM: {VIEW_BOTTOM}')

            # ## Tree to Top
            if r_idx == 0:
                pass
            else:
                top_tree_idx = r_idx - 1
                check = True
                while check:
                    print(f'[{r_idx}, {tree_idx}], [{curr_tree}], {top_tree_idx}, {grid[r_idx][top_tree_idx]}')
                    tree_to_the_top = grid[top_tree_idx][tree_idx]
                    if tree_to_the_top < curr_tree:
                        VIEW_TOP += 1
                    else:
                        VIEW_TOP += 1
                        check = False
                    
                    if top_tree_idx <= 0:
                        check = False
                    top_tree_idx -= 1
            print(f'VIEW_TOP: {VIEW_TOP}')

            curr_scenic_score = VIEW_LEFT * VIEW_RIGHT * VIEW_BOTTOM * VIEW_TOP
            
            print(f'({r_idx}, {tree_idx}, [{curr_tree}]) - curr_scenic_score: {curr_scenic_score}')
            # print('max_scenic_score: ', max_scenic_score)
            
            if curr_scenic_score > max_scenic_score:
                max_scenic_score = curr_scenic_score
        
    return max_scenic_score        


def main():
    # filename = '08_example.txt'  # p1: 21 || p2: ?
    filename = '08_input.txt'

    puzzle_input = get_puzzle_input(filename)
    grid         = create_grid(puzzle_input)
    visibility   = check_visibility(grid)
    print(visibility)


if __name__ == '__main__':
    main()
