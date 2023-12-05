def fair_sharer(values, num_iterations, share=0.1):
    """Runs num_iterations.
    In each iteration the highest value in values gives a fraction (share)
    to both the left and right neighbor. The leftmost field is considered
    the neightbor of the rightmost field.
    Examples:
    fair_sharer([0, 1000, 800, 0], 1) --> [100, 800, 900, 0]
    fair_sharer([0, 1000, 800, 0], 2) --> [100, 890, 720, 90]
    Args
    values:
    1D array of values (list or numpy array)
    num_iteration:
    Integer to set the number of iterations
    """
    for i in range(num_iterations):
        values_max = max(values)
        index = values.index(values_max)
        neighbors_1 = index +1
        neighbors_2 = index -1
        
        to_share =  max(values)*share
        
        values_new = values
        values_new[index] = values[index]-to_share*2
        values_new[neighbors_1] = values[neighbors_1] + to_share
        values_new[neighbors_2] = values[neighbors_2] + to_share
    return values_new

if __name__ == "__main__":
    print(fair_sharer([0,1000,800,0], 2))
