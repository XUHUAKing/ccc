import numpy as np
from functions import get_scaled_training_and_testing_data

tfeature_file = "../data/training_data_feature.csv"
sfeature_file = "../data/testining_data_feature.csv"

tfeature = np.zeros((3000, 11))
#sfeature = np.zeros(100000, 11)

# 0.(normalization)
tdata, ttarget, tlabel, sdata, starget = get_scaled_training_and_testing_data()

# 1.(x.max-x.min)/(t.max-t.min)
# 2.终点x离目标x距离
# 3.x.max-x.min
tdata_x = np.delete(tdata, [1,2], axis=2)
t_data_delta_x = np.max(tdata_x, axis=1) - np.min(tdata_x, axis=1)
tfeature[:, 2] = t_data_delta_x.reshape((1,3000))
# 4.|x-x0|^2
# 5.|xi-xi+1|/|ti-ti+1|
# 5.|xi-xi+1|/|ti-ti+1|^2
# 6.停的次数:
# 7.停时有无波动:
# 8.折返距离:
# 9.光滑度
# 9.光滑度方差
# 10.在x<x0时x不变的所有t的总和
# 11.t