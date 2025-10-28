'''

Binary Convertion | Dec - Bin 

'''

a = int('11')
b = int('1')
ret = a+b
def convert(n):
    res = ''

    while n > 0:
        res = str(n % 2) + res
        n //= 2
    return res

print(convert(ret))