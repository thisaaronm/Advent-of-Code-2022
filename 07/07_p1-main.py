
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
                # print(dir_vals[''.join(fullpath))

                fullpath.pop()
                
                dir_vals[''.join(fullpath)] += dir_child_val
                # print(dir_vals[''.join(fullpath)])

            ## update the path to be the cwd / directory being cd'd into
            case '$', 'cd', dir_name:
                fullpath.append(f'{dir_name}/')
                dir_vals[''.join(fullpath)] = 0

            ## skip if ls or dirname
            case ('$', 'ls') | ('dir', _):
                pass

            ## only files should be caught by this
            case _:
                fsize, fname = line.split()
                # print(fullpath, fname, fsize)

                dir_vals[''.join(fullpath)] += int(fsize)

    return dir_vals


def get_answer(dir_sizes: dict) -> int:
    total_size = 0
    for dir_size in dir_sizes.values():
        if dir_size <= 100_000:
            total_size += dir_size
    
    return total_size


def main():
    # filename = '07_example.txt' ## should return 95_437
    filename   = '07_input.txt'
    values     = get_puzzle_input(filename)
    dir_values = parse(values)
    answer     = get_answer(dir_values)

    print(answer)


if __name__ == '__main__':
    main()
