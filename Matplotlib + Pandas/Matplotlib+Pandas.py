import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv("Matplotlib + Pandas/pokedex.csv")

type_count = df["Type1"].value_counts(ascending=True)

plt.barh(type_count.index, type_count.values, color="#03dffc",
                                              edgecolor="black")

plt.title("# of pokemon by primary type")
plt.xlabel("Count")
plt.ylabel("Type")
plt.tight_layout()
plt.show()