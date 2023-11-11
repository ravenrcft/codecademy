def median(seq):
    sortseq = sorted(seq)
    mid = len(sortseq) / 2
    median = 0
    if len(seq) % 2 == 0:
        median = (sortseq[mid] + sortseq[mid-1]) / 2.0
    else:
        median = sortseq[mid]
    return median