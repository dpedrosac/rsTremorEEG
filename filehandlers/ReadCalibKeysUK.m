function Key = ReadCalibKeysUK(path)

%% Import data from text file
% Script for importing data from the following text file:
%
%    filename: Z:\TimWest\DATA\Data\EEG_DP_Tremor\TF9P080822\StimuliPCLocal\TF9P080822_Calibration\XKey.txt
%
% Auto-generated by MATLAB on 17-Aug-2022 12:19:36

%% Set up the Import Options and import the data
opts = delimitedTextImportOptions("NumVariables", 1);

% Specify range and delimiter
opts.DataLines = [1, Inf];
opts.Delimiter = "";

% Specify column names and types
opts.VariableNames = "VarName1";
opts.VariableTypes = "double";

% Specify file level properties
opts.ExtraColumnsRule = "ignore";
opts.EmptyLineRule = "read";

% Specify variable properties
opts = setvaropts(opts, "VarName1", "DecimalSeparator", ".");
opts = setvaropts(opts, "VarName1", "ThousandsSeparator", ",");

% Import the data
Key = table2array(readtable(path, opts));


%% Clear temporary variables
clear opts