
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