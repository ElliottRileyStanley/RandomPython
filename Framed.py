from itertools import product

def filtered_product(iterable, repeat, *condition_fns):
    """
    Generator function that yields elements from product(iterable, repeat) 
    only if they satisfy all condition functions.
    
    :param iterable: The input list for the Cartesian product
    :param repeat: The number of times to repeat the iterable
    :param condition_fns: A list of functions that return True if the element should be included
    """
    for item in product(iterable, repeat=repeat):
        if all(fn(item) for fn in condition_fns):
            yield item

# Example usage
def lightGreen(tup):
    return tup[0] == 5 or tup[1] == 4 or tup[2] == 5 or tup[5] == 3 or (tup[7] == 7 and tup[2] == 6) or (tup[8] == 7 or tup[2] == 6) or tup[9] == 1

def red1(tup):
    return tup[0] == 2 or tup[2] == 7 or tup[3] == 3 or tup[4] == 3 or tup[5] == 5

def red2(tup):
    return tup[0] == 8 or tup[3] == 8 or tup[5] == 7 or (tup[6] == 7 and tup[2] == 6) or (tup[7] == 7 and tup[2] == 6)

def red3(tup):
    return tup[1] == 8 or (tup[3] == 1 and tup[2] == 2) or tup[6] == 8 or (tup[7] == 1 and tup[2] == 2) or tup[8] == 2 or (tup[9] == 7 and tup[2] == 4)

for result in filtered_product([1, 2, 3, 4, 5, 6, 7, 8], 10, lightGreen, red1, red2, red3):
    print(result)
