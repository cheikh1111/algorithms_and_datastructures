def selection_sort(lst: list) -> list:
    # Lists are mutable so your list will be sorted in place
    for i in range(len(lst) - 1):
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[i]:
                lst[i], lst[j] = lst[j], lst[i]


# Example
my_list = [1, 3, 2, 8, 4]
selection_sort(my_list)
print(my_list)  # Outputs: [1,2,3,4,8]
