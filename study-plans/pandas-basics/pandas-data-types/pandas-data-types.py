import pandas as pd

def data_types_overview(data):
    """
    Returns: dict with 'dtypes', 'type_counts', 'num_columns'
    """
    df = pd.DataFrame(data)
    type_counts = {str(dtype): int(count) for dtype, count in df.dtypes.value_counts().items()}
    dtypes = {col: str(dtype) for col, dtype in df.dtypes.items()}
    _ , num_column = df.shape
    return {
        "dtypes" : dtypes , 
        "type_counts" : type_counts , 
        "num_columns" : num_column
    }
    pass