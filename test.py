
import os
import numpy as np
import mne
from dependencies import ROOTDIR
from utils.HelperFunctions import FileOperations
import matplotlib.pyplot as plt


def countdown(n):
    """ very simple function intended to provide a countdown going form n to zero backwards """

    import time
    for count in reversed(range(1, n + 1)):
        print(count)
        time.sleep(1)
    print('Tadaaa!')


def multiplication(k=10, n=5):
    """ simple function which multiplies two values, or - in case only one is defined - one value witha  default """

    result = k*n
    return result


def load_data():
    """ loads some data according to MNE tutorial """
    data_dir = os.path.join(ROOTDIR, 'data')
    files2test = FileOperations.list_files_in_folder(inputdir=data_dir, suffix='vhdr', entire_path=True)
    dat_test = mne.io.read_raw_brainvision(files2test[0])
    print(dat_test)