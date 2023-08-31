def conversion(num):
    i = 0
    while i < len(num):
        if i != '+':
            util = int(num[:i]+ num[i+1:])
        i +=1
    return(util)
n = input()
resultado = conversion(n)
print(resultado)