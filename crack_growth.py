import numpy as np
import pandas as pd
from shutil import copyfile
import sys
import os
import glob
from emery_driver import *

##############
#parameters for the crack_growth function to work properly
original_mesh_file = 'standard_channel_L10_4.inp'
retained_elems_filename = 'RETAINED_ELEMS_chamfer.txt'
init_crack_size = 0.05
previous_step = 1
steps = 9
median_step_size = 0.24
template_radius = 0.01
poly_order = 3
ex_A, ex_B = 5, 5
smoothing_method = "FIXED_ORDER_POLY"
discard_ = 0
exe = 'abaqus'
num_processors = 8
#############

df = pd.read_csv('results_batches/uncracked_results1.csv')


for root_name in df['root_name']:

#    odb_filename = load+'.odb'
    copyfile(''.join(['../inp_files/', root_name, '.inp']), ''.join([root_name, '.inp']))

    results = df[df['root_name'] == root_name]

#    crack_location = list(np.round(results[['loc_x', 'loc_y', 'loc_z']], 2).to_numpy().flatten())
    crack_location = [0.0, -2.82, 6.45]
    direction = list(results[['dir_x', 'dir_y', 'dir_z']].to_numpy().flatten())
    print(crack_location)
    print(direction)

    phi = np.arccos(direction[2])*180/np.pi
    theta = np.arctan(direction[1]/direction[0])*180/np.pi
    rotation = [int(phi), int(theta)]

    insert_and_grow_crack(root_name, retained_elems_filename, init_crack_size,
	    crack_location, rotation, previous_step, steps, median_step_size, template_radius,
	    poly_order, ex_A, ex_B, smoothing_method, discard_, exe, num_processors, initial_crack=True)

