def merge_sort(list):
    if len(list) > 1:
        mid = len(list) // 2
        left = list[:mid]
        right = list[mid:]
        print(left)
        print(right)
        merge_sort(left)
        merge_sort(right)
        i = 0
        k = 0
        j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                list[k] = left[i]
                i += 1
                k += 1
            else:
                list[k] = right[j]
                j += 1
                k += 1
        while i < len(left):
            list[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            list[k] = right[j]
            j += 1
            k += 1
list = ["n", "ew", "ga", "aw", "a", "fs", "rs", "psfv"]
merge_sort(list)
print(list)