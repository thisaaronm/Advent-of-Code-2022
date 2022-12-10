
def get_puzzle_input(filename: str) -> list:
    """
    - returns puzzle input as list
    """
    with open(filename, 'r') as f:
        values = f.read().splitlines()

    return values


def parse(lines):
    dir_vals = {}
    fullpath = []

    for line in lines:
        match line.split():
            ## add / to beginning of path
            case '$', 'cd', '/':
                root = line.split()[2]
                fullpath.append(root)
                dir_vals[root] = 0

            ## if cding into parent 
            case '$', 'cd', '..':
                dir_child_val = dir_vals[''.join(fullpath)]
                fullpath.pop()
                dir_vals[''.join(fullpath)] += dir_child_val

            ## update the path to be the cwd / directory being cd'd into
            case '$', 'cd', dir_name:
                fullpath.append(f'{dir_name}/')
                dir_vals[''.join(fullpath)] = 0

            ## skip if ls or dirname
            case ('$', 'ls') | ('dir', _):
                pass

            ## this should only catch files
            case _:
                fsize, fname = line.split()
                dir_vals[''.join(fullpath)] += int(fsize)

    ## this part adds up any remaining child values up into the parent
    while len(fullpath) > 1:
        try:
            dir_val = dir_vals[''.join(fullpath)]
            fullpath.pop()
            dir_vals[''.join(fullpath[:-1])] += dir_val
        except:
            dir_vals[fullpath[0]] += dir_val

    return dir_vals


def get_answer_p1(dir_sizes: dict) -> int:
    total_size = 0
    for dir_size in dir_sizes.values():
        if dir_size <= 100_000:
            total_size += dir_size
    
    return total_size


def get_answer_p2(dir_sizes: dict) -> int:
    space_total  = 70_000_000
    space_update = 30_000_000
    space_used   = dir_sizes['/']
    space_free   = space_total  - space_used
    space_needed = space_update - space_free

    smallest_dir = sorted([v for v in dir_sizes.values() if v >= space_needed])[0]

    return smallest_dir


def main():
    # filename = '07_example.txt' ## p1: 95_437 // p2: 24_933_642
    filename   = '07_input.txt'
    values     = get_puzzle_input(filename)
    dir_values = parse(values)
    
    answer_p1 = get_answer_p1(dir_values)
    print(answer_p1)
    
    answer_p2 = get_answer_p2(dir_values)
    print(answer_p2)


if __name__ == '__main__':
    main()
