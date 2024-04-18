function IC2012RateVSColorPlots

choices = input('IC Sustained (1) or IC Adapting (2):');

if choices == 1
    cd('IC Sustained Model v2')
    SustainedRateVSColorPlots2012
elseif choices == 2
    cd('IC Adapting Model v4')
    AdaptingRateVSColorPlots2012
else
    
end

cd ..
