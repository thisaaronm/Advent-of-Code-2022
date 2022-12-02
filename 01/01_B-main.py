
def get_input_data(filename: str) -> list:
    """
    - reads input file to `items` list
    - returns `items`
    """
    with open(filename, 'r') as f:
        items = f.read().splitlines()
        items.append('')

    return items


def get_all_calories(items: list) -> int:
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
    all_calories     = []
    food_items       = []

    for item in items:
        if len(item) != 0:
            food_items.append(int(item))
        else:
            current_calories = sum(food_items)
            all_calories.append(current_calories)
            
            food_items = []
    
    return all_calories


def get_top_three(all_calories: list) -> int:
    """
    - takes in `all_calories` list
    - sorts `all_calories` into `sorted_calories`
    - places the three highest calorie amounts into `top_three_calories`
    - returns the sum of `top_three_calories`
    """
    sorted_calories = sorted(all_calories)
    top_three_calories = sorted_calories[-3:]
    
    return sum(top_three_calories)


def main():
    food_items      = get_input_data('01_A-input.txt')
    all_calories    = get_all_calories(food_items)
    top_three_total = get_top_three(all_calories)
    print(top_three_total)


if __name__ == '__main__':
    main()
