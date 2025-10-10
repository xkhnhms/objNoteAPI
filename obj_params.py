# dict of {objname: (sample_voxel_size, model_voxel_size, model_num_sample, pipe_longit_dept)}
configs = {
           # objects
           '000': (0.004, 0.001, 10000, 0.016),
           '001': (0.003, 0.001, 10000, 0.016),
           '002': (0.004, 0.00001, 10000, 0.008),
           '003': (0.005, 0.00001, 10000, 0.008),
           '004': (0.004, 0.00001, 10000, 0.016),
           '005': (0.004, 0.00001, 10000, 0.009),
           '006': (0.005, 0.00001, 10000, 0.012),
           '007': (0.005, 0.00001, 10000, 0.014),
           '008': (0.006, 0.00001, 10000, 0.007),
           '009': (0.003, 0.00001, 10000, 0.012),
           '010': (0.006, 0.00001, 10000, 0.006),
           '011': (0.005, 0.00001, 10000, 0.012),
           '012': (0.007, 0.00001, 10000, 0.006),
           '013': (0.006, 0.00001, 10000, 0.006),
           }

params = {
   'model_dir': 'grasp_dataset/models',
   'save_path': 'grasp_dataset/grasp_label',
   'config_yaml_path': 'config.yaml',
   'voxel_down_min_points': 1400,
   'V': 300,
   'A': 12,
   'H': 0.02,
   'depth_base': 0.02,
   'collision_thresh': 0.01,
   'lr_gap_thresh': 0.004,
   'depth_gap_thresh': 0.004,
   'depth_list': [0.008, 0.01, 0.015, 0.02], 
   'width_list': [0.005 * x for x in range(1, 16, 1)],
   'pool_size': 50,
   'use_depth_gap_thresh': True
}

