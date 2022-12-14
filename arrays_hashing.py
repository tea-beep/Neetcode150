import math


##test cases



##functions
def isAnagram(s, t):
    #one line solution, just check if the two sorted
    #arrays are equal.
    # return sorted(s) == sorted(t)


    #for two strings to be anagrams, they have to contain all of the same 
    #letters.
    if len(s) != len(t):
        return False
    
    hashmapS = {}
    hashmapT = {}

    for i in range (len(s)):
        #add the elements to the hashmaps.
        hashmapS[s[i]] = 1 + hashmapS.get(s[i], 0)
        hashmapT[t[i]] = 1 + hashmapT.get(t[i], 0)
    #check if they're equal! 
    return hashmapS == hashmapT

def containsDuplicate(nums):
    # for i in range (len(nums)):
    #     for j in range(i +1, len(nums)):
    #         if nums[i] == nums[j]:
    #             return True
    # return False

    # need to check if number is in nums, 
    #can iterate through nums adding to a set and check to see
    #if they're already in a set.

    hashset = set()

    for i in range(len(nums)):
        if nums[i] in hashset:
            return True
        else:
            hashset.add(nums[i])
    return False

    #can also just convert nums to a set and compare the length
    #since sets don't allow duplicates.

    # return len(set(nums)) != len(nums)


def twoSum(nums, target):
    #int array, int target, return indices of two numbers
    #that add to target.

    #brute force

    #double for loop.

    #problem with this solution is it's o(n^2)

    # for i in range(len(nums)):
    #     for j in range(i+1, len(nums)):
    #         if nums[i] + nums[j] == target:
    #             return [i,j]

    # return -1

    #use a hashmap for instant retrieval of data?
    #we don't need to check every number.. just looking for specific numbers.
    #diff = target - i, if diff in map, return i, diff?

    #needs to use the enumerate function

    hashMap = {}

    for i, n in enumerate(nums):
        diff = target - n
        if diff in hashMap:
            return [hashMap[diff],i]
        hashMap[n] = i
    return None




##print statements