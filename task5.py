# task5
def correctConditions(a, b, c):
    is_condition1_true = a < b < c

    is_condition2_true = a > 0 or b > 0 or c > 0

    is_condition3_true = ((a > 0 and b <= 0 and c <= 0)
                          or (a <= 0 and b > 0 and c <= 0)
                          or (a <= 0 and b <= 0 and c > 0))
    info = f'''
    [{a},{b},{c}]
    "a < b < c:", {is_condition1_true}
    "Хоча б одне з чисел додатне:", {is_condition2_true}
    "Рівно одне з чисел додатне:", {is_condition3_true}
    '''
    print(info)


correctConditions(2, 4, 69)
correctConditions(12, -4, -69)
correctConditions(-2, 4, 69)
