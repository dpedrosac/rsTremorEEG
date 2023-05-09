function pathsave = saveExpData(R,sub,seshname,subfold,ext,target)

% % if isfield(target,'fsample')
% %     checkHeader(target)
% % end

fileset = [sub];
if ~isempty(seshname)
    fileset = [fileset '_' seshname];
end

root = [R.path.datapath '\' R.path.expname '\' sub ...
    '\Fieldtrip\' fileset '\' subfold '\'];
mkdir(root)
pathsave = [root fileset '_' ext];
if ~isempty(target); %allows to just recover path
    s = whos('target');
    if (s.bytes/1e9) < 2
        save(pathsave,'target')
    else
        warning('Using v7.3 save, this can be very slow!')
        save(pathsave,'target','-v7.3')
    end
end