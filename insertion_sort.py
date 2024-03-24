def insertion_sort(lst: list) -> list:
    for i in range(1, len(lst)):

        while i and lst[i] < lst[i - 1]:
            lst[i], lst[i - 1] = lst[i - 1], lst[i]

            i -= 1
    return lst
