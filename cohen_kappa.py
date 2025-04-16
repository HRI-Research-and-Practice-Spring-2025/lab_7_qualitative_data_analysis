from sklearn.metrics import cohen_kappa_score

# Example data: coder1 and coder2 assign one category per item (mutually exclusive)
coder1 = [0, 1, 2, 1, 0, 2]
coder2 = [0, 2, 2, 1, 0, 1]

kappa = cohen_kappa_score(coder1, coder2)
print("Cohen's Kappa:", kappa)
