import json

def ask_for_fav_number():
    while True:
        fav_number = input('what is your fav number?\n')
        try:
            fav_number = int(fav_number)
        except ValueError:
            print(f'{fav_number} is not a valid number, please try again\n')
        else:
            return(fav_number)

def save_fav_number(favourite_number):
    file_path = 'fav_number.json'
    with open(file_path, 'w') as opened_path:
        json.dump(favourite_number, opened_path)
        print(f'I will remember that your favorite number is {favourite_number}')


def load_fav_number():
    file_path = 'fav_number.json'
    with open(file_path, 'r') as opened_file:
        fav_number = json.load(opened_file)
        return(fav_number)



def say_fav_number():
    file_path = 'fav_number.json'
    try:
        open(file_path,'r')
    except FileNotFoundError:
        favourite_number = ask_for_fav_number()
        save_fav_number(favourite_number)
        return(f'fav number saved as {favourite_number}')
    else:
        return(load_fav_number())
    

