import numpy as np
import pandas as pd

country = ['india', 'pakistan','usa', 'nepal', 'srilanka']

marks = [57,68,75,25]
subject = ["math","English","Hindi","science"]

mark = pd.Series(marks, index=subject)
print(mark)

total = {
    'maths':67,
    'english':50,
    'hindi':85,
    'sanskrit':58
}
print(mark.size)
print(pd.Series(total,name = "govind ke number"))
print(pd.Series(country))