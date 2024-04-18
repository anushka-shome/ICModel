function NEWRateGainPlots(EXins,INins,numtrials,mempot)
freq = [8,16,32,64,128,256,512,1024];
% directs = input('Data Directory Name:','s');
% numtrials = input('Number of Trials:');


% cd(directs)
clear PerTrialSpk
clear PerVS2
clear PerRAY2
clear RayStat
clear VSstat

% lincolor = {'r+-','g*-','bo-','y^-'};

load TrialSPK2

z = 1;
k = mempot;
% z = 2;
% EXins(p,i,z).no = B;
% INins(p,i,z).no = C;
for i = 1:length(freq);
    
    for g = 1:numtrials
        numE = size(EXins(i,g,z).no,2);
        for oh = 1:numE
            dummy2 = length(EXins(i,g,z).no(oh).test);
            set2(oh) = dummy2/.750;
        end
        idRAWe(g) = mean(set2);
        numI = size(INins(i,g,z).no,2);
        for oh = 1:numI
            dummy3 = length(INins(i,g,z).no(oh).test);
            set3(oh) = dummy3/.750;
        end
        idRAWi(g) = mean(set3);
        
    end
    ratesE(i) = mean(idRAWe);
    ratesI(i) = mean(idRAWi);
end
for i = 1:length(freq);
    
    for g = 1:numtrials
        
        dummy = length(PerTrialSpk(i,z,k).test(g).data);
        %         set(i,z,g) = dummy/.5;
        flash(g) = dummy/.75;
        
        permean(i) = mean(flash);
        rategainE(i) = permean(i)/ratesE(i);
        rategainI(i) = permean(i)/ratesI(i);
        

        
    end
end
nfig = figure(1)
semilogx(freq,rategainE,'bo-')
hold on
semilogx(freq,rategainI,'r+-')
%     errorbar(freq,permean,persterr,lincols)
xlim([1 1100])
ylim([0 3])

ylabel('Rate Gain')
xlabel('Period (ms)')
saveas(nfig,'ICRateGains.fig','fig')
% cd ..
end



