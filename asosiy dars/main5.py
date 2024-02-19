class Solution:
    def twoSum(self, nums, target):
        # Butun sonlar massivi nums va butun son berilgan target
        hash_map = {}  # Hash map yaratamiz
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hash_map:  # Agar to'g'ri biror raqam topilsa
                return [hash_map[complement], i]  # Indeksleri qaytarish
            hash_map[num] = i  # Hash mapga raqamlarni va indekslarni qo'shamiz

# Testlar
solution = Solution()
print(solution.twoSum([2, 7, 11, 15], 9))  # Chiqish bo'lishi kerak: [0, 1]
print(solution.twoSum([3, 2, 4], 6))      # Chiqish bo'lishi kerak: [1, 2]
print(solution.twoSum([3, 3], 6))          # Chiqish bo'lishi kerak: [0, 1]
