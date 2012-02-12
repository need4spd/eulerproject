hseqdict = {} # {갯수: 숫자}
for i in range(1, 1000001):
    hseq = [i]
    while hseq[-1] != 1:
        if hseq[-1] % 2 == 0:
            hseq.append(hseq[-1] / 2)
        else:
            hseq.append(3 * hseq[-1] + 1)
    hseqdict[len(hseq)] = i

print (hseqdict[max(hseqdict.keys())])