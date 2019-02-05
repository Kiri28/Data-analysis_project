def percence(gr1,gr2):
    S=0
    for i in range(len(gr1)):
        if gr1[i]>=gr2[i]:
            S+=(100-(gr2[0]*100/gr1[0]))/len(gr1)
        else:
            S+=(100-(gr1[0]*100/gr2[0]))/len(gr1)
    return S
