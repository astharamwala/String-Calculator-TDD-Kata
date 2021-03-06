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

def test_string_calc_should_add_two_numbers():
    result = add("1,2")
    assert result == 3, "String calculater should return 3 for \"1,2\" string"

    result = add("5,10")
    assert result == 15, "String calculater should return 15 for \"5,10\" string"

def test_string_calc_should_allow_new_line_character_between_numbers_as_delimiter():
    result = add("5\n10")
    assert result == 15, "String calculater should return 15 for \"\\n5,10\" string"

    result = add("1\n2,3")
    assert result == 6, "String calculater should return 6 for \"1\\n2,3\" string"

    result = add("\n4,2\n3\n")
    assert result == 9, "String calculater should return 9 for \"\\n4,2\\n3\\n\" string"

def test_string_calc_should_allow_to_add_custom_delimiter():
    result = add("//;\n1;2")
    assert result == 3, "String calculater should return 3 for \"//;\\n1;2\" string"

    result = add("//#\n4#2#7")
    assert result == 13, "String calculater should return 13 for \"//#\\n4#2#7\" string"  

def test_string_calc_negative_number_exception_check():
    try:
        add("1\n-2,3")
    except ValueError as e:
        assert str(e) == "negatives not allowed [-2]"

def test_string_calc_should_allow_to_add_custom_delimiter_for_multiple_chars():
    result = add("//;+-\n1;+-2")
    assert result == 3, "String calculater should return 3 for \"//;\\n1;2\" string"

    result = add("//#*o\n4#*o2#*o7")
    assert result == 13, "String calculater should return 13 for \"//#\\n4#2#7\" string"  