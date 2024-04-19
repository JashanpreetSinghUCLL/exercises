def merge_dictionaries(d1, d2, merge_function):
    resultd1 = dict(d1)
    
    for key, value in d2.items():
        if key in resultd1:
            resultd1[key] = merge_function(resultd1[key], value)
        else:
            resultd1[key] = value
    return resultd1