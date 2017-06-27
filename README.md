# Interview_Training
Answering various code challenges and interview questions


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

-  Create new Element for linked List
-  Append Element to end of linked List
-  find position of given Element in linked List
-  Insert item at custom position in linked List
-  Delete Element from linked List

## Laundry_Day.py:

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
