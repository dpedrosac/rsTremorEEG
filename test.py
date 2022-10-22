
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

    # Remove bad channels, that is those unrelated to EEG; TODO: what is the problem with o9 and 010 und why not keeping EKG?!
    raw_downsampled.info['bads'].extend(['EKG', 'AccX', 'AccY', 'AccZ', 'EMG', 'SC', 'O9', 'O10'])
    good_eeg = mne.pick_types(raw_downsampled.info, meg=False, eeg=True)
    raw_downsampled.pick(good_eeg)
    montage = mne.channels.make_standard_montage('standard_1005')
    print(montage)

    # Adding sensor information
    raw_downsampled.set_montage(montage)

    # Plot Power spectrum, if necessary
    raw_downsampled.plot_psd(fmax=100)
    raw_downsampled.plot(duration=5, n_channels=30)

    # Artifact correcion; TODO a high-pass filter is recommended, which could be added here
    ica = mne.preprocessing.ICA(n_components=20, random_state=97, max_iter=800)
    ica.fit(raw_downsampled)
    ica.plot_components
    ica.plot_sources(raw_downsampled, show_scrollbars=False)
    ica.plot_overlay(raw, exclude=[17, 19], picks='eeg')

    # TODO: Remove DBS artifact if present

    # TODO: Find bad channels and interpolate them

    # TODO: re-reference to common average

    for cutoff in (0.1, 4):
        raw_highpass = raw_downsampled.copy().filter(l_freq=cutoff, h_freq=None)
        with mne.viz.use_browser_backend('matplotlib'):
            fig = raw_highpass.plot(duration=60, proj=False,
                                    n_channels=len(raw_downsampled.ch_names), remove_dc=False)
        fig.subplots_adjust(top=0.9)
        fig.suptitle('High-pass filtered at {} Hz'.format(cutoff), size='xx-large',
                     weight='bold')
    # Set montage

    # Blink artifacts
    raws = list()
    icas = list()



Hallo zusammen!
zweiter Test
Mareike 1. Test