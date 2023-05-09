function readContinuousData(R)
for sub = R.sublist
    for session = 0:16 % remember to start at 0!
        seshname = ['session' num2str(session)];
        eegpath = [R.path.datapath '\' sub{1} '\DBS_01_' num2str(session) '.eeg'];
%       hdrpath = [R.path.datapath '\' sub{1} '\DBS_11_' num2str(session) '.vhdr'];
        
        % Say if DBS is on or not
        if session == 0
            stimflag = 0;
        else
            stimflag = 1;
        end
        data_DBSrejected = read_clean_data_v2(eegpath,stimflag);
        saveExpData(R,sub{1},seshname,seshname,'dbsrejected',data_DBSrejected)
    end
end
% %         %For figures
% %         figure_params_gen(R, data_DBSrejected)
% % 
% %         %Plot DBS-artefact rejection filter
% %         plot_DBS_rejected(R, data_DBSrejected)
% 
%         % Now preprocess!
%         data_pp = eegPreprocessingMasterAC(R,data_DBSrejected);
% 
%         saveExpData(R,sub{1},seshname,seshname,'pp',data_pp)