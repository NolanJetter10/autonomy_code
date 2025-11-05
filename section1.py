#!/usr/bin/env python3

import numpy as np

# add import and helper functions here
if __name__ == "__main__":
    np.random.seed(42)
    x = np.random.normal(size=(4, 10))
    dists = ((x[:, None, :] - x[None, :, :])**2).sum(axis=-1)
    print(dists)