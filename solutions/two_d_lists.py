# TODO: Implement a function that takes a two-dimensional list and returns the sum of each row
def sum_each_row(two_d_list):
    result = []
    for row in two_d_list:
        sum = []
        for j in range(len(row)):
            sum = sum + row[j]
        result.append(sum)
    return result
        


# TODO: Implement a function that counts the number of non-zero elements in a two-dimensional list
def count_non_zero(two_d_list):
    sum = 0
    for row in two_d_list:
        for item in row:
            if item != 0:
                sum = sum +1
    return sum



# TODO: Implement a function that extracts and returns the last element of each row in a two-dimensional list
def last_elements(two_d_list):
    
    result = []
    if len(two_d_list) > 0:    
        for i in range(len(two_d_list)):
            result.append (two_d_list[i][len(two_d_list[i])-1])
    return result
            
    
           
# TODO: Implement a function that counts the number of times a given value appears in a two-dimensional list
def count_occurrences(two_d_list, value):
    result = 0
    for row in two_d_list:
        for item in row:
            if item == value:
                result = result +1
    return result
