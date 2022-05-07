def scale_param(t, in0, in1, out0, out1) -> float:
    in_norm = (t - in0) / (in1 - in0)
    return out0 * (1 - in_norm) + in_norm * out1
