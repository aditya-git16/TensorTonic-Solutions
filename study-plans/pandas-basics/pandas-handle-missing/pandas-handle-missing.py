import pandas as pd

def handle_missing(data, fill_value):
    df = pd.DataFrame(data)
    null_counts = df.isnull().sum().to_dict()
    df.fillna(fill_value, inplace=True)
    cleaned_data = df.to_dict(orient='list')
    return {
        'null_counts': null_counts,
        'cleaned_data': cleaned_data
    }
    pass