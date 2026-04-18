import pandas as pd

def select_columns(data, columns):
    """
    Returns: dict mapping selected column names to value lists
    """
    df = pd.DataFrame(data)
    fil_df = df[columns]
    return fil_df.to_dict('list')
    pass