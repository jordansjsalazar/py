def merge (lst1, lst2):
    if lst1==[]:
        return lst2
    elif lst2==[]:
        return lst1
    if lst1[0] < lst2[0]:
        return [lst1[0]] + merge(lst1[1:], lst2)
    else:
        return [lst2[0]] + merge(lst2[1:], lst1)
        
print(merge([1, 2, 3], [0, 6, 7]))

print(merge([0, 2, 5], [1, 3, 4]))

print(merge([0, 2, 6], [1, 2, 3, 4, 5]))