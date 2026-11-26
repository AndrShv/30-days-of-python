

def build_prefix_sums(arr):
    pref = [0] * (len(arr) + 1) # заполняет всю 0, но длина arr+1
    for i in range(len(arr)):
        pref[i + 1] = pref[i] + arr[i]
    return pref


def range_sum(pref, left, right):
    return pref[right + 1] - pref[left]

my_arr = [5, 10, 15, 20, 25, 30]
pref = build_prefix_sums(my_arr)
print(range_sum(pref, 0, 2 ))
print(range_sum(pref, 1, 3 ))
