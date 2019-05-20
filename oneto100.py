import time

n = 10000000
startTime = time.time()
for_method = 0
for iota in range(n):
    addition = iota + 1
    for_method = for_method + addition
print(f'for_method = {for_method}')
print(f'for_method took {time.time() - startTime} second !')

startTime = time.time()
sap_method = n * (n + 1) * 0.5
print(f'sap_method = {sap_method}')
print(f'sap_method took {time.time() - startTime} second !')