import pandas as pd

def apply_transform(data, column, operation):
    """
    Returns: dict with original columns plus column_transformed
    """
    df = pd.DataFrame(data)
    if operation == 'normalize':
        col_min, col_max = df[column].min(), df[column].max()
        df[f'{column}_transformed'] = ((df[column] - col_min) / (col_max - col_min)).round(4)
    elif operation == 'rank':
        df[f'{column}_transformed'] = df[column].rank().astype(int)
    elif operation == 'double':
        df[f'{column}_transformed'] = df[column]*2
    else:
        df[f'{column}_transformed'] = df[column].apply(operation)
    return df.to_dict('list')
    pass