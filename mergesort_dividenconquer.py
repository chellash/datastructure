def merge_sort(collection):
    if len(collection) <= 1:
        return collection

    mid = len(collection) // 2
    left = collection[:mid]
    right = collection[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]
    return result

if __name__ == "__main__":
    collection = [10, 7, 8, 9, 1, 5]
    sorted_collection = merge_sort(collection)
    print(sorted_collection)
