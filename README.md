# Homework Assignment 2

**Problem 1: Debugging (Weight 2)**. Debugging is the process of 
identifying and resolving issues ('bugs') that prevent your code from running correctly.
In this problem, you are asking to find and fix the bugs 
in the class `SumRatio` (in the file `\Debugging\SumRatio.py`). The class `SumRatio` has a very simple task. It gets two arrays 
(x1, x2, ..., xn) and (y1, y2, ..., yn), and returns the sum of element-wise ratios 
(x1/y1 + x2/y2 + ... + xn/yn). 

1. Find and fix the bugs in the current implementation of `SumRatio` class
such that you can run `Test1.py` script without any error. 
*Hint:* Watch [this video](https://www.youtube.com/watch?v=QJtWxm12Eo0) 
to learn about the debugging features of PyCharm and read 
[this post](https://blog.hartleybrody.com/debugging-code-beginner/) for
some debugging tips. 

2. After fixing the bugs `SumRatio` class, run `Test2.py` script. 
Note that while `SumRatio` class implicitly assumes the `x` and `y` have the same
number of elements, the `x` and `y` used in `Test2.py` have different sizes. 
But when you run `Test2.py` it runs without any issues and prints `1.0` 
for the sum of element-wise ratios. 
This is clearly an error since the sum of element-wise ratios of 
two arrays that have different length is not defined. 
These types of errors are often hard to catch because Python won't complain 
about them at run time. 
One way to safe-guard your code against 
these such errors is to have Python explicitly check the assumptions
held by classes. Read [this post](https://www.programiz.com/python-programming/assert-statement)
 to learn how to use `assert` for this purpose. 
 Use `assert` in the implementation of `SumRatio` to ensure 
 that `x` and `y` have the same size. If not, we want `assert` to display
 `x and y should have the same number of elements.`

**Problem 2: Exception Handling (Weight 2)**. Open `Test3.py`. Note that the second element of `y` is 0. So as expected, 
when we run `Test3.py`, Python will generate a `ZeroDivisionError` and terminates 
the execution of `Test3.py` with minimal information about what caused 
the error (it tells us that `ZeroDivisionError` occurred in line
 `sum += self.x[i]/self.y[i]` but it doesn't specify calculating which
 ratio caused the error). Also, in many cases, we would like to 
 handle errors in a specific way. For example in this exercise, we are going to 
 assume that division by zero is accepted (and hence should not terminate 
 the execution) but then we want to return 'Not a number' if the denominator of
 one of the ratios is 0. 
 The simplest way to handle exceptions is with a "try-except" block. 
 Here is an example:
 
    
        x = 10
        y = 0
        try:
            ratio = x/y
        except ZeroDivisionError:
            print('Division by 0 in calculating the ratio x/y')

Watch Lecture 7 of the MIT Open Course
 [Introduction to Computer Science and Programming in Python](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/lecture-videos/lecture-7-testing-debugging-exceptions-and-assertions/)
 to learn how to use "try-except" blocks to handle errors. 
            
Modify the class `SumRatio` such that if `ZeroDivisionError` occurred in line
 `sum += self.x[i]/self.y[i]` your code:
  1. prints `Warning: Division by zero occurred in calculating 
  the ratio in position x.`, where `x` takes the value of index `i`. 
  2. returns `math.nan` as the results of calculating the sum of ratios (not that to use `math.nan` you need to add `import math` at the
  top of `SumRatio.py`). 



**Problem 3: Expected Health Utility (Weight 3)**. 
Modify the decision tree classes we implemented in class 
(`DecisionTree.py` in this repository) such that 
you can also get the expected health utility of alternatives in addition to 
the expected cost. Test your code on the decision tree below and 
print the expected cost and expected health utility of nodes C1 and C3. 

![Alt text](DecisionTree/DecisionTree.png?raw=true "Test")


 **Problem 4: Economic Evaluation (Weight 1)**.
 For the decision tree you created in Problem 3, calculate the incremental cost-effectiveness ratio (ICER) of Arm 2 
 with respect to Arm 1.  
