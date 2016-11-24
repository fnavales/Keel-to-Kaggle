import pandas as pd
import numpy as np
import sys
import warnings

warnings.filterwarnings("ignore")

file_in = str(sys.argv[1])
file_out = str(sys.argv[2])
path = "../results/C45-C.p2_in/"

df = pd.read_csv(path + file_in, sep="\s")
keep_cols = ["positive"]
new_df = df[keep_cols]
new_df.index += 1
new_df.index.name = 'id'
new_df.columns.values[0] = 'class'
new_df.to_csv(path + file_out)
