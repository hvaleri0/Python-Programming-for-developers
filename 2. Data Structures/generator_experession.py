from sys import getsizeof

values = (x * 2 for x in range(1000000))
# only 112 Bytes even if i  increase the range!
print("GEN:", getsizeof(values))

values2 = [x * 2 for x in range(1000000)]
# 8448728 Bytes because its dependent on the range and it stores in memory!
print("GEN:", getsizeof(values2))

# for x in values:
#     print(x)
