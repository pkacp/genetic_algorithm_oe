import math


class Functions:
    def sample_function(self):
        return 2 * (self[0] * self[0]) + 5

    # prefered range x1 = [-1.5, 4] x2 = [-3,4] min: f(-0.54719, -1.54719) = -1.9133
    def mccormick_function(self):
        return math.sin(self[0] + self[1]) + (self[0] - self[1]) * (self[0] - self[1]) - 1.5 * \
               self[0] + 2.5 * self[1] + 1.0

    # best working for now
    # prefered range = [-10, 10] min: f(1, 1) = 0
    def levy_function(self):
        # print(arg_arr[0])
        a = math.sin(3.0 * math.pi * self[0])
        b = math.sin(3.0 * math.pi * self[1])
        c = 1.0 + math.sin(2.0 * math.pi * self[1])
        return math.pow(a, 2) + math.pow(self[0] - 1.0, 2) * (1.0 + math.pow(b, 2)) + \
               math.pow(self[1] - 1.0, 2) * (1.0 + math.pow(c, 2))

    # prefered range x1 = [-15, -5] x2 = [-3, 3] min: f(-10, 1) = 0
    def bukin_function(self):
        return 100.0 * math.sqrt(math.fabs(self[1] - 0.01 * math.pow(self[0], 2))) + 0.01 * math.fabs(
            self[0] + 10.0)

    # d= 2, m = 10, prefered range x = [0, 4] min: f(2.20, 1.57) = -1.8013
    def michalewicz_function(self):
        return -1.0 * (self.michalewicz_sum_element(self[0], 1) + self.michalewicz_sum_element(self[1], 2))

    def michalewicz_sum_element(x, i):
        return math.sin(x) * math.pow(math.sin(x * x * i), 20) / math.pi
