# Code Training
Answering various code challenges and interview questions

## Kangaroo.py

https://www.hackerrank.com/challenges/kangaroo/problem

Tere are two kangaroos on a number line ready to jump in the positive direction (i.e, toward positive infinity). The first kangaroo starts at location x1 and moves at a rate of v1 meters per jump. The second kangaroo starts at location x2 and moves at a rate of v2 meters per jump. Given the starting locations and movement rates for each kangaroo, can you determine if they'll ever land at the same location at the same time?  


## grade_rounding.py

https://www.hackerrank.com/challenges/grading  

## utopian_tree.py

https://www.hackerrank.com/challenges/utopian-tree/problem  
The Utopian Tree goes through 2 cycles of growth every year. Each spring, it doubles in height. Each summer, its height increases by 1 meter.  

Laura plants a Utopian Tree sapling with a height of 1 meter at the onset of spring. How tall will her tree be after N growth cycles?  
The first line contains an integer T, the number of test cases. 
T subsequent lines each contain an integer N, denoting the number of cycles for that test case.  



## movie_date_from_hell.py
https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem
Logan wants to go to the movies with Lily on some day X satisfying i<=X<=j, but he knows she only goes to the movies on days she considers to be beautiful. Lily considers a day to be beautiful if the absolute value of the difference between X and reversed(X) is evenly divisible by k.  

Given i, j, and k (in one line seperated by " "), count and print the number of beautiful days when Logan and Lily can go to the movies.  

## moving_average.py
Given an input array of numbers, calculate the moving average of 3 indexes at a time.  
The length of the array is a multiple of 3.  
### Example:
[1,2,3,4,5,6]--->[2 3 4 5]  
[1,4,6,12,3,17]-->[3.67 7.33 7.00 10.67]  

## merge_arrays.py
https://leetcode.com/problems/merge-sorted-array/#/description  
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.  
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2. The number of elements initialized in nums1 and nums2 are m and n respectively.  
### Note:
The test case lists had trailing 0s which were not counted as part of the list itself. Therefore, the first step of decreasing the lists sizes until it matched with m,n respectivily was neccesary. 

## max_subarray.py:
https://leetcode.com/problems/maximum-subarray/#/description  
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.  
For example, given the array [-2,1,-3,4,-1,2,1,-5,4]    
the contiguous subarray [4,-1,2,1] has the largest sum = 6  

## Add_one.py:
https://leetcode.com/problems/plus-one/#/description  
Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.  
You may assume the integer do not contain any leading zero, except the number 0 itself.  
The digits are stored such that the most significant digit is at the head of the list.  

## List_Cycle.py:
https://leetcode.com/problems/linked-list-cycle/#/description  
Given a linked list, determine if it has a cycle in it.  

## LinkedLists_duplicates.py
https://leetcode.com/problems/remove-duplicates-from-sorted-list/#/description  
Given a sorted linked list, delete all duplicates such that each element appear only once.  

### For example:
Given 1->1->2, return 1->2.  
Given 1->1->2->3->3, return 1->2->3.  

## merged_meetings.py
https://www.interviewcake.com/question/python/merging-ranges  
Slightly varried input of Lists within Lists

## contains_duplicate.py
https://leetcode.com/problems/contains-duplicate/#/description  
Given an array of integers, find if the array contains any duplicates. Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.  

## two_sums_2.py
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/#/description  
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.  
The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.  
You may assume that each input would have exactly one solution and you may not use the same element twice.  

Input: numbers={2, 7, 11, 15}, target=9  
Output: [1,2]  

## find_single.py
https://leetcode.com/problems/single-number/#/description  
Given an array of integers, every element appears twice except for one. Find that single one.  

## Remove_duplicates.py
https://leetcode.com/problems/remove-duplicates-from-sorted-array/#/description  
Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.  
Do not allocate extra space for another array, you must do this in place with constant memory.  
### For example:
Given input array nums = [1,1,2],  
Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the new length.  

## Stock_Sell.py
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/#/description  
Say you have an array for which the ith element is the price of a given stock on day i.  
If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.  

### Example 1:
Input: [7, 1, 5, 3, 6, 4]  
Output: 5  
max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)  

### Example 2:
Input: [7, 6, 4, 3, 1]  
Output: 0  
In this case, no transaction is done, i.e. max profit = 0.  

## Last_Word.py
https://leetcode.com/problems/length-of-last-word/#/description  
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.  
If the last word does not exist, return 0.  
Note: A word is defined as a character sequence consists of non-space characters only.  

### For example: 
Given s = "Hello World" --> return 5.  

## Needle_haystack.py
https://leetcode.com/problems/implement-strstr/#/description  
Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.  

## Search_Insert_Position.py
https://leetcode.com/problems/search-insert-position/#/description  
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.  
You may assume no duplicates in the array.  

### Here are few examples.  
[1,3,5,6], 5 → 2  
[1,3,5,6], 2 → 1  
[1,3,5,6], 7 → 4  
[1,3,5,6], 0 → 0  

## Balanced_Brackets.py
https://leetcode.com/problems/valid-parentheses/#/description  
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.  
The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.  

## Common_Prefix.py
https://leetcode.com/problems/longest-common-prefix/#/description  
Write a function to find the longest common prefix string amongst an array of strings.  
### Note:  
I adapted the question somewhat from the original question:  
+ ["DOG","dog"] --> recognised as same letters prefix result: "dog"
+ check for random " " in front of or trailing strings and delete


## Convert_Roman_Numerals.py
https://leetcode.com/problems/roman-to-integer/#/description  
Given a roman numeral, convert it to an integer.  
Input is guaranteed to be within the range from 1 to 3999.  

## Two_Sums.py
https://leetcode.com/problems/two-sum/#/description

Given an array of integers, return indices of the two numbers such that they add up to a specific target.  
You may assume that each input would have exactly one solution, and you may not use the same element twice.  

### Example:
Given nums = [2, 7, 11, 15], target = 9 --> return [0, 1]

## mirroredArray.py:

Given an array as input, find out if an array has an index that satisfies the following requirement:  
sum of numbers left of index equals sum of numbers right of index.  
If such an index exists, print index number(index starts as 1, not 0). Otherwise print -1.  

### For example:

Array[0,5,3,5]-->Returns 3, as 0+5=5  
Array[0,5]-->Returns 2, as 0=0  
Array[1,2,4]-->Returns -1  
Array[3]-->Returns -1  

## linked_list.py:

Create a linked List in Python via Class Objects.  
Program should be able to:  

+ Create new Element for linked List
+ Append Element to end of linked List
+ find position of given Element in linked List
+ Insert item at custom position in linked List
+ Delete Element from linked List

## Laundry_Day.py:
https://codecon.bloomberg.com/contest/5948031613881024512/33

### Input Specifications

Each article of clothing will have its own separate line. You have a penchant for hoarding, so there is no guarantee as to the number of pieces, but you can assure yourself that each article can be easily categorized by description (name).  
Articles of clothing will be fed in as line-delimited list. See below for examples.  

### Output Specifications

Output should be an alphabetically (case-insensitive) sorted, line-delimited list of the articles of clothing along with their count. Each field (count, category) should be separated by a pipe (|). If you come across a sock without a soulmate, the count should be designated by a 0 (zero). Socks that are in pairs should be on separate lines from the socks of the same category without pairs, and should come before the pairless sock. See below for examples.

Sample Input/Output

### INPUT
white shirt    
polka dot sock    
red sock  
superhero shirt  
torn jeans  
polka dot sock  
white shirt  
polka dot sock  


### OUTPUT
1|polka dot sock  
0|polka dot sock    
0|red sock  
1|superhero shirt  
1|torn jeans  
2|white shirt  


## Pending:
https://leetcode.com/problems/count-and-say/#/description  

