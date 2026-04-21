import pandas as pd

def concat_dataframes(dfs):
    """
    Returns: list [shape, data] where shape is [rows, cols]
    """
    df = []
    for i in dfs:
        df.append(pd.DataFrame(i))
    dff = pd.concat(df).reset_index(drop=True)
    return [list(dff.shape), dff.to_dict('list')]
    pass