import numpy as np

def descriptive_statistics(data: list | np.ndarray) -> dict:
    """
    Calculate various descriptive statistics metrics for a given dataset.
    
    Args:
        data: List or numpy array of numerical values
    
    Returns:
        Dictionary containing mean, median, mode, variance, standard deviation,
        percentiles (25th, 50th, 75th), and interquartile range (IQR)
    """

    # Your code here
    output = {}

    output['mean'] = np.mean(data)
    output['median'] = np.median(data)
    vals, counts = np.unique(data, return_counts=True)
    output['mode'] = vals[counts.argmax()]
    output['variance'] = np.var(data)
    output['standard_deviation'] = np.std(data)
    output['25th_percentile'], output['50th_percentile'], output['75th_percentile'] = np.percentile(data, [25, 50, 75])
    output['interquartile_range'] = output['75th_percentile'] - output['25th_percentile']
    

    return output