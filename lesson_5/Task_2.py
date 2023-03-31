num = str(int(input()))

def chet_ne_chet (num):
    chet = 0
    nechet = 0
    if int(num[-1:])%2 == 0:
        chet+=1
    else:
        nechet +=1
    chet_ne_chet(int(num[:-1])) 
    print(chet,nechet)