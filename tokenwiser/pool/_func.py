import numpy as np

from sklearn.base import BaseEstimator
from ._pool import Pool


class Pooling(Pool, BaseEstimator):
    def __init__(self, func="sum"):
        funcs = {"sum": np.sum, "mean": np.mean, "min": np.min, "max": np.max}
        self.func = func
        if isinstance(func, str):
            self.func = funcs[func]

    def encode_single(self, embs):
        return self.func([e.vec for e in embs], axis=0)
