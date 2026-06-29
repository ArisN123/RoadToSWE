

#goal is to recreate the title() function where a string's initials are capitalised


#version 1 
def title_rebuilt(input_string):
    input_string = input_string.lower()
    input_string = input_string.split()
    output = ''
    count = -1
    for x in input_string:
        count += 1 
        cap_letter = x[0].upper()
        name_as_list = list(x)
        name_as_list.pop(0)
        full_string = cap_letter
        for y in name_as_list:
            full_string += y
        if count != len(input_string)-1:
            full_string += ' '
        output += full_string
    return(output)


#version 2 
def title_rebuilt_v2(input_string):
    input_string = input_string.lower()
    input_string = list(input_string)
    for x in range(0,len(input_string)):
        if x !=0:
            if input_string[x-1] in [' ','-','_','.']:
                input_string[x] = input_string[x].upper()
        else:
            input_string[x] = input_string[x].upper()
    input_string = "".join(input_string)
    return(input_string)

#testing

test_cases = [
    ("hello world", "Hello World"),
    ("jAVAscript is FUN", "Javascript Is Fun"),
    ("the lord of the rings: the return of the king", "The Lord Of The Rings: The Return Of The King"),
    ("  multiple   spaces here   ", "  Multiple   Spaces Here   "),
    ("hello-world_from.chatgpt", "Hello-World_From.Chatgpt"),
]

test_output = True
for test_case in test_cases:
    if(test_case[1] != title_rebuilt_v2(test_case[0])):
        test_output = False

print(test_output)








