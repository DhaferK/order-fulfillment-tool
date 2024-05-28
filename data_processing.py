import pandas as pd

def analyze_orders(data):
    # Calculate total order volume
    total_volume = data['TotalOrderVolume'].sum()
    
    # Identify peak order periods
    peak_periods = data['OrderDate'].value_counts().head(5)
    
    return {
        'TotalVolume': total_volume,
        'PeakPeriods': peak_periods.to_dict()
    }