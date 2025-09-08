from collections import Counter

def first_uniq_char(chars: str) -> int:
    """
    Returns the index of the first non-repeating character in a string.

    Args:
        chars (str): The input string to search.

    Returns:
        int: The index of the first unique character if found, otherwise -1.

    Example:
        >>> first_uniq_char("leetcode")
        0
        >>> first_uniq_char("loveleetcode")
        2
        >>> first_uniq_char("aabb")
        -1
    """
    counter_list = Counter(chars)
    print(counter_list)
    for iteration,  char in enumerate(chars):
        if counter_list[char] == 1:
            return iteration
    return -1

class Solution:
    def firstUniqChar(self, s: str) -> int:
        return first_uniq_char(s)