res = []
def move_zeros(lst):
    # for i in lst:
    #     if i >=1:
    #         res.append(i)
    # for j in lst:
    #     if j == 0:
    #         res.append(j)
    return [i for i in lst if i>=1] + [i for i in lst if i == 0]

print(move_zeros([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]))