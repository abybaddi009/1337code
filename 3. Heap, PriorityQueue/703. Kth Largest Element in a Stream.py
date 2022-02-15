from typing import List

# My first assumption was to insert the new element, heapify it down in a MaxHeap and return self.array[self.k]
# The above assumption is incorrect since while some of the x largest might be in the correct place, usually the Heap is not sorted by default

# The approach taken here is to implement a min-heap with three elements so that the kth element will be at the root
# For newer items we will discard them if they are smaller that our root
# else we will replace our root and heapify it downwards

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.array = []
        for n in nums:
            self.add(n)

    def add(self, val: int) -> int:
        if len(self.array) >= self.k:
            if val > self.array[0]:
                self.array[0] = val
                self.heapifyDown()
        else:
            self.array.append(val)
            self.heapifyUp()
        return self.array[0]

    def pop(self):
        item = self.array[0]
        self.array[0] = self.array[-1]
        self.array = self.array[:-1]
        self.heapifyDown()
        return item

    def getParentIndex(self, index):
        return (index - 1) // 2

    def getLeftChildIndex(self, index):
        return (2 * index) + 1

    def getRightChildIndex(self, index):
        return (2 * index) + 2

    def hasParent(self, index):
        return self.getParentIndex(index) >= 0
    
    def hasLeftChild(self, index):
        return self.getLeftChildIndex(index) < len(self.array)

    def hasRightChild(self, index):
        return self.getRightChildIndex(index) < len(self.array)

    def heapifyUp(self):
        index = len(self.array) - 1
        while self.hasParent(index) and self.array[self.getParentIndex(index)] > self.array[index]:
            self.array[self.getParentIndex(index)], self.array[index] =  self.array[index], self.array[self.getParentIndex(index)]
            index = self.getParentIndex(index)

    def heapifyDown(self):
        index = 0
        while self.hasLeftChild(index):
            childIndex = self.getLeftChildIndex(index)
            if self.hasRightChild(index) and self.array[childIndex] > self.array[self.getRightChildIndex(index)]:
                childIndex = self.getRightChildIndex(index)
            if self.array[index] > self.array[childIndex]:
                self.array[childIndex], self.array[index] = self.array[index], self.array[childIndex]
            else:
                break
            index = childIndex

    def __str__(self):
        return str(self.array)
    
    def __repr__(self):
        return str(self.array)


if __name__ == '__main__':
    kthLargest = KthLargest(3, [4, 5, 8, 2])
    assert kthLargest.add(3) == 4
    assert kthLargest.add(5) == 5
    assert kthLargest.add(10) == 5
    assert kthLargest.add(9) == 8
    assert kthLargest.add(4) == 8