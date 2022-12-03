
def get_puzzle_input(filename: str) -> list:
    """
    - reads filename to `items` list
    - returns `items`
    """
    with open(filename, 'r') as f:
        items = f.read().splitlines()

    return items


def get_item_types(items: list) -> list:
    """
    - iterates through list of items
        - splits each item in half
        - gets common element in each half (set intersection)
        - appends common element to `item_types` list
    - returns `item_types`
    """
    # if len(items) % 2 != 0: print(items)
    item_types = []
    for item in items:
        item_len = len(item)
        half_len = item_len // 2

        h1 = item[0:half_len]
        h2 = item[half_len:]

        item_type = set(h1).intersection(h2)
        item_types.append(''.join(item_type))
    
    return item_types


def get_priority(types: list) -> int:
    """
    - iterates through list of "item types" (UPPER and lowercase letters)
    - increments `total_priority` by the item's index in `priority`
    - returns `total_priority`
    """
    prioritiy = '_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    total_priority = 0
    for type in types:
        total_priority += prioritiy.index(type)
    
    return total_priority
    

def main():
    puzzle_input   = get_puzzle_input('03-input.txt')
    item_types     = get_item_types(puzzle_input)
    total_priority = get_priority(item_types)
    print(total_priority)


if __name__ == '__main__':
    main()
