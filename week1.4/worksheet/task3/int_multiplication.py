def int_multiplication(x, y):
    if y != 1:
        return x + int_multiplication(x, y - 1)
    else:
        return x

print(int_multiplication(9, 9))

def unique_combinations(nums, target):
    expression = ""
    current_target = 0

    OPERATORS = ['+', '-', '*', '/']

    for op1 in OPERATORS:
        for op2 in OPERATORS:
            if op1 == op2: continue
            for op3 in OPERATORS:
                if op2 == op3 or op1 == op3: continue
                
                expression = f"{nums[0]}{op1}{nums[1]}{op2}{nums[2]}{op3}{nums[3]}"

                if eval(expression) == target: return expression

    return ""
