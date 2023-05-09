% My Master Script
% restoredefaultpath
clear; close all
restoredefaultpath;
addpath(genpath(cd))
% setup paths
 R = analysisRSEEG_AddPaths();
 R.path.expname = 'restingstateDBS';
 R.sublist = {'rsEEG_01'};

% Name Files as follows: DBS_13_0, DBS_04_7, DBS_12_8, DBS_13_12

% 'rsEEG_01', 'rsEEG_02', 'rsEEG_03', 'rsEEG_04', 
%              'rsEEG_05', 'rsEEG_06', 'rsEEG_07', 'rsEEG_08','rsEEG_09','rsEEG_10',
%              'rsEEG_11', 'rsEEG_12', 'rsEEG_13', 'rsEEG_14','rsEEG_15','rsEEG_16',
%              'rsEEG_17', 'rsEEG_18', 'rsEEG_19', 'rsEEG_20','rsEEG_21','rsEEG_22',
%              'rsEEG_23', 'rsEEG_24', 'rsEEG_25'};

% 
% % %Load Data, reject DBS-Artefact, Notch-Filter, Resample, 
% readContinuousData(R)

% %Preprocess
eegPreprocessingMasterAC(R);


%Time-Frecuency Analysis