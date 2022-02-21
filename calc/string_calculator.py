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
    return sum(numbers)

def normalize_custom_delimiter(param: str) -> str:
    if param.startswith("//"):
        delim = param[2]
        param = param[3:].replace(delim, ",").strip(',')
    return param
