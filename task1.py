import numpy as np

zp = [35, 45, 190, 200, 40, 70, 54, 150, 120, 110]
ks = [401, 574, 874, 919, 459, 739, 653, 902, 746, 832]
mult = []
for i in range(len(zp)):
    mult.append(zp[i] * ks[i])
cov = np.mean(mult) - np.mean(zp) * np.mean(ks)
print(cov)

print(np.cov(zp, ks, ddof=0))
print()
print(np.std(zp, ddof=0))
print()
print(np.std(ks, ddof=0))
print()
print(np.cov(zp, ks, ddof=0) / (np.std(zp, ddof=0) * np.std(ks, ddof=0)))
print()
print(np.corrcoef(zp, ks))
