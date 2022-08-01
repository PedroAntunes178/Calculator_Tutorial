#! /usr/bin/env python3

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
    print(numbers)
    print(operations)
    for i in range(len(operations)):
        numbers[i+1] = do_operation(numbers[i], numbers[i+1], operations[i])
    return numbers[-1]

def main():
    calc = input('Inserir conta: ')
    input_numbers    = list()
    input_operations = list()
    possible_operations = ['+', '-', '/', '*']
    aux = ''
    for c in calc:
        if ((c in possible_operations) and (aux != '')):
            input_numbers.append(float(aux))
            input_operations.append(c)
            aux = ''
        else:
            aux += c
    input_numbers.append(float(aux))
    print(input_numbers)
    print(input_operations)
    res = do_calc(input_numbers, input_operations)
    print(int(res))

main()
