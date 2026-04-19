import pandas as pd

def reset_index_demo(data, index_col):
    """
    Returns: list [columns_before_reset, columns_after_reset]
    """
    df = pd.DataFrame(data)
    df.set_index(index_col, inplace=True)
    pre_columns = df.columns.tolist()
    df.reset_index(inplace=True)
    post_columns = df.columns.tolist()
    return [pre_columns, post_columns]
    pass