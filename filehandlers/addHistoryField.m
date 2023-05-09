function ftdata = addHistoryField(ftdata,entry)
% Initialize history field
if ~isfield(ftdata.hdr,'history')
    ftdata.hdr.history = {};
end


histlist = strncmp(ftdata.hdr.history,entry,4);
if any(histlist)
    ftdata.hdr.history(find(histlist)) = [];
end
ftdata.hdr.history = [ftdata.hdr.history [entry ' ' date]];
