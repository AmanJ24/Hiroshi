# class Solution:
#     def twoSum(self, nums, target):
#         hashmap = {}
#         for i in range(len(nums)):
#             complement = target - nums[i]
#             if complement in hashmap:
#                 return [i, hashmap[complement]]
#             hashmap[nums[i]] = i

# ans = Solution()
# target = 6
# nums = [3, 2, 2, 5, 11, 10, 6, 9, 4]
# print(ans.twoSum(nums, target))


def remove_elem(nums, val):
    change = 0
    while val in nums:
        nums.remove(val)
        change += 1
    return change

val = 2
nums = [0,1,2,2,3,0,4,2]
print(remove_elem(nums, val))
print(nums)