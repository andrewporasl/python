def reverse_sort_dictionary(dict):
    keys = list(dict.keys())

    n = len(keys)
    for i in range(n):
        for j in range(0, n-i-1):
            if [keys[j]] < [keys[j+1]]:
                keys[j], keys[j+1] = keys[j+1], keys[j]

    sorted = [(key, dict[key][0]) for key in keys]
    return sorted

d = {'Tom': (5464512, 24), 'Sara': (5446987, 32), 'Mary': (1557896, 20)}
print(reverse_sort_dictionary(d))
