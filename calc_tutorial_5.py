#! /usr/bin/env python3
import sys

DEBUG = 0

def do_operation(x, y, operation):
    if(operation == '+'):
        return x+y
    elif(operation == '-'):
        return x-y
    elif(operation == '*'):
        return x*y
    elif(operation == '/'):
        return x/y

def do_priority_calc(numbers, operations):
    tmp_numbers = []
    tmp_operations = []
    priority_operations = ['*', '/']
    for i in range(len(operations)):
        if(operations[i] in priority_operations):
            numbers[i+1] = do_operation(numbers[i], numbers[i+1], operations[i])
        else:
            tmp_numbers.append(numbers[i])
            tmp_operations.append(operations[i])
    tmp_numbers.append(numbers[-1]) # numbers[-1] = numbers[len(operations)]
    return tmp_numbers, tmp_operations

def do_calc(numbers, operations):
    numbers, operations = do_priority_calc(numbers, operations)
    if DEBUG: print(numbers)
    if DEBUG: print(operations)
    for i in range(len(operations)):
        numbers[i+1] = do_operation(numbers[i], numbers[i+1], operations[i])
    return numbers[-1]

def calculate(calc):
    if DEBUG: print('Expression to calculate: ' + calc)
    input_numbers    = list()
    input_operations = list()
    possible_operations = ['+', '-', '/', '*']
    aux = ''
    idx = 0
    while (idx < len(calc)):
        c = calc[idx]
        if (c == '('):
            if (aux != ''):
                input_numbers.append(float(aux))
                input_operations.append('*')
                aux = ''
            i_idx_subcalc = calc.find('(')+1
            f_idx_subcalc = calc.rfind(')')
            if DEBUG: print('Sub calculation between ' + str(i_idx_subcalc) + ' and ' + str(f_idx_subcalc))
            aux = calculate(calc[i_idx_subcalc:f_idx_subcalc])
            idx = f_idx_subcalc
        elif (c in possible_operations):
            input_numbers.append(float(aux))
            input_operations.append(c)
            aux = ''
        else:
            aux += c
        idx = idx + 1
    input_numbers.append(float(aux))
    if DEBUG: print(input_numbers)
    if DEBUG: print(input_operations)
    res = do_calc(input_numbers, input_operations)
    if DEBUG: print(int(res))
    return str(res)

if __name__ == "__main__":
    if (len(sys.argv) != 2):
        user_input = input('Inserir conta: ')
    else:
        user_input = sys.argv[1]
    final_result = calculate(user_input)
    print('Result: ' + str(final_result))
