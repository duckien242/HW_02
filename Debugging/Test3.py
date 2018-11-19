import Debugging.SumRatio as Cls
import math

x = [1, 2, 3]
y = [2, 0, 1]
correct_sum_ratio = math.nan

# calculate the sum of ratios
sum_ratio = Cls.SumRatio(x=x, y=y)
result = sum_ratio.get_sum_ratio()

if result is correct_sum_ratio:
    print('Test 2 passed. Sum of ratios = ', result)
else:
    print('Test 2 failed. Calculated sum of ratios: ', result, 'Correct sum of ratios: ', correct_sum_ratio)
