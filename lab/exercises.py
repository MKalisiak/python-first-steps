def describe_list(arg: list) -> list:
    """
    Should return a list of tuples looking like this:
    [ (element_index, element), (element_index, element), ... ]

    The best solution would be a one-liner, but whatever works is fine
    """
    # return [(index, arg[index]) for index in range(len(arg))]
    return [(index, value) for index, value in enumerate(arg)]

def print_christmas_tree(width: int, height: int = 3, character: str = '*') -> None:
    """
    Example:
    print_christmas_tree(5)
      *
     ***
    *****
      *
     ***
    *****
      *
     ***
    *****
    :param width: has to be an odd number, number of characters in the lowest row
    :param height: number of triangle parts of the tree
    :param character: character used to print the tree
    :return: doesn't return anything, just prints

    If you have time, throw an error if width is even or if character is not exactly 1 char
    """
    for triangle in range(height):
        for row in range(1, width+1, 2):
            spaces = (width - row) // 2
            print(' ' * spaces + character * row + ' ' * spaces)

def remove_duplicates_loop(arg: list) -> list:
    """
    Remove duplicates from a list using a loop
    Example:
    remove_duplicates_set([1, 2, 3, 1, 5, 3, 2, 7]) == [1, 2, 3, 5, 7]

    :param arg: list to remove duplicates from
    :return: list with the same elements as arg, but without duplicates
    """
    deduplicated = []
    for item in arg:
        if item not in deduplicated:
            deduplicated.append(item)
    return deduplicated

def remove_duplicates_set(arg: list) -> list:
    """
    Remove duplicates from a list using a set
    Example:
    remove_duplicates_set([1, 2, 3, 1, 5, 3, 2, 7]) == [1, 2, 3, 5, 7]

    :param arg: list to remove duplicates from
    :return: list with the same elements as arg, but without duplicates
    """
    return list(set(arg))

def flatten_dicts(dicts: list) -> dict:
    """
    Merge a list of dicts into a single dicts. It should contain all keys from the dicts.
    Assume that dict values are numbers.
    If two or more dicts contain the same key,
        its value in the result dict should be a sum of all its values in given dicts

    Example:
    a = {'a': 1, 'b': 2}
    b = {'b': 3, 'c': 3}
    c = {'d': 6, 'a': 7}
    flatten_dicts([a, b, c]) == {'a': 8, 'b': 5, 'c':3, 'd': 6}

    :param dicts: list of dictionaries, assume keys are any type, values are numbers
    :return: dict that is a concatenation of dicts in param dicts
    """
    result = {}
    for _dict in dicts:
        for key, value in _dict.items():
            if key in result:
                result[key] = result[key] + value
            else:
                result[key] = value
    return result

def primes(limit: int) -> list:
    """
    Create a list of prime numbers from 0 to limit (inclusive)
    ProTip - you can create a function inside a function (not that it's necessary here, it just looks cool)
    Example:
    primes(7) == [2, 3, 5, 7]

    :param limit: the upper bound of prime search (inclusive)
    :return: list of prime numbers between 0 and limit
    """
    def is_prime(number: int) -> bool:
        if number == 0 or number == 1:
            return False
        if number == 2:
            return True
        for check_number in range(2, (number // 2) + 1):
            if number % check_number == 0:
                return False
        return True

    return [x for x in range(limit+1) if is_prime(x)]