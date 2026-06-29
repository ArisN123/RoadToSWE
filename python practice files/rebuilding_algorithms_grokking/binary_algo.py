#algorithm
test_list  = [5,10,25,35,47,67,499]

def binary_search(sorted_list,value_to_find):
    iterations = 0
    min_index = 0
    max_index = len(sorted_list)-1
    while min_index <= max_index:
        iterations += 1 
        middle_index = (min_index + max_index) // 2 
        if sorted_list[middle_index] > value_to_find:
            max_index = middle_index-1
        elif sorted_list[middle_index] < value_to_find:
            min_index = middle_index+1
        elif sorted_list[middle_index] == value_to_find:
            return(f"took {iterations} iterations to find value {value_to_find} in position {middle_index}")
    return("value not in list")
        


#print(binary_search(test_list,999))


def max_iterations_binary_search(items):
    items = items//2
    iterations = 0 
    while items>0:
        iterations += 1
        items = items // 2 
    return iterations
        

# print(max_iterations_binary_search(5))



