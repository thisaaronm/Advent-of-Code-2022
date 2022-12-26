
'''
Resources for figuring this one out:
- https://medium.com/@datasciencedisciple/advent-of-code-2022-in-python-day-11-5832b8f25c21
- https://github.com/silentw0lf/advent_of_code_2022/blob/main/11/solve.py
'''

def get_puzzle_input(filename: str) -> list:
    """
    - returns puzzle input as list
    """
    with open(filename, 'r') as f:
        values = f.read().splitlines()

    return values


def parse_input(lines: list) -> dict:
    monkeys = {}
    for line in lines:
        match line.strip().split():
            case 'Monkey', num:
                num = num[0]
                monkeys[num] = {'inspected': 0}
            case 'Starting', 'items:', *s_items:
                s_items = [int(i.split(',')[0]) for i in s_items]
                monkeys[num]['items'] = s_items
            case 'Operation:', 'new', '=', 'old', op, op_num:
                if op_num.isnumeric():
                    op_num = int(op_num)
                monkeys[num]['op'] = [op, op_num]
            case 'Test:', 'divisible', 'by', test_num:
                monkeys[num]['test'] = int(test_num)
            case 'If', 'true:', 'throw', 'to', 'monkey', true_num:
                monkeys[num]['true'] = true_num
            case 'If', 'false:', 'throw', 'to', 'monkey', false_num:
                monkeys[num]['false'] = false_num
            case _:
                pass

    return monkeys


def process_rounds(monkeys: dict, rounds: int = 1, part: int = 1) -> int:
    count = 0

    if part == 2:
        test_ = 1
        for t in monkeys.values():
            test_ *= t['test']

    while count < rounds:
        for val in monkeys.values():
            while len(val['items']) > 0:
                item = val['items'].pop(0)
                val['inspected'] += 1

                if val['op'][1] == 'old':
                    op_num = item
                else:
                    op_num = val['op'][1]

                if val['op'][0] == '+':
                    worry = item + op_num
                elif val['op'][0] == '*':
                    worry = item * op_num

                if part == 2:
                    worry %= test_
                elif part == 1:
                    worry //= 3

                if worry % val['test'] == 0:
                    monkeys[val['true']]['items'].append(worry)
                else:
                    monkeys[val['false']]['items'].append(worry)

        count += 1


def main():
    part   = 2
    rounds = 20 if part == 1 else 10000

    # filename = '11_example.txt' ## p1: 10605 || p2: 2713310158
    filename = '11_input.txt'
    values   = get_puzzle_input(filename)
    monkeys  = parse_input(values)

    process_rounds(monkeys, rounds, part)
    
    inspected = sorted([v['inspected'] for v in monkeys.values()])
    print(inspected[-2] * inspected[-1])


if __name__ == '__main__':
    main()
