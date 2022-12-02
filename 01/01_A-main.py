
def get_input_data(filename: str) -> list:
    """
    - reads input file to `items` list
    - returns `items`
    """
    with open(filename, 'r') as f:
        items = f.read().splitlines()
        items.append('')

    return items


def get_total_calories(items: list) -> int:
    """
    - instantiates `current_calories` and `total_calories` to 0
    - instantiates `food_items` to empty list
    - iterates through `items` list
        - appends lines with len > 0 to `food_items` list
        - on lines where len == 0:
            - sums `food_items` list to `current_calories`
            - compares `current_calories` against `total_calories`
            - if `current_calories` is greater than `total_calories`, set `total_calories` to `current_calories`
            - sets `food_items` back to empty list
    - returns `total_calories`
    """
    current_calories = 0
    total_calories   = 0
    food_items       = []

    for item in items:
        if len(item) != 0:
            food_items.append(int(item))
        else:
            current_calories = sum(food_items)
            if current_calories > total_calories:
                total_calories = current_calories
            
            food_items = []
    
    return total_calories


def main():
    food_items     = get_input_data('01_A-input.txt')
    total_calories = get_total_calories(food_items)
    print(total_calories)


if __name__ == '__main__':
    main()
