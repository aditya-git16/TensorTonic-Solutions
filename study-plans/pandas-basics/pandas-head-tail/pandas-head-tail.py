import pandas as pd

def head_tail(data, n):
    """
    Returns: dict with 'head' and 'tail' (both dicts of column -> list)
    """
    df = pd.DataFrame(data)
    head = {col: values.tolist() for col, values in df.head(n).items()}
    tail = {col: values.tolist() for col, values in df.tail(n).items()}
    return {
        "head" : head,
        "tail" : tail
    }
    pass