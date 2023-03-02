<h1>Data structure algorithm samples from ChatGPT using GoF patterns</h1>

<h2>Bubble sort using Iterator pattern</h2>
The Iterator pattern is used to provide a way to access the elements of an aggregate object (such as an array) sequentially, without exposing the underlying implementation. It is useful when you have a collection of objects that you want to iterate over, but you don't want to expose the internal representation of the collection to the client.

In this example, the BubbleSortIterator class provides an interface for iterating over the collection of integers that will be sorted using the Bubble Sort algorithm. The BubbleSort class implements the Bubble Sort algorithm, and takes an iterator as an argument to sort the collection. Finally, we create an instance of the iterator and pass it to the BubbleSort class to sort the collection. The sorted collection is then printed using the built-in list() function.

By using the Iterator pattern, we are able to provide a way to iterate over the collection without exposing the internal implementation of the sorting algorithm, which makes the code more modular and easier to maintain.

<h2>Selection sort using Strategy pattern</h2>
The Strategy pattern is used to define a family of algorithms, encapsulate each one, and make them interchangeable. It allows the client to select an algorithm at runtime without modifying the client code. In the case of Selection Sort, we can use the Strategy pattern to encapsulate the different ways of selecting the minimum element during the sort.

In this example, the SelectionSort class implements the Selection Sort algorithm, and takes a SelectionStrategy object as an argument to determine how to select the minimum element during the sort. The SelectionStrategy class is an abstract class that defines the interface for the different selection strategies. The MinElementSelection and MaxElementSelection classes implement the SelectionStrategy interface and provide different ways of selecting the minimum element during the sort.

We create an instance of the SelectionSort class and pass in a SelectionStrategy object to determine the selection strategy. We then call the sort() method on the SelectionSort object to sort the collection using the selected strategy.

By using the Strategy pattern, we can encapsulate the different selection strategies and make them interchangeable. This allows the client to select the selection strategy at runtime without modifying the client code, making the code more modular and easier to maintain.

<h2>Insertion sort using Template Method pattern</h2>
The Template Method pattern is used to define the skeleton of an algorithm in a base class, but delegate some steps to subclasses. It allows the subclasses to redefine certain steps of the algorithm without changing its structure. In the case of Insertion Sort, we can use the Template Method pattern to define the overall structure of the sort algorithm in a base class, but delegate the specific comparisons to subclasses.

In this example, the InsertionSort class defines the overall structure of the Insertion Sort algorithm. The sort() method iterates through the collection and calls the insert() method to insert each element in its correct position in the sorted subarray. The insert() method uses the compare() method to determine the order of the elements.

The AscendingInsertionSort and DescendingInsertionSort classes are subclasses of InsertionSort, and they implement the compare() method to define the specific comparison for the sort algorithm.

We create an instance of the AscendingInsertionSort and DescendingInsertionSort classes and call the sort() method to sort the collection in ascending or descending order.

By using the Template Method pattern, we can define the overall structure of the algorithm in a base class, but allow subclasses to redefine specific steps of the algorithm. This makes the code more modular and easier to maintain, and allows for greater flexibility in the implementation of the algorithm.

<h2>Merge sort using Divide & Conquer pattern</h2>
The Divide and Conquer pattern is a problem-solving approach that breaks down a problem into smaller sub-problems, solves each sub-problem independently, and then combines the solutions to obtain the final solution. Merge Sort is a classic example of an algorithm that uses the Divide and Conquer pattern.

In this example, the merge_sort() function is the main function that implements the Merge Sort algorithm. The function first checks if the collection has only one element or is empty, in which case it returns the collection as is. If the collection has more than one element, the function splits it into two halves and recursively calls merge_sort() on each half. The two sorted halves are then merged using the merge() function.

The merge() function takes two sorted lists as input and returns a single sorted list. The function iterates through the two lists and compares the elements at each index. The smaller element is appended to a new list, and the index of the corresponding list is incremented. After one list is fully iterated, the remaining elements of the other list are appended to the new list.

By breaking the problem down into smaller sub-problems and solving each sub-problem independently, we can achieve a more efficient solution to the Merge Sort problem. This algorithm has a time complexity of O(n log n), which is faster than many other sorting algorithms, such as Bubble Sort or Insertion Sort.

<h2>Quick sort using Strategy pattern</h2>
The Strategy Pattern is a design pattern that defines a family of interchangeable algorithms and encapsulates each algorithm in a separate class. The Quick Sort algorithm is a good candidate for the Strategy Pattern, as it allows us to interchange the partitioning strategy used in the algorithm.

In this example, the QuickSort class is the main class that implements the Quick Sort algorithm. The class takes a partitioning strategy as a parameter in its constructor. The sort() method of the class first checks if the collection has only one element or is empty, in which case it returns the collection as is. If the collection has more than one element, the function selects a pivot element using the partitioning strategy and partitions the collection into two halves. The two halves are then recursively sorted using the sort() method and merged together.

The first_element_partition() and middle_element_partition() functions are examples of partitioning strategies. The first_element_partition() strategy selects the first element of the collection as the pivot, while the middle_element_partition() strategy selects the middle element of the collection as the pivot.

By encapsulating the partitioning strategy in a separate class, we can easily interchange the strategy used in the Quick Sort algorithm without changing the overall structure of the algorithm. This makes the code more modular and easier to maintain, and allows for greater flexibility in the implementation of the algorithm.
