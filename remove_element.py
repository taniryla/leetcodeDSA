class Solution:
    def removeElement(self, nums, val):
        while True:
            if nums.count(val) != 0:
                nums.remove(val)
            else:
                break
        k = len(nums)
        print(k, nums)
        return k

"""
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k.
Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int val = ...; // Value to remove
int[] expectedNums = [...]; // The expected answer with correct length.
                            // It is sorted with no values equaling val.

int k = removeElement(nums, val); // Calls your implementation

assert k == expectedNums.length;
sort(nums, 0, k); // Sort the first k elements of nums
for (int i = 0; i < actualLength; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.

"""
a = Solution()
a.removeElement(nums = [3,2,2,3], val = 3)

"""
Example 1:

Input: 
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).
Example 2:

Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
Note that the five elements can be returned in any order.
It does not matter what you leave beyond the returned k (hence they are underscores).
 

Constraints:

0 <= nums.length <= 100
0 <= nums[i] <= 50
0 <= val <= 100
"""

"""
Remember the acronym UPS check

Step One (Understand). We have to understand the problem.
1. What is the unknown? remove all occurrences of val in nums in-place and return the number of elements "k" left in nums
2. What are the data inputs? integer list nums and integer val
3. Can you restate the problem in your own words? find all val and remove it from nums
4. Can the unknown be determined from the data inputs? yes
5. Is the data inputs sufficient to determine the unknown? Insufficient? Redundant? Contradictory? yes
6. How should I label important pieces of data input that are a part of the problem? nums, val, k
7. Draw a figure. Introduce suitable notation.
s
Step Two (Plan). Come up with concrete examples to help you understand the problem better. Find a connection between the data inputs and the unknown. You may be obliged to consider auxiliary problems if an immediate connection cannot be found. 
8.  Have you seen it before? Or have you seen the same problem in a slightly different form? Do you know a related problem? 
9.   Do you know a coding strategy that could be useful? for in loop Look at the unknown! And try to think of a familiar problem having the same or a similar unknown. Here is a problem related to yours and solve before. Could you use it? Could you use its result? Could you use its method? 
10. Start with a simple example. Could you restate the problem? Could you restate it still differently? 
11. What about examples with empty inputs? Any other edge case examples? What examples with invalid inputs? negative val
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
