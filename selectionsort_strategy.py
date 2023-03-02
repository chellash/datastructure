class SelectionSort:
    def __init__(self, selection_strategy):
        self.selection_strategy = selection_strategy

    def sort(self, collection):
        n = len(collection)
        for i in range(n):
            min_index = self.selection_strategy.get_min_index(collection, i, n)
            collection[i], collection[min_index] = collection[min_index], collection[i]

class SelectionStrategy:
    def get_min_index(self, collection, i, n):
        pass

class MinElementSelection(SelectionStrategy):
    def get_min_index(self, collection, i, n):
        min_index = i
        for j in range(i + 1, n):
            if collection[j] < collection[min_index]:
                min_index = j
        return min_index

class MaxElementSelection(SelectionStrategy):
    def get_min_index(self, collection, i, n):
        max_index = i
        for j in range(i + 1, n):
            if collection[j] > collection[max_index]:
                max_index = j
        return max_index

if __name__ == "__main__":
    collection = [10, 7, 8, 9, 1, 5]
    selection_strategy = MinElementSelection()
    sort_algorithm = SelectionSort(selection_strategy)
    sort_algorithm.sort(collection)
    print(collection)

    collection = [10, 7, 8, 9, 1, 5]
    selection_strategy = MaxElementSelection()
    sort_algorithm = SelectionSort(selection_strategy)
    sort_algorithm.sort(collection)
    print(collection)
