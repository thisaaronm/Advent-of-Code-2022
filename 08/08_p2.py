
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


def get_scenic_score(grid: list[list[int]]) -> int:
    '''
    x => horizontal => columns
    y => vertical   => rows
    '''
    max_scenic_score = 0
    for row in enumerate(grid):
        r_idx, row_data = row ## (row_index / grid[row_index])

        for column in enumerate(row_data):
            cur_tree_idx, cur_tree_val = column ## (column_index / grid[row_index][column_index])

            VIEW_L = 0
            VIEW_R = 0
            VIEW_T = 0
            VIEW_B = 0

            ## Tree to Left
            if cur_tree_idx == 0:
                pass
            else:
                l_tree_idx = cur_tree_idx - 1
                check = True
                while check:
                    l_tree_val = grid[r_idx][l_tree_idx]
                    if l_tree_val < cur_tree_val:
                        VIEW_L += 1
                    else:
                        VIEW_L += 1
                        check = False

                    if l_tree_idx <= 0:
                        check = False
                    l_tree_idx -= 1
            
            # ## Tree to Right
            if cur_tree_idx == len(row_data) - 1:
                pass
            else:
                r_tree_idx = cur_tree_idx + 1
                check = True
                while check:
                    r_tree_val = grid[r_idx][r_tree_idx]
                    if r_tree_val < cur_tree_val:
                        VIEW_R += 1
                    else:
                        VIEW_R += 1
                        check = False
                    
                    if r_tree_idx >= len(row_data) - 1:
                        check = False
                    r_tree_idx += 1

            # ## Tree to Bottom
            if r_idx == len(row_data) - 1:
                pass
            else:
                b_tree_idx = r_idx + 1
                check = True
                while check:
                    b_tree_val = grid[b_tree_idx][cur_tree_idx]
                    if b_tree_val < cur_tree_val:
                        VIEW_B += 1
                    else:
                        VIEW_B += 1
                        check = False
                    if b_tree_idx >= len(row_data) - 1:
                        check = False
                    b_tree_idx += 1

            # ## Tree to Top
            if r_idx == 0:
                pass
            else:
                t_tree_idx = r_idx - 1
                check = True
                while check:
                    t_tree_val = grid[t_tree_idx][cur_tree_idx]
                    if t_tree_val < cur_tree_val:
                        VIEW_T += 1
                    else:
                        VIEW_T += 1
                        check = False
                    
                    if t_tree_idx <= 0:
                        check = False
                    t_tree_idx -= 1

            cur_scenic_score = VIEW_L * VIEW_R * VIEW_B * VIEW_T
            if cur_scenic_score > max_scenic_score:
                max_scenic_score = cur_scenic_score
        
    return max_scenic_score        


def main():
    # filename = '08_example.txt'  # p1: 21 || p2: 8
    filename = '08_input.txt'

    puzzle_input = get_puzzle_input(filename)
    grid         = create_grid(puzzle_input)
    scenic_score = get_scenic_score(grid)
    print(scenic_score)


if __name__ == '__main__':
    main()
