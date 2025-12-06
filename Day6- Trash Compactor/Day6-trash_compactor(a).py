

'''
Docstring for Day6-trash_compactor
https://adventofcode.com/2025/day/6

'''
def trash_compactor(input):
    lines = input.splitlines()
    operator_line = lines[-1]
    number_lines = lines[:-1]  

    operators = operator_line.split()
    total_column = len(operators)
    
    coloumns = []
    for i in range(total_column):
        coloumns.append([])

    for row in number_lines:
        parts = row.split()
        for i in range(total_column):
            coloumns[i].append(int(parts[i]))

    results = []

    for i in range(total_column):
        col = coloumns[i]
        op = operators[i]

        if op == '+':
            results.append(sum(col))
        elif op == '*':
            product = 1
            for val in col:
                product *= val
            results.append(product)

    final_answer = sum(results)
    return final_answer



with open('input(a).txt' ,'r' ) as file:
    file_content=file.read()
    print(trash_compactor(file_content))