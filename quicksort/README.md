# Quicksort

Quicksort is an in-place sorting algorithm. It runs, in average cases at O(n logn) time and worst case O(n**2). It uses O(1) space because it sorts in-place and does not create any auxiliary data structures. 

## In English

Quicksort takes an array as input, along with values marking which segment of the array will be operated upon. We often talk about the array as being filled with ints, but any values that can be compared using `>`, `<` and `=` will work. 

The algorithm works in a divide-and-conquer fashion, recursively sorting smaller and smaller segments of itself until it is sorted fully in ascending order. 

At each step, Quicksort takes the entire array and two indices representing a `start` and an `end` of the segment to examine. It is initialized with values that represent the entire array (`0`...`len(arr)-1`).

It then passes those references to a `partition` function. The job of the `partition` function is to roughly sort the values in the array around a `pivot` value, such that all the values less than the pivot are on its left, and all the values greater than the pivot are on its right.  The `partition` function then returns the index of the `pivot` value, which is used to further divide the array.

`partition` is implemented by assigning a `pivot` value that is chosen randomly, however, in many implementations it is simply the last value in the given segment.  It then also chooses what I've called a `divider`, and is also referred to as a `pivotIndex`, or a `divider`.  This value is initialized as the first index in the segment of the array we are operating on.  

As we walk through the segment, for each value we check whether it is less than the value of the pivot. If it is, we move it to the left of the `divider`, and increment the index of the `divider` by 1. 

Once we have completed iterating over the array, we swap the values at the `pivot` and `divider` respectively, and return the `divider` index (which now points to the value we used as our pivot). At this point, the array has a pivot which separates values less than it from values greater than it. 

Our `quicksort` function then subdivides the array around the pivot index (getting the list of items smaller than the pivot and the list of items greater than the pivot) and recursively sorting them in the same fashion, until there are no more elements to sort. 

