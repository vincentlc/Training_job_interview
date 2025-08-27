def two_sum(nums, target):
    dict_value = {}
    for index,value  in enumerate(nums):
        complement = target - value
        print(dict_value, complement, value)
        if complement in dict_value:
            return [dict_value[complement], index]
        dict_value[value]=index
    return 0
