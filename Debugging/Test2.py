import Debugging.SumRatio as Cls

x = [1, 2]
y = [2, 4, 1]

# calculate the sum of ratios
sum_ratio = Cls.SumRatio(x=x, y=y)
result = sum_ratio.get_sum_ratio()
print(result)