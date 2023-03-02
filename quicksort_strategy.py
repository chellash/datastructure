from typing import List

class QuickSort:
    def __init__(self, partition_strategy):
        self.partition_strategy = partition_strategy

    def sort(self, collection):
        if len(collection) <= 1:
            return collection

        pivot = self.partition_strategy(collection)

        left = []
        right = []
        for item in collection:
            if item < pivot:
                left.append(item)
            elif item > pivot:
                right.append(item)

        left = self.sort(left)
        right = self.sort(right)

        return left + [pivot] * collection.count(pivot) + right

def first_element_partition(collection):
    return collection[0]

def middle_element_partition(collection):
    return collection[len(collection) // 2]

if __name__ == "__main__":
    collection = [10, 7, 8, 9, 1, 5]
    sort_algorithm = QuickSort(first_element_partition)
    sorted_collection = sort_algorithm.sort(collection)
    print(sorted_collection)

    collection = [10, 7, 8, 9, 1, 5]
    sort_algorithm = QuickSort(middle_element_partition)
    sorted_collection = sort_algorithm.sort(collection)
    print(sorted_collection)
