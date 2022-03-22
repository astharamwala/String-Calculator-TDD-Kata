def add(param: str) -> int:
    """
        To calculate the string numbers

        :param: numbers in string
        :return: total of numbers passed as string
    """
    param = normalize_delimiters(param)
    if param:
        result = add_numbers(param)
        return result
    else:
        return len(param)

def normalize_delimiters(param: str) -> str:
    """
        Normalize the delimeters from string
    """
    param = normalize_custom_delimiter(param)
    return param.replace("\n", ",").strip(',')

def add_numbers(param: str) -> int:
    """ Add numbers and return total sum."""
    numbers = list(map(int, param.split(",")))
    numbers = validate_numbers(numbers)
    return sum(numbers)

def validate_numbers(param: str):
    """ Check for the negative values."""
    if any(num < 0 for num in param):
        raise ValueError("negatives not allowed " + str([num for num in param if num < 0]))

    param = [num for num in sorted(param, reverse=True) if num < 1001]
    return param

def normalize_custom_delimiter(param: str) -> str:
    """
        Normalize the custom delimeters from string
    """
    if param.startswith("//"):
        delim, param = param.split('\n', 1)

        # fetch multiple delims
        delims = delim.lstrip('/').split('][')
        for delim in delims:
            delim = delim.lstrip('[').rstrip(']')
            param = param.replace(delim, ",").strip(',')
    return param
