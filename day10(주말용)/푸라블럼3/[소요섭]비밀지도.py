def get_binary(intnum, pn):
    n = 1
    rems = []
    while intnum or n < pn+1:
        intnum, rem = divmod(intnum,2)
        rems.append(rem)
        intnum = intnum
        n +=1
    rems.reverse()
    return rems

def solution(n, arr1, arr2):

    answer = []

    for a1, a2 in zip(arr1, arr2):
        pw = str()
        bi_1 = get_binary(a1,n)
        bi_2 = get_binary(a2,n)

        passwords = [0]*n

        for i,val in enumerate(bi_1):
            passwords[i] += val
        for i,val in enumerate(bi_2):
            passwords[i] += val

    # print(passwords)
        for val in passwords:
            if val > 0:
                pw +='#'
            else : pw += ' '
        answer.append(pw)

    return answer
