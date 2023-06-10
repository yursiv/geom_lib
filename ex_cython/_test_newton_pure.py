import time
import numpy as np
from py_newton import newton

if __name__ == '__main__':
    print("\n\n-------TESTING NEWTON PURE PYTHON")
    n = 100


    def test_func(x):
        f = np.zeros([n])

        for i in np.arange(0, n - 1, 1):
            f[i] = (3 + 2 * x[i]) * x[i] - x[i - 1] - 2 * x[i + 1] - 2

        f[0] = (3 + 2 * x[0]) * x[0] - 2 * x[1] - 3
        f[n - 1] = (3 + 2 * x[n - 1]) * x[n - 1] - x[n - 2] - 4

        return f


    # x0 = np.zeros([n])
    # x, iter = newton(test_func, x0)
    sol_times = []
    for i in range(10):
        x0 = np.zeros([n])
        st = time.time()
        x, iter = newton(test_func, x0)
        sol_time = time.time() - st

        # print('Solution:\n', x)
        # print('Newton iteration = ', iter)
        print('Newton method time', round(sol_time, 3), 'seconds')

        sol_times.append(sol_time)

    sol_times = np.array(sol_times)

    print(f"{sol_times.sum() / sol_times.shape[0]} {sol_times.round(3)}")
