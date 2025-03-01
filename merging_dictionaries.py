def merge_dictionaries(dict1, dict2): 
    merged= dict1
    merged.update(dict2)   
    return merged          

dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 10, "d": 4}

print(merge_dictionaries(dict1, dict2))

