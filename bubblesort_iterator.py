class BubbleSortIterator:
    def __init__(self, collection):
        self.collection = collection
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.collection):
            raise StopIteration
        else:
            self.index += 1
            return self.collection[self.index - 1]

class BubbleSort:
    def sort(self, collection):
        n = len(collection)
        for i in range(n):
            for j in range(n-i-1):
                if collection[j] > collection[j+1]:
                    collection[j], collection[j+1] = collection[j+1], collection[j]

if __name__ == "__main__":
    collection = [10, 7, 8, 9, 1, 5]
    iterator = BubbleSortIterator(collection)
    sort_algorithm = BubbleSort()
    sort_algorithm.sort(iterator)
    print(list(iterator))