function [] = sourceReconstruction(R)
close all
subI = 0;
for sub = R.import.subsel
    subI = subI + 1;
    for block = 1:3 % block loop
        if block<3
            prun = 1;
            condlist = 1;
        else % for task data its again subdivided
            prun = 3;
            condlist = R.import.condsel;
        end
        for cond = condlist
            for part = 1:prun
                ft = 1; % just do blocked
                if block < 3
                    fileappend = 'pp_p';
                    ftdata = loadExpData(R,sub{1},R.import.blockpart{block},[],fileappend,'epoched');
                elseif block==3
                    if ft ==1
                        fileappend = [R.epoch.names{part} '_block_pp_p'];
                        ftdata = loadExpData(R,sub{1},'Task',['Condition' num2str(cond)],fileappend,'epoched');
                    elseif ft == 2
                        fileappend = [R.epoch.names{part} '_trans_pp_p'];
                        ftdata = loadExpData(R,sub{1},'Task',['Condition' num2str(cond)],fileappend,'epoched');
                    end
                end
                
                
                
                
                
                
                
                
            end
        end
    end
end

