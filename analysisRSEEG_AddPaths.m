function R = analysisRSEEG_AddPaths(R)
switch getenv('computername')
    case 'LAPTOP-6JVM9STC'
        R.path.ftpath = 'C:\Users\alexa\Downloads\fieldtrip-20230328\fieldtrip-20230328';
        R.path.datapath = 'C:\Users\alexa\OneDrive\Dokumente\rsEEG';
%         R.path.datapath.dbsrejected = 'C:\Users\alexa\Downloads\EEG_Test\restingstateDBS';
end

addpath(R.path.ftpath); ft_defaults();