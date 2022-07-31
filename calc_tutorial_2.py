def do_operation(x, y, operation):
    if(operation == '+'):
        return x+y
    elif(operation == '-'):
        return x-y
    elif(operation == '*'):
        return x*y
    elif(operation == '/'):
        return x/y

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
    res =  do_operation(input_numbers[0], input_numbers[1], input_operations[0])
    print(int(res))

main()
