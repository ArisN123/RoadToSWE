# EX 2
# Split and rejoin
# Take a full name string, split it into parts, reverse the order (last name first), and rejoin with a comma. "Ahmed Ali Hassan" → "Hassan, Ahmed Ali".

name = "Ahmed Ali Hassan" 



def rearrange_name(input_string):
    list_name = input_string.split()
    final_output = f'{list_name[-1]}, {" ".join(list_name[:-1])}'
    return final_output
print(rearrange_name(name))

