"""
26. Remove Duplicates from Sorted Array

Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that
each unique element appears only once. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result
placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates,
then the first k elements of nums should hold the final result.
It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array.
You must do this by modifying the input array in-place with O(1) extra memory.

Note:
Since our first element is already present at index 0 (it is a unique element),
we quickly run a for loop for the entire array to scan for unique elements.

If the current element and the next element are the same,
then we just keep on going till we find a different

Once we find a different element, it is inserted at index 1, because, index 0 is taken by the first unique element.

Once this is done, the same scanning is done to find out the next unique element
and this element is to be inserted at index 2. This process continues until we are done with unique elements.

We use a variable (ind = 1) which is incremented to the next index whenever we find a unique element
and we insert this element at its corresponding index.
"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ind = 1
        for i in range(len(nums)-1):
            if nums[i+1] != nums[i]:
                nums[ind] = nums[i+1]
                ind += 1
        print(nums)
        return ind
