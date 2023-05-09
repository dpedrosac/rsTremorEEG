function [object,pathsave] = loadExpData(R,sub,seshname,subfold,ext)
% This function will load in data for the analysis
% It has the path format - root\experimentName\session\
fileset = [sub];
if ~isempty(seshname)
    fileset = [fileset '_' seshname];
end
root = [R.path.datapath '\' R.path.expname '\' sub ...
    '\Fieldtrip\' fileset '\' subfold '\'];
% mkdir(root)
pathsave = [root fileset '_' ext];
object = load(pathsave,'target');
object = object.target;