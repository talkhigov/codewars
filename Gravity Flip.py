num = [4, 3, 1, 6, 2]

def flip(d, a):
    if d == 'R':
        return sorted(a)
    elif d == 'L':
        a = sorted(a)
        return a[::-1]
    
print(flip('R', num))
print(flip('L', num))