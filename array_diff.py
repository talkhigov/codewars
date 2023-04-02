def array_diff(a, b):
    # result = []
    # for i in a:
    #     if i not in b:
    #         result.append(i)
    # return result

    return [i for i in a if i not in b]
        
print(array_diff([], [1,2]))