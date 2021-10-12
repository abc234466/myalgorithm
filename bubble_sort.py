import random


def bubble_sort(lst: list) -> list:
    for idx_1 in range(len(lst)):
        for idx_2 in range(idx_1+1, len(lst)):
            if lst[idx_1] > lst[idx_2]:
                lst[idx_1], lst[idx_2] = lst[idx_2], lst[idx_1]
    return lst


list_a = random.sample([i for i in range(100)], 7)
print(f"Before bubble sort: {list_a}")
print(f"After insertion sort: {bubble_sort(list_a)}")
