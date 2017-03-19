#!/usr/local/bin/python
# coding: latin-1
# https://leetcode.com/problems/search-insert-position
#
# Given a sorted array and a target value, return the index if
# the target is found. If not, return the index where it would
# be if it were inserted in order.
#
# You may assume no duplicates in the array.
# 
# Here are few examples.
# [1,3,5,6], 5 → 2
# [1,3,5,6], 2 → 1
# [1,3,5,6], 7 → 4
# [1,3,5,6], 0 → 0 

def searchInsert(nums, target):
    for i, num in enumerate(nums):
        if num == target:
            return i
        elif num > target:
            return i
    return len(nums)

def tests():
    print(searchInsert([1,3,5,6], 5) == 2)
    print(searchInsert([1,3,5,6], 2) == 1)
    print(searchInsert([1,3,5,6], 7) == 4)
    print(searchInsert([1,3,5,6], 0) == 0)
    print(searchInsert([], 0) == 0)
    print(searchInsert([1], 0) == 0)
    print(searchInsert([1], 2) == 1)

tests()
