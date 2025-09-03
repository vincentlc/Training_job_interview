def count_num(input_list: list[int])-> dict[int]:
    """
    count the repeated element in a string
    Args:
        input_list: a list of int

    Returns:
        dict, dictionary of the occurence of each value

    Note: This could also simply be replace by Counter(input_list), but wanted to implemented it manually 
        for training purpose 
    """

    occurrence_dict = {}
    for num in input_list:
        if num in occurrence_dict:
                occurrence_dict[num]+=1
        else:
            occurrence_dict[num]=1
    return occurrence_dict

def search_repeated(input_list:list[int], occurrence_dict:dict[int])->list[int]:
    """
    search value repeated in a num list, base on a dict of occurence
    Args:
        input_list: a list of int
        occurrence_dict: a dictionary of int

    Returns:
        list , list of the repeated value of the int

    """
    repeated_values = []
    for item in input_list:
        if occurrence_dict.get(item, 0) > 0:
            occurrence_dict[item] -=1
            repeated_values.append(item)
    return repeated_values

def __validate_non_negative(seq: list[int], name: str) -> None:
    """
    Scan *seq* and raise ValueError the first time a negative value appears.

    Parameters
    ----------
    seq : List[int]
        The list we want to validate.
    name : str
        Human‑readable identifier used in the error message (e.g. "nums1").
    """
    for i, val in enumerate(seq):
        if val < 0:
            raise ValueError(
                f"Negative value {val} found at index {i} of '{name}'. "
                "All numbers must be >= 0."
            )

def intersect(nums1: list[int], nums2: list[int]) -> list[int]:
    occurrence_dict = {}
    repeated_values = []
    __validate_non_negative(nums1, str(nums1))
    __validate_non_negative(nums2, str(nums2))
    if len(nums1) > len(nums2):
        large, small = nums1, nums2
        
    else:
        large, small = nums2, nums1
    occurrence_dict = count_num(large)
    repeated_values=search_repeated(small, occurrence_dict)
    return repeated_values

class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        return intersect(nums1, nums2)

