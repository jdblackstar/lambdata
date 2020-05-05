def tvt_split(df):
    # don't need these, right?
    import pandas as pd 
    import numpy as np 
    from sklearn.model_selection import train_test_split

    train, test = train_test_split(df, test_size=0.1)
    train, val = train_test_split(train, test_size=0.1)

    return train, val, test

def only_nulls(df):
    # don't need these right?
    import pandas as pd 
    import numpy as np 
    
    dfx = df[df.isnull().any(axis=1)]

    return dfx

if __name__ == "__main__":
    print("Don't run this file.")