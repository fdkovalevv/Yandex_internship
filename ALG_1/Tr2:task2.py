def tsk():
    seq = []
    while True:
        number = int(input())
        if number == -2000000000:
            break
        seq.append(number)

    if len(set(seq)) == 1:
        return "CONSTANT"
    ASCENDING = all(seq[i] < seq[i+1] for i in range(len(seq)-1))
    WEAKLY_ASCENDING = all(seq[i] <= seq[i+1] for i in range(len(seq)-1))

    DESCENDING = all(seq[i] > seq[i+1] for i in range(len(seq)-1))
    WEAKLY_DESCENDING = all(seq[i] >= seq[i+1] for i in range(len(seq)-1))

    if ASCENDING:
        return "ASCENDING"
    elif WEAKLY_ASCENDING:
        return "WEAKLY ASCENDING"
    elif DESCENDING:
        return "DESCENDING"
    elif WEAKLY_DESCENDING:
        return "WEAKLY DESCENDING"
    else:
        return "RANDOM"
print(tsk())