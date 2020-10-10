#Binary Search 

def binary_search(list, item):
    low = 0 #the lowest part of the list you will search in, starts at zero because the lowest index in every list is 0 
    high = len(list)-1 #the last index number will be the length of the list minus 1 because index numbers start at 0... mini ex) [0,2,5,8] || length of the list is 4 so the last index number will be 3

    while low <= high: # while we haven't gotten the index place we want yet 
        mid = (low + high) #checking middle element 
        guess = list[mid]  #checking middle element 
        if guess == item: # if the guess equals the mid then we return the mid 
            return mid
        if guess > item: #if the guess is high
            high = mid - 1
        else:
            low = mid + 1 # if the guess is too low 
    return None # if the item is not in the list 

my_list = [1, 3, 5, 7, 9]

print(binary_search(my_list,3))
print(binary_search(my_list,-1))