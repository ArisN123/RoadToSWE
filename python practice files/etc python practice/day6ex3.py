# EX 3
# Messy input gauntlet
# Write a normalise() function and test it against these 6 inputs — 
# all should produce the same normalised string: "OMAR KHALID", "omar khalid", " Omar Khalid ", "OMAR-KHALID", "Omar Khalid", "dr. omar khalid".
# You may need to handle multiple spaces — look up " ".join(name.split()).

test_list = ["OMAR KHALID", "omar khalid", " Omar Khalid ", "OMAR-KHALID", "Omar Khalid", "dr. omar khalid"]

test_name = 'OMAR KHALID'

def normalise(input_string):
    input_string = input_string.strip().lower().replace('-',' ').replace('dr.','').strip()
    return input_string

for name in test_list:
    print(normalise(name))