print("Start csv read application")

import pandas as pd
import numpy as np

df = pd.read_csv('pokemon.csv')
print(len(df["#"]))
test = np.array(len(df["#"]))
