
def uniqueString2(string: str):
    index = 0
    list_dictionarry = dict({string[0]:0})
    print(f'index={index} list_dictionarry={list_dictionarry}')
    for character in string:
        if(character in list_dictionarry): 
            list_dictionarry[character]+=1
        else:
            list_dictionarry[character]=1
    print(list_dictionarry)
    for character in string:
        if list_dictionarry[character]==1:
            return index
        else:
            index+=1
    
    return -1


def uniqueString(string: str):
    # Edge case: empty string
    if not string:
        return -1
    
    counts = {}
    print(f'list_dictionarry={counts}')
    for character in string:
        if(character in counts): 
            counts[character]+=1
        else:
            counts[character]=1
    print(counts)
    for index, character in enumerate(string):
        if counts[character]==1:
            return index
    
    return -1


if __name__=='__main__':
    uniqueString('leetcode')