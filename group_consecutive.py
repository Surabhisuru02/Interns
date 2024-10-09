def group_consecutive_numbers(nums):
    nums.sort()
    result = []
    current_group = [nums[0]]
    
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1] + 1:
            # Continue the current group
            current_group.append(nums[i])
        elif nums[i] == nums[i - 1]:
            current_group.append(nums[i])
        else:
            # End of the current group
            result.append(current_group)
            # Start a new group
            current_group = [nums[i]]
    
    # Add the last group
    result.append(current_group)
    return result
nums = [4,1,5,2,6,61,6,6]
print(group_consecutive_numbers(nums))
