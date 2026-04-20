import pandas as pd

def multi_agg(data, group_col, value_col, funcs):
    """
    Returns: dict mapping function name to {group: value} dict
    """
    df = pd.DataFrame(data)
    result = {}
    for func in funcs:
        func_name = func if isinstance(func, str) else func.__name__
        result[func_name] = df.groupby(group_col)[value_col].agg(func).to_dict()
    return result
    pass