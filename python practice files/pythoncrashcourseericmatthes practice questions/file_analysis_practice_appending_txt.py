



#10-3
# file_path = "C:/Users/aris123/Desktop/python_practice/demo files/guest.txt"
# with open(file_path, mode = 'a') as opened_file:
#     response = input('please enter your name in the guest list\n')
#     opened_file.write(response+ '\n')



#10-4
file_path = "C:/Users/aris123/Desktop/python_practice/demo files/guest_list.txt"
with open(file_path, mode = 'a') as opened_file:
    response = ''
    while True:
        response = input('please enter your name in the guest list; write "q" to quit\n')
        if response != 'q':
            opened_file.write(response+'\n')
            print(f'Welcome {response}!')
        else:
            break
