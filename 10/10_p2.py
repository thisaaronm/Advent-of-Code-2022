
def get_input(filename):
    with open(filename) as f:
        instructions = f.read().splitlines()

    return instructions


def check_sprite(cyc, reg):
    match cyc:
        case cyc if cyc < 40:
            row = 0
        case cyc if cyc < 80:
            row = 1
            cyc -= 40
        case cyc if cyc < 120:
            row = 2
            cyc -= 80
        case cyc if cyc < 160:
            row = 3
            cyc -= 120
        case cyc if cyc < 200:
            row = 4
            cyc -= 160
        case cyc if cyc < 240:
            row = 5
            cyc -= 200

    if reg in [cyc - 1, cyc, cyc + 1]:

        return True, row, cyc

    return False, row, cyc


def check_instructions(INSTR, REGIS, CYCLE, REGISTER, SCREEN):
    if INSTR == 'noop':
        BOOL, ROW, CYC = check_sprite(CYCLE, REGISTER)
        if BOOL: SCREEN[ROW][CYC] = '#'
        CYCLE += 1
        REGISTER += REGIS
    
    if INSTR == 'addx':
        BOOL, ROW, CYC = check_sprite(CYCLE, REGISTER)
        if BOOL: SCREEN[ROW][CYC] = '#'
        CYCLE += 1
    
        BOOL, ROW, CYC = check_sprite(CYCLE, REGISTER)
        if BOOL: SCREEN[ROW][CYC] = '#'
        CYCLE += 1
        REGISTER += REGIS

    return CYCLE, REGISTER, SCREEN


def main():
    #fn = '10_ex1.txt'
    fn = '10_input.txt'
    instructions = get_input(fn)

    screen = [['.' for _ in range(40)] for _ in range(6)]
    cycles   = 0
    register = 1

    for i in instructions:
        try:
            instr, regis = i.split()
            regis = int(regis)
        except:
            instr = i
            regis = 0

        cycles, register, screen = check_instructions(instr, regis, cycles, register, screen)

    for s in screen:
        print(''.join(s))


if __name__ == '__main__':
    main()
