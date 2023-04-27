def calchex(dec):
    return hex(dec)
def calcdec(hexa):
    return int(hexa, 16)

z = 1
while z==True:
    x = input()
    if x.startswith('0x'):
        print(calcdec(x))
    else:
        y = int(x)
        if y <= 0 or y>=2**31:
            z-=1
            pass
        else:
            print('0x{:2}'.format(calchex(y).upper()[2:]))