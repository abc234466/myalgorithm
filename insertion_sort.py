import random


def insertion_sort(lst: list) -> list:
    # import ipdb; ipdb.set_trace()
    for idx_1 in range(1, len(lst)):
        cur_val = lst[idx_1]
        idx_2 = idx_1 - 1
        while cur_val < lst[idx_2] and idx_2 >= 0:
            lst[idx_2 + 1] = lst[idx_2]
            idx_2 -= 1
        lst[idx_2 + 1] = cur_val
    print(lst)


list_a = random.sample([i for i in range(100)], 7)
print(f"Before insertion sort: {list_a}")
insertion_sort(list_a)
print(f"After insertion sort: {list_a}")
