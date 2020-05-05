import pandas as pd
import numpy as np
from .my_mod import tvt_split, only_nulls

# these were tests
# print("HELLO WORLD")
# print(2+2)

# create NaN variable to put into our dataframe
NaN = np.nan

#create dataframe - not too sure about formatting here, it's a little long
# maybe i don't use this dictionary format
df = pd.DataFrame({
    "a":[1,2,NaN,4,5,NaN,7,8,9,0],
    "b":[0,9,NaN,7,6,5,4,NaN,2,1]}
)


print(df.head())

# use only_nulls function from my_mod.py on the local dataframe 'df'
only_nulls(df)

# train, val, test split (not even sure this is applicable to the assignment)
tvt_split(df)







