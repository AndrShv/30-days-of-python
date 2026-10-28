msg = "Hello World!"
print(msg)




num = 5
def update_num(x):
    return x + 10

new_num = update_num(num)
print(new_num)


my_list = [1, 2, 3]
my_tuple = (1, my_list)

print(my_tuple)
print(id(my_tuple))
print(id(my_list))


my_list.append(4)

print(my_tuple)
print(id(my_tuple))
print(id(my_list))




import copy

original = [[1, 2], [3, 4]]
shallow = copy.copy(original)
deep = copy.deepcopy(original)

original[0].append(99)

print(shallow)
print(deep)


