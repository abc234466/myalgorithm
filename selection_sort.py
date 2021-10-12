import random


def selection_sort(lst: list) -> list:
    for idx_1, num_1 in enumerate(lst):
        minimum = num_1
        mini_idx = idx_1
        for idx_2, num_2 in enumerate(lst[idx_1:]):
            if num_2 < minimum:
                mini_idx = idx_2 + idx_1
                minimum = num_2
        lst[idx_1], lst[mini_idx] = minimum, lst[idx_1]
    return lst


list_a = random.sample([i for i in range(100)], 7)
print(f"After insertion sort: {selection_sort(list_a)}")
