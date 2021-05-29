import numpy as np
from scipy import stats
def otsu(bins,counts):
    total=np.sum(counts)
    value_range=np.arange(0,256)
    sumB,nB,maximum,sum1=0,0,0,np.dot(value_range,counts)
    for i,ii in enumerate(value_range):
        nB+=counts[i]
        sumB+=ii*counts[i]
        nF=total-nB
        if nB > 0 and nF > 0:
            mF=(sum1-sumB)/nF
            val=nB*nF*((sumB/nB-mF)**2)
            if val>=maximum:
                level=ii
                maximum=val
        
    return level