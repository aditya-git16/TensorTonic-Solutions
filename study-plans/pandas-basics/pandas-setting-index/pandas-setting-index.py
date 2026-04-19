import pandas as pd

def set_index_column(data, index_col):
    """
    Returns: dict with 'index_values', 'columns', 'data'
    """
    df = pd.DataFrame(data)
    # set_index is used to set the index of the DataFrame and inplace=True is used to modify the DataFrame in place.
    df.set_index(index_col, inplace=True)
    return {
        'index_values': df.index.values,
        'columns': df.columns.values,
        'data': df.to_dict(orient='list')
    }
    pass