
def get_first_num():
    first_num = input('please choose the first number\npress q to quit\n')
    if first_num == 'q':
        return('user quit')
    else:
        try:
            first_num = int(first_num)
        except ValueError:
            print('invalid input,please insert valid number\n')
            return(get_first_num())
        else:
            return int(first_num)
    
def get_second_num():
    second_num = input('please choose the second number\npress q to quit\n')
    if second_num == 'q':
        return('user quit')
    else:
        try:
            second_num = int(second_num)
        except ValueError:
            print('invalid input,please insert valid number\n')
            return(get_second_num())
        else:
            return int(second_num)

def add_two_values():
    first_num_val = get_first_num()
    second_num_val = get_second_num()
    if first_num_val != 'user_quit' and second_num_val != 'user quit':
        return(f'{first_num_val + second_num_val}')
    else:
        return('user quit')