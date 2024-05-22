def bynary_to_dec(x:str):
    #1011
    x:list[str] = list(x)
    # x -> ['1', '0', '1', '1']
    #        3    2    1    0

    num:int = 0
    for i in range (len(x)):
        num += int(x[i]) * 2 **(len(x)-i-1)
    return num
print (bynary_to_dec('10100'))




