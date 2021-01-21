def reverse_list(input_list):
    """
    Reverses order of elements in list input_list.
    """
    idx1 = 0
    idx2 = len(input_list)-1
    while(idx1<idx2):
    	input_list[idx1], input_list[idx2] = input_list[idx2], input_list[idx1]
    	idx1+=1
    	idx2-=1
    return input_list

def count_digits(number):
    """
    Return count of digits
    """
    counter = 0
    while(number!=0):
    	counter+=1
    	number=number//10
    return counter