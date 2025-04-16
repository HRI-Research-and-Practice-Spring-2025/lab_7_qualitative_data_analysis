import numpy as np
import krippendorff

# Example data: rows are items, columns are coders, values are categories
# Missing values (unrated items) can be marked with `np.nan`
data = np.array([
    [1, 1, 1],
    [0, 0, 1],
    [2, 2, 2],
    [1, 1, np.nan],
    [0, 1, 0]
])

alpha = krippendorff.alpha(reliability_data=data.T, level_of_measurement='nominal')
print("Krippendorff's Alpha:", alpha)

