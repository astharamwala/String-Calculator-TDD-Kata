def add(param: str) -> int:
    param = normalize_delimiters(param)
    if param:
        result = add_numbers(param)
        return result
    else:
        return len(param)

def normalize_delimiters(param: str) -> str:
    param = normalize_custom_delimiter(param)
    return param.replace("\n", ",").strip(',')

def add_numbers(param: str) -> int:
    numbers = list(map(int, param.split(",")))
    validate_numbers(numbers)
    return sum(numbers)

def validate_numbers(param: str):
    if any(num < 0 for num in param):
        raise ValueError("negatives not allowed " + str([num for num in param if num < 0]))

def normalize_custom_delimiter(param: str) -> str:
    if param.startswith("//"):
        delim, param = param.split('\n', 1)
        delim = delim.lstrip('/')
        param = param.replace(delim, ",").strip(',')
    return param
