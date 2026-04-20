import numpy as np

def euclidean_distance(x, y):
    """
    Returns: float, the Euclidean distance between x and y.
    """
    x = np.array(x)
    y = np.array(y)
    # linalg.norm is used to calculate the Euclidean distance between two vectors
    result = np.linalg.norm(x - y)
    # item() is used to convert the result to a float how numpy.linalg.norm returns a scalar
    return result.item()  
    pass