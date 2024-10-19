# Binary Heap-based Priority Queue implementation
import math

class MaxHeap:

    def __init__(self):
        self.heap = None
        self.pivot = None

    # Swaps the elements of the heap, takes indeces as input
    def swap(self, a, b):
        tmp = self.heap[a]
        self.heap[a] = self.heap[b]
        self.heap[b] = tmp

    # Transforms a given array into an XHeap
    def heapify(self, arr):
        self.heap = arr
        self.pivot = math.floor((len(self.heap) / 2))
        for i in range(self.pivot):
            max = 0
            if self.heap[i] < self.heap[i + 1]:
                max = i + 1
            if self.heap[max] < self.heap[i + 2]:
                max = i + 2
            if self.heap[i] != self.heap[max]:
                self.swap(i, max)

    def extractMax(self):
        max = self.heap[0]

# Wrong implementation !

