import pytest 
from contain_duplicate import contain_duplicate

@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1,2,3,1], True),
        ([1,2,3,4], False),
        ([1,1,1,3,3,4,3,2,4,2], True),
        ([], False),
        ([-1,-1,-1,-3,-3,4,-3,2,4,2], True),
        ([1], False),
        ([2, 2, 2, 2], True),
    ],
)
def test_contain_duplicate(nums: list[int], expected: bool):
    assert contain_duplicate(nums) == expected
