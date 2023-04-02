def descending_order(num):
    num = str(num)
    result = []
    res = ''
    for i in num:
        result.append(int(i))
    result = sorted(result)[::-1]
    for i in result:
        res+=str(i)
    res = int(res)
    return res
        
# print(descending_order(42518976))

def descending_order(num):
    return int("".join(sorted(str(num), reverse=True)))

print(descending_order(123456987))

