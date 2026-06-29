


file_path = "C:/Users/aris123/Desktop/python_practice/demo files/1m.txt"
pi_list = ''
with open(file_path) as opened_pi_file:
    for line in opened_pi_file:
        pi_list  =  pi_list + line


pi_list = '3.' + pi_list


dob = '231101' 

if dob in pi_list:
    print(f'DOB {dob} is found within pi_list')
else:
    print(f'DOB {dob} not in list :(')
