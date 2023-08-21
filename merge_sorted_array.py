"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
"""

class Solution(object):
    def merge(self, nums1, m: int, nums2: int, n: int):
        # merge nums1 and num2
        while True:
            if len(nums1) > m: # how to get nums1 list to length of m?
                nums1.pop()
            elif len(nums1) == m:
                for i in range(n):
                    nums1.append(nums2[i]) 
                nums1.sort()
                print(nums1)
                break

"""
Remember the acronym UPS check

Step One (Understand). We have to understand the problem.
1. What is the unknown? merged sorted array in non-decreasing order (sorted in-place inside the array)
2. What are the data inputs? two integer arrays nums1 and nums2 sorted in non-decreasing order and 2 integers m and n representing the number of elements in nums1 and nums2 respectively
3. Can you restate the problem in your own words? add num2 into num1
4. Can the unknown be determined from the data inputs? yes
5. Is the data inputs sufficient to determine the unknown? yes Insufficient? Redundant? Contradictory? 
6. How should I label important pieces of data input that are a part of the problem? constraints nums1.length == m + n and nums2.length == n
7. Draw a figure. Introduce suitable notation.

Step Two (Plan). Come up with concrete examples to help you understand the problem better. Find a connection between the data inputs and the unknown. You may be obliged to consider auxiliary problems if an immediate connection cannot be found. 
8.  Have you seen it before? Or have you seen the same problem in a slightly different form? Do you know a related problem? use append 
9.   Do you know a coding strategy that could be useful? Look at the unknown! And try to think of a familiar problem having the same or a similar unknown. Here is a problem related to yours and solve before. Could you use it? Could you use its result? Could you use its method? 
10. Start with a simple example. Could you restate the problem? Could you restate it still differently? 
11. What about examples with empty inputs? Any other edge case examples? What examples with invalid inputs? 
12. Progress to more complex examples. What is your updated plan here to find a solution?
13. If you still cannot solve the proposed problem, try to solve first some related problem. Could you imagine a more accessible related problem? A more general problem? A more special problem? An analogous problem? Could you solve a part of the problem? Keep only a part of the data inputs, drop the other part; how far is the unknown then determined, how can it vary? Could you derive something useful from the data? Could you think of other data appropriate to determine the unknown? Could you change the unknown or the data, or both if necessary, so that the new unknown and the new data are nearer to each other? Did you use all the data? Did you use the whole of the data inputs? Have you taken into account all essential notions involved in the problem?


Step Three (Solve). Carry out your plan of the solution and check each one of your steps in pseudocode.
14.  Can you see clearly that the step is correct?


IV. 	Step Four (Check). Examine the solution obtained and refactor. 
15.  Can you check your result? 
16.  Can you check the argument? 
17.  Can you derive the result differently? 
18.  Can you see it at a glance? 
19.  Can you make the code DRYer and refactor? 
20.  Can you improve the performance? 
21.   How have other people solved this problem?
"""
a = Solution()
a.merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3)

"""
Example 1:
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].
Example 3:

Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.
 

Constraints:

nums1.length == m + n
nums2.length == n
0 <= m, n <= 200
1 <= m + n <= 200
-109 <= nums1[i], nums2[j] <= 109
"""