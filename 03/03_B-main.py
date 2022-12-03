
def get_puzzle_input(filename: str) -> list:
    """
    - reads filename to `items` list
    - returns `items`
    """
    with open(filename, 'r') as f:
        items = f.read().splitlines()

    return items


def divide_into_groups(items: list) -> list:
    """
    - while the list of items is greater than 0
        - append the first 3 items into a new `groups` list
        - reassign the list of items to itself, without the first 3 items
    - returns `groups`
    """
    # if len(items) % 3 != 0: raise ValueError('Not evenly divisible by 3')
    groups = []
    while len(items) > 0:
        groups.append(items[0:3])
        items = items[3:]
    
    return groups


def get_badges(items: list) -> list:
    """
    - iterates through list of rucksacks (items)
        - splits each item into rucksack1 through 3
        - gets the badge (common element) in rucksack (set intersection)
        - appends badge to `badges` list
    - returns `bagdes`
    """
    
    badges = []
    for item in items:
        rs1, rs2, rs3 = item
        badge = set(rs1).intersection(rs2, rs3)
        badges.append(''.join(badge))
    
    return badges


def get_priority(badges: list) -> int:
    """
    - iterates through list of "badge types" (UPPER and lowercase letters)
    - increments `total_priority` by the badges' index in `priority`
    - returns `total_priority`
    """
    prioritiy = '_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    total_priority = 0
    for badge in badges:
        total_priority += prioritiy.index(badge)
    
    return total_priority
    

def main():
    puzzle_input   = get_puzzle_input('03-input.txt')
    groups_of_items = divide_into_groups(puzzle_input)
    badges = get_badges(groups_of_items)
    total_priority = get_priority(badges)
    print(total_priority)


if __name__ == '__main__':
    main()
