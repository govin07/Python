import pandas as pd
import numpy as np

# rad = pd.read_csv('kohli_ipl.csv',index_col='match_no').squeeze("columns")

# print(type(rad))

# print(rad)

bol = pd.read_csv('bollywood.csv',index_col='movie')
list(bol)
# print(bol)

# print(bol.value_counts())
print([bol <= 20])