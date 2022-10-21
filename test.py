
import os
import numpy as np
import mne
from dependencies import ROOTDIR
from utils.HelperFunctions import FileOperations
import matplotlib.pyplot as plt
from mne.preprocessing import (ICA, create_eog_epochs, create_ecg_epochs,
                               corrmap)

def countdown(n=10):
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


def load_and_preprocess_data():
    """ loads some data according to MNE tutorial """
    data_dir = os.path.join(ROOTDIR, 'data')
    files2test = FileOperations.list_files_in_folder(inputdir=data_dir, suffix='vhdr', entire_path=True)
    raw =  mne.io.read_raw_brainvision(files2test[0], preload=True, verbose=True)
    raw.info['line_freq'] = 50
    raw_downsampled = raw.copy().resample(sfreq=200)
    raw_downsampled2 = raw.copy().resample(sfreq=100)

    for cutoff in (0.1, 4):
        raw_highpass = raw_downsampled.copy().filter(l_freq=cutoff, h_freq=None)
        with mne.viz.use_browser_backend('matplotlib'):
            fig = raw_highpass.plot(duration=60, proj=False,
                                    n_channels=len(raw_downsampled.ch_names), remove_dc=False)
        fig.subplots_adjust(top=0.9)
        fig.suptitle('High-pass filtered at {} Hz'.format(cutoff), size='xx-large',
                     weight='bold')
    # Set montage
    montage = mne.channels.make_standard_montage('standard_1005')
    # raw.set_montage(montage, verbose=True)

    # Blink artifacts
    raws = list()
    icas = list()

    for subj in range(4):
        # EEGBCI subjects are 1-indexed; run 3 is a left/right hand movement task
        fname = mne.datasets.eegbci.load_data(subj + 1, runs=[3])[0]
        raw = mne.io.read_raw_edf(fname).load_data().resample(50)
        # remove trailing `.` from channel names so we can set montage
        mne.datasets.eegbci.standardize(raw)
        raw.set_montage('standard_1005')
        # high-pass filter
        raw_filt = raw.copy().load_data().filter(l_freq=1., h_freq=None)
        # fit ICA, using low max_iter for speed
        ica = ICA(n_components=30, max_iter=100, random_state=97)
        ica.fit(raw_filt, verbose='error')
        raws.append(raw)
        icas.append(ica)

    raw.set_eeg_reference('average', projection=False, verbose=False)
    #neuercomment