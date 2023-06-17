

def checkisgt(index, params):
    seq, x = params
    return seq[index] > x

def checkisgte(index, params):
    seq, x = params
    return seq[index] >= x

def findfirst(seq, x, check):
    ans = left_binsearch(0, len(seq)-1, check, (seq, x))
    if not check(ans, (seq, x)):
        return len(seq)
    return ans

def countx(seq, x):
    indexgt = findfirst(seq, x, checkisgt)
    indexgte = findfirst(seq, x, checkisgte)

    return indexgt - indexgte

