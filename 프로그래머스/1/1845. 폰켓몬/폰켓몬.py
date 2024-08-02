
def solution(nums):
    temp = len(nums)//2
    nums = list(set(nums))
    return min(temp, len(nums))