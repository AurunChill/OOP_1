def _is_number(value) -> bool:
    """
    Checks if the given value can be converted to a float.

    :param value: The value to check
    :return: True if the value is a number, False otherwise
    """
    try:
        float(value)
        return True
    except ValueError:
        return False


class Pair:
    def __init__(self, first: float = None, second: float = None):
        """
        Initializes a Pair instance with two numbers.

        :param first: The first number of the pair
        :param second: The second number of the pair
        """
        self.first = first
        self.second = second

    def read(self):
        """
        Reads two numbers from user input and assigns them to the pair.
        Raises a ValueError if the input is not a number.
        """
        first_input = input('Enter first argument: ')
        if not _is_number(first_input):
            raise ValueError('Argument must be number!')
        second_input = input('Enter second argument: ')
        if not _is_number(second_input):
            raise ValueError('Argument must be number!')
        first_input, second_input = float(first_input), float(second_input)
        if first_input > second_input:
            raise ValueError('First argument must be greater than second one!')

        self.first = first_input
        self.second = second_input

    def display(self):
        """
        Displays the range defined by the pair.
        """
        print(f'Range: ({self.first}:{self.second})')

    def rangecheck(self, number: int | float) -> bool:
        """
        Checks if a number is within the range defined by the pair.

        :param number: The number to check
        :return: True if the number is within the range, False otherwise
        """
        return self.first < number < self.second


def make_pair(first: int | float, second: int | float) -> Pair:
    """
    Creates a Pair instance with the given numbers.

    :param first: The first number
    :param second: The second number
    :return: A Pair instance
    :raises ValueError: If arguments are not numbers
    """
    if type(first) not in (int, float) or type(second) not in (int, float):
        raise ValueError('Arguments must be numbers!')
    elif first >= second:
        raise ValueError('First argument must be less than the second argument!')
    else:
        return Pair(first=first, second=second)


if __name__ == '__main__':
    pair = make_pair(5, 10)
    pair.display()

    pair.read()

    try:
        print('Check 7 in range:', pair.rangecheck(7))
        print('Check 4 in range:', pair.rangecheck(4))
        print('Check 10 in range:', pair.rangecheck(10))
    except ValueError as e:
        print(e)
