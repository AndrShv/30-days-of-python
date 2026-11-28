import time


num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def print_all(items: list):
    for item in items:
        time.sleep(0.5)
        yield "Number: " + str(item) + ""

gen = print_all(num_list)
for i in gen:
    print(i)