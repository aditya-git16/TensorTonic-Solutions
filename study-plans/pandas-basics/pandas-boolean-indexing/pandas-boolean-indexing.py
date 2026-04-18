import pandas as pd

def boolean_filter(data, column, threshold):
    """
    Returns: dict with 'filtered_data' (dict) and 'count' (int)
    """
    df = pd.DataFrame(data)
    filtered_data = df.loc[df[column] > threshold]
    count , _ = filtered_data.shape
    return {
        "filtered_data" : filtered_data.to_dict('list') ,
        "count" : count
    }
    pass