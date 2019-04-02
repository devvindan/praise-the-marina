# to-do: actually implement algorithms for grammar inference

dict_first_step = {
    "S": ["cA1", "bA4"],
    "A1": ["aA2"],
    "A2": ["aA3"],
    "A3": ["ab", "b"],
    "A4": ["bA5"],
    "A5": ["aA6"],
    "A6": ["ab"],
}

dict_second_step = {
    "S": ["cA1", "bA4"],
    "A1": ["aA2", "b"],
    "A2": ["aA2", "b"],
    "A4": ["bA5"],
    "A5": ["aA5"],
    "A5": ["b"]
}

dict_third_step = {
    "S": ["cA", "bB"],
    "A": ["aA", "b"],
    "B": ["bA"],
}