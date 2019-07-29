def sort_count(array):
    if len(array) == 1:
        return array, 0
    else:
        mid = len(array)//2
        left_sorted, left_inversions = sort_count(array[:mid])
        right_sorted, right_inversions = sort_count(array[mid:])
        split_sorted, split_inversions = count_split_inv(left_sorted, right_sorted)
        return split_sorted, left_inversions+right_inversions+split_inversions

def count_split_inv(left_array, right_array):
    i = 0
    j = 0
    nr_inversions = 0
    merged_array = []

    while (i < len(left_array) and j < len(right_array)):
        if left_array[i] < right_array[j]:
            merged_array.append(left_array[i])
            i += 1
        else:
            merged_array.append(right_array[j])
            nr_inversions += len(left_array[i:])
            j += 1

    merged_array.extend(left_array[i:])
    merged_array.extend(right_array[j:])
    return merged_array, nr_inversions

def main():
    with open('IntegerArray.txt') as f:
        array = [int(x) for x in f]
    print("Number of inversions: ", sort_count(array)[1])

if __name__ == "__main__":
    main()
