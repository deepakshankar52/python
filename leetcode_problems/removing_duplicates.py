# Remove duplicates from sorted array

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 1
        for i in range(1,len(nums)):
            if(nums[i] != nums[i-1]):
                nums[j] = nums[i]
                j += 1
        return j
    


'''

input: [1,1,2]
output: 2 (after removing duplicates, total elements of [1,2])

input: [0,0,1,1,1,2,2,3,3,4]
output: 4 ([0,1,2,3,4])

'''