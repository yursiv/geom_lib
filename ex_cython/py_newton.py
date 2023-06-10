#
#  MIT License
#  Copyright (c) 2023. [Yuriy Sivalniev]
#  #
#  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and
#  associated documentation files (the "Software"), to deal in the Software without restriction, including
#  without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
#  sell copies of the Software, and to permit persons to whom the Software is furnished to do so,
#  subject to the following conditions:
#  #
#  The above copyright notice and this permission notice shall be included in all copies or substantial
#  portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
#  OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
#  MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO
#  EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
#  DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
#  OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE
#  USE OR OTHER DEALINGS IN THE SOFTWARE.

# https://habr.com/ru/post/419453/
from typing import Callable, Tuple

import numpy as np
import time


def jacobian(func, x, dx, args):
    n = len(x)

    jac_matr = np.zeros([n, n])
    f0 = func(x, *args)

    for i in np.arange(0, n, 1):
        tt = x[i]
        x[i] = tt + dx
        f1 = func(x, *args)
        x[i] = tt

        deriv = (f1 - f0) / dx
        if deriv == 0:
            return None, None

        jac_matr[:, i] = deriv

    return jac_matr, f0


def get_jacobian(func, x, delta_x, args):
    n = len(x)

    jac_matr = np.zeros([n, n])
    f0 = func(x, *args)

    for i in np.arange(0, n, 1):
        x_i = x[i]

        x[i] = x_i + delta_x
        f1 = func(x, *args)

        x[i] = x_i

        deriv = (f1 - f0) / delta_x
        # deriv[deriv==0] = 1
        # cprint("    deriv:", deriv)
        jac_matr[:, i] = deriv

    return jac_matr, f0


def newton(func, x, args=(), max_iters=500, tol=1.0e-9, delta_x=1e-4, log=False):
    xcount = len(x)

    for i in range(max_iters):
        jac_matr, f0 = get_jacobian(func, x, delta_x, args=args)

        if np.sqrt(np.dot(f0, f0) / xcount) < tol:
            return x, i

        rank = np.linalg.matrix_rank(jac_matr)
        if rank == xcount:
            dx = np.linalg.solve(jac_matr, f0)
        else:
            if log:
                print(i, "bad rank:", rank, jac_matr)
            return None, -1

        # try:
        #     dx = np.linalg.solve(jac_matr, f0)
        # except Exception as ex:
        #     print(ex)
        #     print(jac_matr)
        #     return None, -1

        # print("x: ", x)
        # print("dx: ", dx)
        x = (x - dx)

    # print("Too many iterations for the Newton method")
    # print(x, func(x))
    # AttributeError("Too many iterations for the Newton method")

    return None, -1

