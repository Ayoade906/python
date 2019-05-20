import time

n = 10000000
startTime = time.time()
for_method = 0
for iota in range(n):
    addition = iota + 1
    for_method = for_method + addition
print(f'for_method = {for_method}')
print(f'for_method took {time.time() - startTime} second !')


def sum_n(num):
    return num * (num + 1) * 0.5


startTime = time.time()
sap_method = sum_n(n)
print(f'sap_method = {sap_method}')
print(f'sap_method took {time.time() - startTime} second !')

