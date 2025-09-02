import pytest 
from intersection_two_array import intersect, Solution
@pytest.mark.parametrize(
    "nums1, nums2, expected",
    [
        ([1,2,2,1], [2,2], [2,2]),
        ([4,9,5], [9,4,9,8,4], [4,9]),
        ([1,3,5,6,8,9], [], []),
        ([],[1,3,5,6,8,9], []),
        ([],[], []),
        ([3, 1, 3, 1], [1, 1, 3, 3], [1, 1, 3, 3]),
        ([1], [1], [1]),
        ([1, 2, 3], [4, 5, 6], []),
    ],
) 
def test_intersect_function(nums1: list[int], nums2: list[int], expected: list[int]):
    """
    Test the `intersect` function with various inputs, including edge cases.
    Uses sorted() to compare lists regardless of order.
    """
    assert sorted(intersect(nums1, nums2)) == sorted(expected)

def test_solution_class_intersect():
    """
    Test the `Solution.intersect` method with various inputs.
    Uses sorted() to compare lists regardless of order.
    """ 
    solution = Solution()
    assert sorted(solution.intersect([1,2,2,1], [2,2])) == sorted([2,2])
    assert sorted(solution.intersect([4,9,5], [9,4,9,8,4])) == sorted([4,9])
    assert sorted(solution.intersect([1,3,5,6,8,9], [])) == sorted([])
    assert sorted(solution.intersect([], [1,3,5,6,8,9])) == sorted([])

def test_intersect_function_negative_input():
    """
    Test that the function raises ValueError for negative inputs.
    """
    with pytest.raises(ValueError):
        intersect([-1, 2, 3], [1, 2, 3]) 