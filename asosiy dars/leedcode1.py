def removeDuplicates(nums):
    if not nums:
        return 0
    
    k = 0  # Pointer for storing unique elements
    
    for i in range(1, len(nums)):
        if nums[i] != nums[k]:
            k += 1
            nums[k] = nums[i]
    
    return k + 1  # Number of unique elements

# Test the implementation
nums1 = [1, 1, 2]
expectedNums1 = [1, 2]
k1 = removeDuplicates(nums1)
print(f"Output: {k1}, nums: {nums1[:k1]}")  # Expected output: 2, nums: [1, 2]

nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
expectedNums2 = [0, 1, 2, 3, 4]
k2 = removeDuplicates(nums2)
print(f"Output: {k2}, nums: {nums2[:k2]}")  # Expected output: 5, nums: [0, 1, 2, 3, 4]
