class Solution:
    def removeDuplicates(self, nums):
        pass


"""

Remember the acronym UPS check

Step One (Understand). We have to understand the problem.
1. What is the unknown?
2. What are the data inputs?
3. Can you restate the problem in your own words?
4. Can the unknown be determined from the data inputs?
5. Is the data inputs sufficient to determine the unknown? Insufficient? Redundant? Contradictory? 
6. How should I label important pieces of data input that are a part of the problem?
7. Draw a figure. Introduce suitable notation.

Step Two (Plan). Come up with concrete examples to help you understand the problem better. Find a connection between the data inputs and the unknown. You may be obliged to consider auxiliary problems if an immediate connection cannot be found. 
8.  Have you seen it before? Or have you seen the same problem in a slightly different form? Do you know a related problem? 
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



Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.
Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.

 

Example 1:
"""

a = Solution()
a.removeDuplicates([1,1,2])

"""
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
Example 2:

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
 

Constraints:

1 <= nums.length <= 3 * 104
-100 <= nums[i] <= 100
nums is sorted in non-decreasing order.
"""