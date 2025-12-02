import bisect

def list_basics():

    lst = []
    lst = ["a", "b", "c"]

    print(lst)

    fst_elem = lst[0]
    lst_elem = lst[-1]

    print(f"First element: {list[0]}, Last element: {lst_elem}")

    size = len(lst)

    print(f"List size: {size}")

    lst.append("d")

    print(f"After append: {lst}")

    lst.insert(1, "x")

    print("After insert at index 1:", lst)


    removed = lst.pop() # remove elements by index and return it

    print(f"After pop(): {lst}, removed element: {removed}")

    removed = lst.pop(1)

    print(f"After pop(1): {lst}, removed element: {removed}")

    del lst[0] # remove by index, return nothing

    print(f"After del lst[0]: {lst}")

    lst = ["a", "b", "c", "d", "c"]

    print(f"Before remove('c'): {lst}")

    fst_idx = bisect.bisect_left([1, 1, 1, 2, 3], 1)
    lst_idx = bisect.bisect_right([1, 1, 1, 2, 3], 1)

    print(f"First index of 1: {fst_idx}, Last index of 1: {lst_idx}")

    cnt_1 = [1, 1, 1, 2, 3].count(1)
    print(f"Count of 1 in the list {[1, 1, 1, 2, 3]} is {cnt_1}")

    lst.remove("c") # remove first occurrence by value and return nothing

    print(f"After remove('c'): {lst}")

    lst.clear() # remove all elements

    lst1 = [1, 2, 3]
    lst2 = [4, 5, 6]

    combined = lst1 + lst2

    lst1_extended = lst1.extend(lst2) # extend lst1 in place, return None

# slicing to get a subset of a list
# numbers[start_index: stop_index: step] stop_index is exclusive
def list_slicing():
    lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(f"Original list: {lst}")

    print(f"lst[1:-1]={lst[1:-1]}")

    print(f"lst[::2]={lst[::2]}")  # every second element

    print(f"lst[::-1]={lst[::-1]}")  # reverse the list\

    print(f"lst[-3:-1]={lst[-3:-1]}") # last third and second elements exclude the last one
    print(f"lst[-3:]={lst[-3:]}") # last two elements
    print(f"lst[-1:-3:-1]={lst[-1:-3:-1]}")  # last two elements in reverse order   

def list_operations():
    lst = [0, 1, 2, 3, 5, 0, 7]
    print(f"Original list: {lst}")
    reversed_lst = list(reversed(lst))
    print(f"Reversed list: {reversed_lst}")

    fst_element, *remaining = lst
    print(f"fst_element, *remaining = lst \r\nFirst element: {fst_element}, Remaining elements: {remaining}, Type of remaining: {remaining.__class__}")

    # overwrite original list
    print("Overwrite original list to keep only even numbers")
    lst = [1, 2, 3, 4, 5, 6, 7, 8]
    print(f"Original list: {lst}")
    lst[:] = [number for number in lst if number % 2 == 0]
    print(f"After overwriting lst[:] = new_lst: {lst}")

    for i, number in enumerate([1, 2, 3, 4, 5]):
        print(f"Element at position {i} is {number}")
    
    # list equality
    lst1 = [1, 2, 3]
    lst2 = [1, 2, 3]
    lst3 = [1, 2]
    print(f"{lst1}=={lst1} = {lst1==lst2}")
    print(f"{lst1}=={lst3} = {lst1==lst3}")


if __name__ == "__main__":
    #list_basics()   
    #list_slicing()
    list_operations()