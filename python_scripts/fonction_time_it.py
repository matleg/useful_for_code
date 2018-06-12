import timeit

print(timeit.timeit('(u[1:]-u[0:-1])', setup='import numpy as np \
; u =np.array([1,2,3,4,5,6])', number=10000))
