x = ["a", "b", "c", "d", "e", "f", "g", "h", "i"] 
y = [ 0,   1,   6,    4,   5,   3,   2,   8,   9] 
def sort_list(list1, list2): 
    zipped_pairs = zip(list2, list1) 
    z = [x for _, x in sorted(zipped_pairs)] 
    return z

print(sort_list(x, y)) 