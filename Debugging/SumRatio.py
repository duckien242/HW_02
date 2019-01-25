class SumRatio:
    def __init__(self, x, y):
        """
        :param x: (list) of numbers
        :param y: (list) of numbers
        """
        self.x = x
        self.y = y

    def get_sum_ratio(self):
        """
        :return: x_1/y_1 + x_2+y_2 + ...
        """

        # number of ratios to calculate
        num_of_elements = len(self.x_)

        # sum all ratios
        sum = 0
        for i in range(1, num_of_elements):
            sum = self.x[i]/self.y[i]

        return sum
