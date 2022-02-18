def add(param: str) -> int:
    if len(param) == 0:
        return 0
    elif len(param) == 1:
        return int(param)
    else:
        numbers_list = map(int, param.split(","))
        return sum(numbers_list)
