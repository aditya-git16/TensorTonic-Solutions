import pandas as pd

def groupby_basics(data, group_col, value_col):
    """
    Returns: dict with 'sum', 'mean', 'count' (each a dict)
    """
    df = pd.DataFrame(data)
    group_sum = df.groupby(group_col)[value_col].sum().to_dict()
    group_mean = df.groupby(group_col)[value_col].mean().to_dict()
    group_count = df.groupby(group_col)[value_col].count().to_dict()
    return {
        "sum": group_sum,
        "mean": group_mean,
        "count": group_count
    }
    pass