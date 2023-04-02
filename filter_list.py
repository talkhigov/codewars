lst = [1,2,'aasf','1','123',123]

def filter_list(l):
    # for i in l:
    #     if type(i) == int:
    #         print(i)
    
    return [i for i in l if type(i) == int]

print(filter_list(lst))