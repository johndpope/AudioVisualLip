import numpy as np
import argparse
from glob import glob
import os

def load_args(default_config=None):
    parser = argparse.ArgumentParser(description='Lipreading Pre-processing')
    # -- utils
    parser.add_argument('--video-direc', default='/datasets3/voxceleb2/lip/dev/', help='landmark directory')
    parser.add_argument('--video-list', default='/data/liumeng/Lipreading_using_Temporal_Convolutional_Networks/preprocessing/voxceleb2/videolist', help='mean face pathname')

    args = parser.parse_args()
    return args

args = load_args()

pattern = args.video_direc + "/*/*/*.npz"
filelist = sorted(glob(pattern))

with open(args.video_list, 'w') as w:
    for filepath in filelist:
        no = filepath.split('.')[0]
        spk = no.split('/')[-3]
        session = no.split('/')[-2]
        fn = no.split('/')[-1]
        w.write(os.path.join(spk,session,fn)+'\n')
w.close()
