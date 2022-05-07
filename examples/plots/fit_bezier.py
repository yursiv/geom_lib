# https://stackoverflow.com/a/51351849/11365520

import matplotlib.pyplot as plt
import numpy as np
from scipy.special import comb as binom

import time

bern = lambda deg, u, pi: u ** pi * (1 - u) ** (deg - pi) * binom(deg, pi)

degree = 2
cp_count = degree + 1
bern_coeff = lambda params: [[bern(degree, u, pi) for pi in range(cp_count)] for u in params]

fcn = np.log

params_count = 16
samples_step = 3

bezier_params = np.linspace(0., 1., params_count)
bezier_param_samples = bezier_params[0:params_count:samples_step]

input_params = np.linspace(0.1, 2.5, params_count)
input_params_samples = input_params[0:params_count:samples_step]

in_co = np.column_stack((input_params_samples, fcn(input_params_samples)))  # shapes (9,2)

st = time.time()

pseudo_inv = np.linalg.pinv(bern_coeff(bezier_param_samples))  # (9,4) -> (4,9)
bezier_cps = pseudo_inv.dot(in_co)  # (4,9)*(9,2) -> (4,2)

print("time: ", time.time() - st)

pnts_on_bezier = np.array(bern_coeff(bezier_params)).dot(bezier_cps)

residuum = fcn(pnts_on_bezier[:, 0]) - pnts_on_bezier[:, 1]

fig, ax = plt.subplots()

ax.plot(input_params, fcn(input_params), 'r-')
ax.plot(input_params_samples, in_co[:, 1], 'ro', label='input')
ax.plot(pnts_on_bezier[:, 0], pnts_on_bezier[:, 1], 'k-', label='fit')

ax.plot(input_params, 10. * residuum, 'b-', label='10*residuum')
ax.plot(bezier_cps[:, 0], bezier_cps[:, 1], 'ko:', fillstyle='none')

ax.legend()
fig.show()
