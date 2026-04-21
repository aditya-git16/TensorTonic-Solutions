import pandas as pd

def unstack_to_wide(data, index_col, columns_col, values_col):
    """
    Returns: dict with index_col plus one key per unique value in columns_col
    """
    df = pd.DataFrame(data)
    unstacked = df.pivot(index=index_col, columns=columns_col, values=values_col)
    unstacked.columns.name = None
    unstacked = unstacked.reset_index()
    return unstacked.to_dict('list')
    pass