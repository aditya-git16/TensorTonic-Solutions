import pandas as pd

def drop_duplicates(data):
    """
    Returns: list [rows_before, rows_after, cleaned_data]
    """
    df = pd.DataFrame(data)
    pre_rows = df.shape[0] # accesing first element of shape tuple which represents rows in the DataFrame
    # drop_duplicates function drops the duplicate rows in the DataFrame
    df.drop_duplicates(inplace=True)
    post_rows = df.shape[0]
    cleaned_data = df.to_dict(orient='list')
    return [pre_rows, post_rows, cleaned_data]
    pass