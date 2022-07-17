#!/usr/bin/env python
# -*- coding: utf-8 -*-

import glob
import os
import re
from itertools import groupby
from operator import itemgetter
from dependencies import ROOTDIR, GITHUB


class LittleHelpers:
    def __init__(self, _debug=False):
        self.debug = _debug


class Output:
    def __init__(self, _debug=False):
        self.debug = _debug

    @staticmethod
    def printProgressBar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='█', printEnd="\r"):
        """ copied from: https://stackoverflow.com/questions/3173320/text-progress-bar-in-the-console
        Call in a loop to create terminal progress bar
        @params:
            iteration   - Required  : current iteration (Int)
            total       - Required  : total iterations (Int)
            prefix      - Optional  : prefix string (Str)
            suffix      - Optional  : suffix string (Str)
            decimals    - Optional  : positive number of decimals in percent complete (Int)
            length      - Optional  : character length of bar (Int)
            fill        - Optional  : bar fill character (Str)
            printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
        """
        percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
        filledLength = int(length * iteration // total)
        bar = fill * filledLength + '-' * (length - filledLength)
        print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end=printEnd)

        # Print New Line on Complete
        if iteration == total:
            print()

    @staticmethod
    def split_lines(text):
        lines = text.split('\n')
        regex = re.compile(r'.{1,130}(?:\s+|$)')
        return '\n'.join(s.rstrip() for line in lines for s in regex.findall(line))


class FileOperations:
    def __init__(self, _debug=False):
        self.debug = _debug

    @staticmethod
    def create_folder(foldername):
        """creates folder if not existent"""

        if not os.path.isdir(foldername):
            os.mkdir(foldername)

    @staticmethod
    def list_folders(inputdir, prefix='subj', files2lookfor='NIFTI'):
        """takes folder and lists all available subjects in this folder according to some filter given as [prefix]"""

        list_all = [name for name in os.listdir(inputdir)
                    if (os.path.isdir(os.path.join(inputdir, name)) and prefix in name)]

        if list_all == '':
            list_subj = 'No available subjects, please make sure {}-files are present and correct ' \
                        '"prefix" is given'.format(files2lookfor)
        else:
            list_subj = set(list_all)

        return list_subj

    @staticmethod
    def return_full_filename(inputdir, filename):
        """returns the entire path if only a filename is known"""
        filename_complete = glob.glob(inputdir + '/*/{}'.format(filename))

        return filename_complete[0]

    @staticmethod
    def list_files_in_folder(inputdir, contains='', suffix='nii', entire_path=False, subfolders=True):
        """returns a list of files within a folder (including subfolders"""

        if subfolders:
            allfiles_in_folder = glob.glob(os.path.join(inputdir + '/**/*.' + suffix), recursive=True)
        else:
            allfiles_in_folder = glob.glob(inputdir + '/*.' + suffix)

        if not contains:
            filelist = [file_id for file_id in allfiles_in_folder]
        else:
            filelist = [file_id for file_id in allfiles_in_folder if any(y in file_id for y in contains)]

        if not entire_path:
            filelist = [os.path.split(x)[1] for x in filelist]

        return filelist

    @staticmethod
    def get_filelist_as_tuple(inputdir, subjects):
        """create a list of all available files in a folder and returns tuple together with the name of subject"""

        allfiles = []
        [allfiles.extend(
            zip(glob.glob(os.path.join(inputdir, x + "/*")), [x] * len(glob.glob(os.path.join(inputdir, x + "/*")))))
            for x in subjects]

        return allfiles

    @staticmethod
    def inner_join(a, b):
        """from: https://stackoverflow.com/questions/31887447/how-do-i-merge-two-lists-of-tuples-based-on-a-key"""

        L = a + b
        L.sort(key=itemgetter(1))  # sort by the first column
        for _, group in groupby(L, itemgetter(1)):
            row_a, row_b = next(group), next(group, None)
            if row_b is not None:  # join
                yield row_b[0:1] + row_a  # cut 1st column from 2nd row
