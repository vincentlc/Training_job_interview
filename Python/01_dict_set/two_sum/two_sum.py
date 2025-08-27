
def two_sum(nums: list[int], target:int) -> list[int]:
    """
    Given an array of integers `nums` and an integer `target`, return the indices of the two numbers
    that add up to `target`. Each input has exactly one solution, and you may not use the same element twice.

    Args:
        nums: List of integers.
        target: Target sum.

    Returns:
        List of two indices whose values add up to `target`. Returns an empty list if no solution exists.
    """
    dict_value = {}
    for index,value  in enumerate(nums):
        complement = target - value
        print(dict_value, complement, value)
        if complement in dict_value:
            return [dict_value[complement], index]
        dict_value[value]=index
    return []

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """Class-based solution for the Two Sum problem."""
        return two_sum(nums, target)

if __name__ == "__main__":
    # Example usage
    solution = Solution()
    print(solution.twoSum([2, 7, 11, 15], 9))  # Output: [0, 1]
    print(solution.twoSum([3, 2, 4], 6))      # Output: [1, 2]
    print(solution.twoSum([3, 3], 6))         # Output: [0, 1]