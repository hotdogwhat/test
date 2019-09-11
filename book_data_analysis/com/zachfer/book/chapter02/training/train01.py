import numpy as np

print("-----------------第一题结果为-------------------")
print(np.arange(0, 1, 0.01))

print("\n", "-----------------第二题结果为-------------------")
print(np.random.randn(100))

print("\n", "-----------------第三题结果为-------------------")
x, y = np.array([1, 2, 3]), np.array([4, 5, 6])
print("数组相加为：", x + y)
print("数组相减为：", x - y)
print("数组相乘为：", x * y)
print("数组相除为：", x / y)

print("\n", "-----------------第四题结果为-------------------")
np.random.seed(666)
arr_sort = np.random.randint(1, 10, size=10)
print("排序前数组为：", arr_sort)
arr_sort.sort()
print("排序后数组为：", arr_sort)



