nums = [1, 2, 3, 4, 5]

# Python has only dynamic arrays, which are called lists.
# Look-up/Accsess- O(1)
# Push/Pop - O(1)* # could be O(n) if the array needs to be resized
# Insert - O(n)
# Delete - O(n)


# Look-up - O(1) - Constant Time
print(nums[2])

# Push - O(1) - Constant Time
nums.append(6)

# Pop - O(1) - Constant Time
nums.pop()

# Insert - O(n) - Linear Time
nums.insert(2, 99)

# Remove - O(n) - Linear Time
nums.remove(99)  # remove the first occurrence of 99

# Del - O(n) - Linear Time
del nums[2:4]  # delete elements from index 2 to 3 (4 is exclusive)
