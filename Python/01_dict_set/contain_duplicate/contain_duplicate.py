def contain_duplicate(nums: list[int]) -> bool:
    """
    Given an integer array `nums`, return `True` if any value appears **at least twice** in the array, 
    and return `False` if all elements are distinct.

    Args:
        nums: List of integers.

    Returns:
        Bool, True if all elements appear at least twice
    """
    dict_value = {}
    for value  in nums:
        if(value in dict_value): 
            return True
        else:
            dict_value[value]=1
    print(dict_value)
 
    return False