from array import array


def merge_sorted_arrays(first_array, second_array):
    if not first_array:
        return second_array
    if not second_array:
        return first_array

    merged_array = array('l')
    first_len, second_len = len(first_array), len(second_array)
    i, j = 0, 0

    while i < first_len and j < second_len:
        if first_array[i] < second_array[j]:
            merged_array.append(first_array[i])
            i += 1
        else:
            merged_array.append(second_array[j])
            j += 1

    while i < first_len:
        merged_array.append(first_array[i])
        i += 1

    while j < second_len:
        merged_array.append(second_array[j])
        j += 1

    return merged_array
