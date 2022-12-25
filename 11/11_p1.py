
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


def process_rounds(monkeys: dict, rounds: int = 1) -> int:
    count = 0
    while count < rounds:
        for k, v in monkeys.items():
            while len(v['items']) > 0:
                i = v['items'].pop(0)
                v['inspected'] += 1
                #print(i)
                #print(v['op'][0])
                
                if v['op'][1] == 'old':
                    op_num = i
                else:
                    op_num = v['op'][1]
                    
                if v['op'][0] == '+':
                    worry = i + op_num
                elif v['op'][0] == '*':
                    worry = i * op_num
                
                worry = worry // 3
                if worry % v['test'] == 0:
                    monkeys[v['true']]['items'].append(worry)
                else:
                    monkeys[v['false']]['items'].append(worry)
        count += 1
    
    inspected = sorted([v['inspected'] for k, v in monkeys.items()])
    print(inspected[-2] * inspected[-1])
                
                


def main():
    #filename = '11_ex1.txt' ## p1: 10605 || p2: ?
    filename = '11_input.txt' ## 118674
    values = get_puzzle_input(filename)
    monkeys = parse_input(values)
    process_rounds(monkeys, 20)


if __name__ == '__main__':
    main()
