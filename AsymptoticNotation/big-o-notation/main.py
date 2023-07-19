lst = [1, 2, 3, 4, 5]

# O(1). Get by index
a = lst[4]

# O(n). Step-by-step on list
for num in lst:
    print(num)

# O(n^2)
for num_1 in lst:
    for num_2 in lst:
        print(num_1 * num_2)


# O(log(n))
def binary_search(elem, lst):
    pass


binary_search(elem=2, lst=lst)
