import pytest 
from two_sum import two_sum, Solution

@pytest.mark.parametrize(
    "nums, target, expected",
    [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
        ([3, 4], 6, []),  # No solution
        ([], 6, []),      # Empty input
        ([-1, -2, -3, -4], -5, [1, 2]),  # Negative numbers
        ([0, 4, 3, 0], 0, [0, 3]),       # Zeroes
        ([1, 2, 3, 4, 5], 100, []),      # No solution
    ],
)
def test_two_sum(nums: list[int], target: int, expected: list[int]):
    assert two_sum(nums, target) == expected

def test_solution_class():
    solution = Solution()
    assert solution.twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert solution.twoSum([3, 2, 4], 6) == [1, 2]
    assert solution.twoSum([3, 3], 6) == [0, 1]
    assert solution.twoSum([3, 4], 6) == []