from random import shuffle


def is_sorted(lst: list[int]) -> bool:
    if lst:
        current_index = 0
        for num in lst[1:]:
            if num < lst[current_index]:
                return False
            current_index += 1
    return True


def quick_sort(lst: list) -> None:
    """
    This algorithm basically run by luck.
    it takes a list as an input and keep shuffling it until it is sorted.

    """
    while True:
        if is_sorted(lst):
            break
        shuffle(lst)
