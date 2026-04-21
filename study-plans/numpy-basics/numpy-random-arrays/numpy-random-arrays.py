import numpy as np

def generate_random_array(shape, kind, seed):
    """
    Returns: 2D ndarray of float64 random values
    """
    if kind == 'uniform':
        np.random.seed(seed=seed)
        return np.random.random(size=shape)
    elif kind == 'normal':
        np.random.seed(seed=seed)
        return np.random.standard_normal(size=shape )
    elif kind == 'integer':
        return rng.randint(low=0, high=100, size=shape)
    else:
        raise ValueError(f"Invalid kind: {kind}")
    pass
