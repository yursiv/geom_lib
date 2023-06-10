import cython
import numpy as np
cimport numpy as np

cpdef tuple newton_raphson(double x0, double tol, int max_iterations):
    cdef double x = x0
    cdef double f, f_prime

    for i in range(max_iterations):
        f = x**2 - 4  # Функция f(x) = x^2 - 4
        f_prime = 2*x  # Производная f'(x) = 2*x

        if abs(f) < tol:
            break

        x = x - f/f_prime

    cdef tuple out = (i, x)
    return out


cdef int n=100
cpdef  np.ndarray[np.float_t, ndim=1] some_func(x):
    cdef np.ndarray[np.float_t, ndim=1] f = np.zeros([n], dtype=float)
    
    for i in np.arange(0,n-1,1):
            f[i] = (3 + 2*x[i])*x[i] - x[i-1] - 2*x[i+1] - 2
    
    f [0] = (3 + 2*x[0] )*x[0] - 2*x[1] - 3
    f[n-1] = (3 + 2*x[n-1] )*x[n-1] - x[n-2] - 4
    
    return f

cdef tuple get_jacobian(func, np.ndarray[np.float_t, ndim=1] x, double delta_x, args):
    cdef int n = x.shape[0]

    cdef np.ndarray[np.float_t, ndim=2] jac_matr = np.zeros((n, n), dtype=np.float64)
    cdef np.ndarray[np.float_t, ndim=1] f0 = func(x, *args)
    cdef np.ndarray[np.float_t, ndim=1] f1, deriv

    cdef int i
    cdef np.float_t x_i

    for i in range(n):
        x_i = x[i]

        x[i] = x_i + delta_x
        f1 = func(x, *args)

        x[i] = x_i

        deriv = (f1 - f0) / delta_x
        jac_matr[:, i] = deriv

    cdef tuple out = (jac_matr, f0)
    return out

#Tuple[np.ndarray[np.float_t, ndim=1], int]
cpdef  tuple newton(func, np.ndarray[np.float_t, ndim=1] x, args=(), int max_iters=500, double tol=1.0e-9, double delta_x=1e-4, bint log=False):
    cdef int xcount = x.shape[0]

    cdef int i
    cdef np.ndarray[np.float_t, ndim=2] jac_matr
    cdef np.ndarray[np.float_t, ndim=1] f0
    cdef np.ndarray[np.float_t, ndim=1] dx
    cdef tuple out = (-1, None)

    cdef int rank 

    for i in range(max_iters):
        jac_matr, f0 = get_jacobian(func, x, delta_x, args=args)

        if np.sqrt(np.dot(f0, f0) / xcount) < tol:
            out = (i, x)
            return out

        rank = np.linalg.matrix_rank(jac_matr)
        if rank == xcount:
            dx = np.linalg.solve(jac_matr, f0)
        else:
            if log:
                print(i, "bad rank:", rank, jac_matr)
            return out

        x -= dx

    print("Too many iterations for the Newton method")

    return out
   