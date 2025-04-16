
### fleiss_kappa.py

import numpy as np
from statsmodels.stats.inter_rater import fleiss_kappa

# Example matrix: rows are items, columns are number of coders assigning each category
# For example, the first row [0, 0, 3] means all 3 coders chose last category for item 1
matrix = np.array([
    [0, 0, 3],
    [1, 2, 0],
    [0, 3, 0],
    [0, 1, 2],
    [3, 0, 0],
    [1, 1, 1]
])

fkappa = fleiss_kappa(matrix)
print("Fleiss' Kappa:", fkappa)