#ex.) > python ~/DLC/convH5.py '.' 'OK'
#
import os
import re
import pandas as pd
import scipy.io as scio
import numpy as np
import argparse

def convDLC2mat(path_h5file, DLCName0):
    Dataframe = pd.read_hdf(path_h5file)
    scorer = Dataframe.columns.get_level_values(0)[0]
    bodyparts = Dataframe.columns.get_level_values(1).unique()

    xydims = []
    for bp in bodyparts:
        xydims.extend([Dataframe[scorer][bp]['x'], Dataframe[scorer][bp]['y']])

    xydims = np.vstack(xydims)

    # Extract the numeric part from the file name
    filename = os.path.basename(path_h5file)
    match = re.search(r'(\d{8}_\d+)', filename.split(DLCName0)[0])

    if match:
        numeric_part = match.group()
    else:
        numeric_part = 'unknown'
        
    #    print(numeric_part)

    path_matfile = os.path.join(os.path.dirname(path_h5file), numeric_part + '.mat')
    scio.savemat(path_matfile, {'xydims': xydims})
    print(path_matfile)

def find_and_convert_h5(root_path, target_dir, DLCName0):
    for curDir, _, files in os.walk(root_path):
        rel_path = os.path.relpath(curDir, root_path)
        if target_dir not in rel_path.split(os.path.sep):
            continue  # Skip if target_dir is not in the path

        for file in files:
            if file.endswith(".h5"):
                convDLC2mat(os.path.join(curDir, file), DLCName0)

def main():
    parser = argparse.ArgumentParser(description='Process .h5 files in a specific directory.')
    parser.add_argument('root_videodir', type=str, help='Root directory to search within')
    parser.add_argument('target_dir', type=str, help='Specific subdirectory to process')
    args = parser.parse_args()

    DLCName0 = 'DLC'
    find_and_convert_h5(os.path.join(os.getcwd(), args.root_videodir), args.target_dir, DLCName0)

if __name__ == '__main__':
    main()


