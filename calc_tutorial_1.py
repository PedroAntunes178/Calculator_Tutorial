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
    possible_operations = ['+', '-', '/', '*']
    res = do_operation(int(calc[0]), int(calc[2]), calc[1])
    print(int(res))

main()
