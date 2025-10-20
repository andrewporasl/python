def merge_list(list1, list2):
    merged = list1 + list2
    for i in range(1, len(merged)):
        key = merged[i]
        j = i - 1
        while j >= 0 and key < merged[j]:
            merged[j + 1] = merged[j]
            j -= 1
        merged[j + 1] = key

    return merged

