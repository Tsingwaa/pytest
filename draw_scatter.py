from tkinter.tix import CELL
from webbrowser import get
from xml.sax.handler import feature_external_ges
import numpy as np
import pickle
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = "Times New Roman"

# CE
CE_train_pk_fpath = "./h5files/Skin7_r50pre_CE/last_visual_train_features_labels.pickle"
CE_test_pk_fpath = "./h5files/Skin7_r50pre_CE/last_visual_test_features_labels.pickle"

# CE_CT
CT_train_pk_fpath = "./h5files/Skin7_r50pre_CE_CT_lmd0.07/last_visual_train_features_labels.pickle"
CT_test_pk_fpath = "./h5files/Skin7_r50pre_CE_CT_lmd0.07/last_visual_test_features_labels.pickle"

# CE_TP
TP_train_pk_fpath = "./h5files/Skin7_r50pre_CE_TP_lmd0.03/last_visual_train_features_labels.pickle"
TP_test_pk_fpath = "./h5files/Skin7_r50pre_CE_TP_lmd0.03/last_visual_test_features_labels.pickle"

# CE_SC
SC_train_pk_fpath = "./h5files/Skin7_r50pre_CE_supcon_lmd1.0/last_visual_train_features_labels.pickle"
SC_test_pk_fpath = "./h5files/Skin7_r50pre_CE_supcon_lmd1.0/last_visual_test_features_labels.pickle"

def get_feat_label(pk_fpath):
    with open(pk_fpath, 'rb') as f:
        pk = pickle.load(f)
        features = pk["features"]
        labels = pk["labels"]
    return features, labels

CE_train_features, CE_train_labels = get_feat_label(CE_train_pk_fpath)
CE_test_features, CE_test_labels = get_feat_label(CE_test_pk_fpath)
CT_train_features, CT_train_labels = get_feat_label(CT_train_pk_fpath)
CT_test_features, CT_test_labels = get_feat_label(CT_test_pk_fpath)
TP_train_features, TP_train_labels = get_feat_label(TP_train_pk_fpath)
TP_test_features, TP_test_labels = get_feat_label(TP_test_pk_fpath)
SC_train_features, SC_train_labels = get_feat_label(SC_train_pk_fpath)
SC_test_features, SC_test_labels = get_feat_label(SC_test_pk_fpath)

# matplotlib
fig = plt.figure(figsize=(8, 3.5))

plt.subplot(1, 2, 1)
s1=plt.scatter(CE_train_features[:, 0], CE_train_features[:, 1], c=CE_train_labels, s=5)
# plt.title("CE Trainset")
# plt.legend(*s1.legend_elements(), loc="best")
plt.xticks([])
plt.yticks([])
# plt.subplot(4, 2, 2)
# s5=plt.scatter(CE_test_features[:, 0], CE_test_features[:, 1], c=CE_test_labels, s=5)
# plt.legend(*s5.legend_elements())
# plt.title("CE testset")
# plt.xticks([])
# plt.yticks([])
# plt.subplot(4, 2, 3)
# s2=plt.scatter(CT_train_features[:, 0], CT_train_features[:, 1], c=CT_train_labels, s=5)
# plt.legend(*s2.legend_elements())
# plt.title("CE+CT trainset")
# plt.xticks([])
# plt.yticks([])
# plt.subplot(4, 2, 4)
# s6=plt.scatter(CT_test_features[:, 0], CT_test_features[:, 1], c=CT_test_labels, s=5)
# plt.legend(*s6.legend_elements())
# plt.title("CE+CT testset")
# plt.xticks([])
# plt.yticks([])

plt.subplot(1, 2, 2)
# plt.subplot(4, 2, 5)
s3=plt.scatter(TP_train_features[:, 0], TP_train_features[:, 1], c=TP_train_labels, s=5)
# box = s3.get_position()
# s3.set_position([box.x0, box.y0, box.width, box.height * 0.8])
plt.legend(*s3.legend_elements(), loc="lower right", ncol=7, bbox_to_anchor=(0.75, -0.16), handlelength=1, columnspacing=3)
# plt.title("CE+TP Trainset")
plt.xticks([])
plt.yticks([])
# plt.subplot(4, 2, 6)
# s7=plt.scatter(TP_test_features[:, 0], TP_test_features[:, 1], c=TP_test_labels, s=5)
# plt.legend(*s7.legend_elements())
# plt.title("CE+TP testset")
# plt.xticks([])
# plt.yticks([])
# plt.subplot(4, 2, 7)
# s4=plt.scatter(SC_train_features[:, 0], SC_train_features[:, 1], c=SC_train_labels, s=5)
# plt.legend(*s4.legend_elements())
# plt.title("CE+SC trainset")
# plt.xticks([])
# plt.yticks([])
# plt.subplot(4, 2, 8)
# s8=plt.scatter(SC_test_features[:, 0], SC_test_features[:, 1], c=SC_test_labels, s=5)
# plt.legend(*s8.legend_elements())
# plt.title("CE+SC testset")
# plt.xticks([])
# plt.yticks([])

plt.savefig(fname='visualization_CEvsCE_TP_v4.pdf')

plt.show()