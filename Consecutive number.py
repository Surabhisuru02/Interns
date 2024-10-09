def group_con_num(num):
    if not num:
        return []
   
    # Sort the numbers to handle them in ascending order
    sort_num = sorted(num)
   
    # Initialize the result list to hold the grouped consecutive numbers
    result = []
   
    # Start the first group with the first number in the sorted list
    gr = [sort_num[0]]
   
    # Iterate through the sorted numbers starting from the second element
    for i in range(1, len(sort_num)):
        if sort_num[i] == sort_num[i - 1] or sort_num[i] == sort_num[i - 1] + 1: # Check if the current number is consecutive to the previous number or if it's a duplicate of the previous number
            gr.append(sort_num[i])
        else:
            result.append(gr)  # If not consecutive or duplicate, add the current group to the result
            gr = [sort_num[i]] #start a new group
   
    # Append the last group to the result
    result.append(gr)
    return result