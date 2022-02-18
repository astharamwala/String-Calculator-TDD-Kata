from calc.string_calculator import add

# TDD CYCLE
# 1. MAKE TEST THAT FAILS
# 2. MAKE THE TEST PASS
# 3. REFACTOR

def test_string_calc_should_return_zero_on_empty_string():
    result = add("")
    assert result == 0, "String calculater should return 0 on empty string"

def test_string_calc_should_return_correct_value_on_one():
    result = add("1")
    assert result == 1, "String calculater should return 1 on \"1\" string"

def test_string_calc_should_return_correct_value_on_two():
    result = add("2")
    assert result == 2, "String calculater should return 2 on \"2\" string"