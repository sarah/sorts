import unittest

def quicksort(A):
    """
    API function that calls internal function _quicksort with initial args
    """
    _quicksort(A,0,len(A)-1)


def _quicksort(A, start, last):
    """
    :A array
    :start Int
    :last Int
    """
    if (last - start) > 0:
        pIndex = partition(A,start,last)

        _quicksort(A,start, pIndex-1)    # segment to the left of the pivot
        _quicksort(A,pIndex+1, last)     # segment to the right of the pivot 

def partition(A, start, last):
    """
    :A array
    :start Int
    :last Int
    """
    pivot = last
    divider = start

    for i in range(start, last):
        if(A[i] <= A[pivot]):
            # swap, move the smaller value to the left of the 'divider' and move the divider
            A[i], A[divider] = A[divider], A[i]
            divider += 1

    # put the value of the pivot in the divider position, completing the partition.
    A[divider], A[pivot] = A[pivot], A[divider]

    return divider


class QuickSortTest(unittest.TestCase):
    def testSorts(self):
        A = [5,4,10,9,8,7,15,1,2]
        quicksort(A)
        expected = [1,2,4,5,7,8,9,10,15]
        self.assertEqual(A, expected)

    def testSortsAlreadySortedList(self):
        A = [1,2,4,5,7,8,9,10,15]
        quicksort(A)
        expected = [1,2,4,5,7,8,9,10,15]
        self.assertEqual(A, expected)


if __name__== "__main__":
    unittest.main()
