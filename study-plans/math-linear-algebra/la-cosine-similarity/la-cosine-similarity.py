import numpy as np

def cosine_similarity(a, b):
    """
    Returns: float in [-1, 1], cosine similarity between a and b.
    """
    a = np.array(a)
    b = np.array(b)
    dot_product = np.dot(a,b)
    a_norm = np.linalg.norm(a)
    b_norm = np.linalg.norm(b)
    if a_norm==0 or b_norm==0 :
        return 0.000000
    elif a_norm == 1 and b_norm == 1 :
        return dot_product
    else : 
        result = dot_product / (a_norm*b_norm)
        return result
    pass