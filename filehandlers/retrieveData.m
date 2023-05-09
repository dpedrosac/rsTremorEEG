function ftdata_cat = retrieveData(R,retdat)
if ~isfield(retdat,'keeptrialinfo')
    retdat.keeptrialinfo = 'yes';
end

ip = 0;
for sub = retdat.sub
    for block = retdat.block % Block of the Experiment
        switch R.import.blockpart{block}
            case 'Task'
                for cond = retdat.cond % Condion type
                    for part = retdat.part % part of task
                        ip = ip + 1;
                        %                         fileappend = [R.epoch.names{part} '_block_pp_vc'];
                        fileappend = eval(retdat.fileapend);
                        ftdata_rep{ip} = loadExpData(R,sub{1},'Task',[],fileappend,eval(retdat.subfold));
                    end
                end
            otherwise
                ip = ip + 1;
                %             fileappend = 'pp_vc';
                fileappend = eval(retdat.fileapend);
                ftdata_rep{ip} = loadExpData(R,sub{1},R.import.blockpart{block},[],fileappend,retdat.subfold);
        end
        
    end
end

if retdat.ftflag
    repN = ip;
    % Ensure same channels (or error!)
    list = [];
    for i = 1:numel(ftdata_rep)
        if i == 1
            list  =  ftdata_rep{i}.label;
        else
            list = intersect(list, ftdata_rep{i}.label);
        end
    end
    % select common channels
    cfg = [];
    cfg.channel = list;
    ip = 0;
    for i = 1:numel(ftdata_rep)
        if isempty(ftdata_rep{i}.trial)
            warning('You are merging data that does not have valid trials!')
        else
            ip = ip+1;
            ftdata_rep{ip} = ft_selectdata(cfg,ftdata_rep{i});
        end
    end

    % remove trial info
    if strcmp(retdat.keeptrialinfo,'no')
     for i = 1:numel(ftdata_rep)
        ftdata_rep{i} = rmfield(ftdata_rep{i},'trialinfo');
     end
    end

    ftdata_cat = appendFTData(ftdata_rep,repN);
else
    ftdata_cat = [ftdata_rep{:}];
end

