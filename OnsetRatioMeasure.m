function [MeanOnsetRatio,OnsetRatioStErr] = OnsetRatioMeasure(numtrials)
clear PerTrialSpk
load TrialSPK2
freq = [8,16,32,64,128,256,512,1024];
k = 5;
z = 1;
for i = 1:length(freq)
    for g = 1:numtrials
        dummy1(g) = length(PerTrialSpk(i,z,k).test(g).data <= 350);
        rateOns(g) = dummy1(g)/.150;
        dummy2(g) = length(PerTrialSpk(i,z,k).test(g).data > 350);
        rateSus(g) = dummy2(g)/.600;
        OnsetRatio(g) = (rateOns - rateSus)./(rateOns + rateSus);
    end
    MeanOnsetRatio(i) = mean(OnsetRatio);
    OnsetRatioStDev(i) = std(OnsetRatio);
    OnsetRatioStErr(i) = OnsetRatioStDev(i)/sqrt(numtrials);
end

op = figure;
errorbar(freq,MeanOnsetRatio,OnsetRatioStErr)
xlabel('Modulation Freq')
xlim([0 1024])
ylim([-1 1])
ylabel('Vector Strength')

saveas(op,'ICOnsRat.fig','fig')





