# list.append
list = [2, 1, 3]
list.append(4)
print(list) # add one element at the end

#list.sort
list = [2, 1, 3]
print(list.sort())
print(list) # sort in ascending order

#list.sort(reserve = true)
list = [2, 1, 3]
print(list.sort(reverse = True)) # sort in descending order
print(list)

list = ['a', 'd', 'e', 'f', 'c', 'b']
print(list.sort())
print(list)

# list.reverse()
list = ['a', 'd', 'e', 'f', 'c', 'b']
list.reverse()
print(list) # reverse list

# list.insert(idx, el)
list = [2, 1, 3]
list.insert(1, 5)
print(list) # insert element at index

# list.remove(1)
list = [2, 1, 3]
list.remove(1)
print(list) # removes first occureence of element

# list.pop(idx)
list = [2, 1, 3, 1]
list.pop(2)
print(list) # removes element at idx
