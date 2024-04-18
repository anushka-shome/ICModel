function CustomRateGain(periods,numtrials,size,mempot,plas)
% periods = [3,5,7.5,10,13,15,20,25,50,100,150];
directs = input('Data Directory Name:','s');
rates = InputCharsIV;
cd(directs)
clear PerTrialSpk
clear PerVS2
clear PerRAY2
clear RayStat
clear VSstat

lincolor = {'r+-','g*-','bo-','y^-'};

load TrialSPK2

j = size;
w = 1;
k = mempot;
z = plas;
% rates = InputCharsIV;
% for z = 1:4
rategain = [];
permean = [];
perstd = [];
persterr = [];
RayStat = [];
VSstat = [];
for i = 1:length(periods);
    for g = 1:numtrials
        dummy = length(PerTrialSpk(j,1,k).data(i,z).test(g).data);
        %         set(i,z,g) = dummy/.5;
        flash(g) = dummy/.75;
    end
    permean(i) = mean(flash);
    rategain(i) = permean(i)/rates(1,i);
    %         perstd(i) = std(flash);
    %         persterr(i) = perstd(i)./(sqrt(numtrials));
    
end

%     lincols = char(lincolor(z));
figure(1)
semilogx(periods,rategain,'rx')
%     errorbar(periods,permean,persterr,lincols)
xlim([1 200])
ylim([0 3])
hold on
% end

figure(1)
ylabel('Rate Gain')
xlabel('Period (ms)')
% legend('None','PPD','Mixed','PPF');
cd ..
end

function rate = InputCharsIV
load rates_11A2.mat
rate = tot_11A2_1570um_bpam1(2:6);
end
