
def get_input(filename):
    with open(filename) as f:
        instructions = f.read().splitlines()
    
    return instructions


def get_signal_strength(instructions):
    cycles   = [20, 60, 100, 140, 180, 220]
    cycle    = 0
    register = 1
    signal   = 0

    for instruction in instructions:
        try:
            instr, regis = instruction.split()
            regis = int(regis)
        except:
            instr = instruction
            regis = 0

        match instr:
            case 'noop':
                cycle   += 1
                register += regis

                if cycle in cycles:
                    signal += cycle * register
            case 'addx':
                cycle += 1
                if cycle in cycles:
                    signal += cycle * register

                cycle += 1
                if cycle in cycles:
                    signal += cycle * register

        register += regis

    return signal


def main():
    # fn = '10_ex1.txt'
    fn = '10_input.txt'

    puzzle_input    = get_input(fn)
    signal_strength = get_signal_strength(puzzle_input)

    print(signal_strength)


if __name__ == '__main__':
    main()
