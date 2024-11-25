def sum_of_squares(nums):
    total = 0
    for i in range(len(nums)):
        distinct = set()
        for j in range(i, len(nums)):
            distinct.add(nums[j])
            total += len(distinct) ** 2
    return total

nums = [1, 2, 1]
print(sum_of_squares(nums))  
