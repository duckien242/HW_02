import Debugging.SumRatio as Cls

x = [1, 2, 3]
y = [2, 4, 1]
correct_sum_ratio = 1/2 + 2/4 + 3/1

# calculate the sum of ratios
sum_ratio = Cls.SumRatio(x=x, y=y)
result = sum_ratio.get_sum_ratio()

if result == correct_sum_ratio:
    print('Test 1 passed. Sum of ratios = ', result)
else:
    print('Test 1 failed. Calculated sum of ratios: ', result, 'Correct sum of ratios: ', correct_sum_ratio)
