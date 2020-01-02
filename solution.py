def fromArr(A, num):
    s = 0
    max = 0
    initIndex = 0

    for i in range(0,len(A)):
        if (i <= len(A) - num):
            for j in range(i,i + num):
                s = s + A[j]

        if (s > max):
            max = s
            initIndex = i

        s = 0
    return (max, initIndex)

def solution(A, K, L):
    if(K+L>len(A)):
            return -1

    result = 0

    indexTuple = fromArr(A,K)
    result += indexTuple[0]
    leadingList = A[0:indexTuple[1]][:]
    trailingList = A[(indexTuple[1] + K):len(A)][:]

    mergedLists = leadingList+ trailingList

    indexTuple = fromArr(mergedLists, L)
    result += indexTuple[0]
    return result
