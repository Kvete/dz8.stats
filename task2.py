import numpy as np
import scipy.stats as stats

a = [131, 125, 115, 122, 131, 115, 107, 99, 125, 111]
print(
    stats.t.interval(0.95, df=len(a) - 1, loc=np.mean(a), scale=stats.sem(a)))
