def count_element(text:str)->dict:
    """
    count the repeated element in a string and sort it, all value are put to lower case

    Args:
        text: a string

    Returns:
        dict, dictionary of the occurence of each letter in sorted order

    Note: This could also simply be replace by Counter(text.lower()), but wanted to implemented it manually 
        for training purpose 
    """
    dict_text = {}
    for char in text.lower():
        if char in dict_text:
            dict_text[char]+=1
        else:
            dict_text[char]=1
    dict_text = dict(sorted(dict_text.items())) # sort the dict
    return dict_text


def is_anagram(text: str, anagram: str) -> bool:
    """
    Check if two strings are anagrams, ignoring case but including spaces and punctuation.

    Args:
        text: First input string.
        anagram: Second input string.

    Returns:
        bool: True if the strings are anagrams, False otherwise.

    Examples:
        >>> is_anagram("listen", "silent")
        True
        >>> is_anagram("Hello", "World")
        False
    """
    print(len(text), len(anagram))
    if len(text) != len(anagram):
        return False

    dict_text, dict_anagram= map(count_element,(text, anagram))
    print(dict_text, dict_anagram)
    return  dict_text == dict_anagram



class Solution:
    def is_anagram(self, text: str, anagram:str, ) -> bool:
        """LeetCode-style method name."""
        return is_anagram(text, anagram)