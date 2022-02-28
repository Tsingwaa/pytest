# import seaborn as sns
# from PIL import Image
from asyncio import base_subprocess
from cProfile import label
from pickletools import markobject
from sklearn.manifold import TSNE
from sklearn.metrics import confusion_matrix
# from scipy import stats, integrate
from matplotlib import pyplot as plt
# from os.path import join
import pandas as pd
import numpy as np
# %matplotlib inline

# read data
csv_fpath = "/Users/waa/Desktop/lambda.csv"
df = pd.read_csv(csv_fpath)
weight = df["Lambda"].tolist()
CT_mca = df["CT"].tolist()
TP_mca = df["TP"].tolist()
SC_mca = df["SC"].tolist()
bsl = [TP_mca[0]] * len(weight)
best_bsl = [85.21] * len(weight)


# Set matplotlib setting
plt.figure(figsize=(9,8))
plt.xlabel("Lambda")
plt.ylabel("Mean Class Accuracy")
plt.xlim(0.0001, 0.01)
plt.ylim(70, 100)

plt.plot(weight, bsl, linestyle='--')  # draw baseline (CE -> cRW)
plt.plot(weight, best_bsl, linestyle='-.')  # draw best baseline(LDAM-DRW)
plt.plot([0.001,], [86.50,], marker="^")
plt.plot(
    weight,
    TP_mca,
    marker="o",
    ms=1,
    label="a",
    linestyle="-",
)



plt.tick_params(labelsize=13)

plt.show()