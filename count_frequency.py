# from collections import Counter  # which is used for counting hashable objects(Integers,Floats,Strings,tuple)
#
# def count_frequency(elements):
#     frequency = Counter(elements) # Creates a Counter object that counts the occurrences of each element in the list
#     return frequency
#
# # Example usage
# elements = [1, 2, 2, 3, 3, 3, 4]
# print(count_frequency(elements))

def count_frequency(elements):
    frequency = {}  # Initialize an empty dictionary to store frequencies
    for element in elements:  # Iterate over each element in the list
        if element in frequency:  # If the element is already in the dictionary
            frequency[element] += 1  # Increment its count
        else:
            frequency[element] = 1  # Initialize its count to 1
    return frequency

# Example usage
elements = [1, 2, 2, 3, 3, 3, 4]
print(count_frequency(elements))


hello thanu 
bye
