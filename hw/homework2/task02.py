"""
Given an array of size n, find the most common and the least common elements.
The most common element is the element that appears more than n // 2 times.
The least common element is the element that appears fewer than other.

You may assume that the array is non-empty and the most common element
always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3, 2

Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2, 1

"""
from collections import Counter
from typing import List, Tuple


def get_major_and_minor_list_elements(inp: List) -> Tuple[int, int]:
    c = Counter(inp)
    # most_common returns list, which is sorted based on count of the elements
    most_frequent = c.most_common()[0][0]
    less_frequent = c.most_common()[-1][0]

    return most_frequent, less_frequent