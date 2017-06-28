# Interview_Training
Answering various code challenges and interview questions

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
