import pytest 
from first_uniq_char import first_uniq_char, Solution
@pytest.mark.parametrize(
    "char, expected",
    [
        ("leetcode", 0),
        ("loveleetcode", 2),
        ("aabb", -1),
        ("", -1),
        
    ],
) 
def test_first_uniq_char_function(char: str, expected: int):
    """
    Test the `first_uniq_char` function with various inputs, including edge cases.
    
    """
    assert first_uniq_char(char) == expected

def test_solution_class_intersect():
    """
    Test the `Solution.firstUniqChar` method with various inputs.
    """ 
    solution = Solution()
    assert solution.firstUniqChar("leetcode") == 0
    assert solution.firstUniqChar("loveleetcode") == 2
    assert solution.firstUniqChar("aabb") == -1



