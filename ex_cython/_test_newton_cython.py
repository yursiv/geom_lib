import time
import numpy as np
from optimize import newton, some_func

if __name__ == '__main__':
    print("\n\n-------TESTING NEWTON CYTHON")
    n = 100

    sol_times = []
    for i in range(10):
        x0 = np.zeros([n])
        st = time.time()
        x, iter = newton(some_func, x0)
        sol_time = time.time() - st

        # print('Solution:\n', x)
        # print('Newton iteration = ', iter)
        print('Newton method time', round(sol_time, 3), 'seconds')

        sol_times.append(sol_time)

    sol_times = np.array(sol_times)

    print(f"{sol_times.sum()/sol_times.shape[0]} {sol_times.round(3)}")


