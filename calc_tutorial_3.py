def do_operation(x, y, operation):
    if(operation == '+'):
        return x+y
    elif(operation == '-'):
        return x-y
    elif(operation == '*'):
        return x*y
    elif(operation == '/'):
        return x/y

def do_calc(numbers, operations):
    aux = numbers[0]
    for i in range(len(operations)):
        aux = do_operation(aux, numbers[i+1], operations[i])
    return aux

def main():
    calc = input('Inserir conta: ')
    input_numbers    = list()
    input_operations = list()
    possible_operations = ['+', '-', '/', '*']
    aux = ''
    for c in calc:
        if (c in possible_operations):
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
