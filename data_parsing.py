import os
import sys
import xarray
import pandas as pd
import numpy as np
import h5py
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("path", help="path to the folder \'TC_data\'", default="../TC_data")
parser.add_argument("output", help="path to the output hdf5 file", default="TCIR.h5")
args = parser.parse_args()

DataSets = ["0211_WPACout", "0212_EPACout", "0213_ATLNout"]

data_info = pd.DataFrame(columns = ["data_set", "ID", "lon", "lat", "time", "Vmax", "R35_4qAVG", "MSLP"])
data_matrix = []

for data_set in DataSets:
	print("Processing data set: %s" % data_set)
	set_path = os.path.join(args.path, data_set)
	Cyclones = sorted([entry for entry in os.listdir(set_path) if os.path.isdir(os.path.join(set_path, entry))])
	cyclones_num = len(Cyclones)
	count = 0
	for cyclone in Cyclones:
		cyclone_path = os.path.join(set_path, cyclone)
		Frames = os.listdir(cyclone_path)
		count += 1
		sys.stdout.write("......%s  (%d/%d)\r" % (cyclone, count, cyclones_num))
		sys.stdout.flush()
		for frame in Frames:
			frame_path = os.path.join(cyclone_path, frame)
			frame_data = xarray.open_dataset(frame_path)
			frame_info = pd.Series(frame_data.attrs)
			frame_info.index = ["ID", "lon", "lat", "time", "Vmax", "R35_4qAVG", "MSLP"]
			frame_info["data_set"] = data_set
			data_info.loc[data_info.shape[0]] = frame_info
			# transfer 201*201 data matrix into numpy ndarray
			data_matrix.append(frame_data.to_array().values.transpose([1, 2, 0]))
	print("done")

#=======store data=========
data_matrix = np.stack(data_matrix)
f = h5py.File(args.output,'w')
f['matrix'] = data_matrix
f.close()
data_info.to_hdf(args.output, "info")
