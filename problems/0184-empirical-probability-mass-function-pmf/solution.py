def empirical_pmf(samples):
    """
    Given an iterable of integer samples, return a list of (value, probability)
    pairs sorted by value ascending.
    """
    # TODO: Implement the function
    uni = dict()
    n = 0
    output = list()
    
    for i in samples:
        uni[i] = uni.get(i, 0) + 1
        n += 1

    for num, ct in uni.items():
        output.append((num, ct/n))

    return output
