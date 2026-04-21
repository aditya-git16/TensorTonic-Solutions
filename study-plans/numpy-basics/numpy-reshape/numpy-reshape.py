import numpy as np

def reshape_array(data, operation):
    """
    Returns: ndarray of float64 with shape determined by the operation
    """
    arr = np.array(data, dtype=np.float64)
    if operation == 'flatten':
        return arr.flatten()
    if operation == 'transpose':
        # Calling .copy() materializes it into an independent array so the returned 
        # object does not share memory with the input
        return arr.T.copy()
    # np.expand_dims(arr, axis=0) inserts a new length-1 axis at position 0, turning shape 
    return np.expand_dims(arr, axis=0)
    pass
