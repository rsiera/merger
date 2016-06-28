from array import array


def merge_sorted_arrays_from_back(first_array, second_array):
    if not first_array:
        return second_array
    if not second_array:
        return first_array

    first_len, second_len = len(first_array), len(second_array)
    merged_array = array('l', first_array)
    merged_array.extend((0,) * second_len)

    i, j = first_len - 1, second_len - 1
    k = first_len + second_len - 1

    while i >= 0 and j >= 0:
        if first_array[i] > second_array[j]:
            merged_array[k] = first_array[i]
            k -= 1
            i -= 1
        else:
            merged_array[k] = second_array[j]
            j -= 1
            k -= 1
    return merged_array
