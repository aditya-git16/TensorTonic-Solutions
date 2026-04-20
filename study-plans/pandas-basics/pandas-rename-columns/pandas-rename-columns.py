import pandas as pd

def rename_columns(data, rename_map):
    """
    Returns: dict mapping renamed column names to value lists
    """
    df = pd.DataFrame(data)
    df.rename(columns=rename_map, inplace=True)
    update_df  = df.to_dict(orient='list')
    return update_df
    pass