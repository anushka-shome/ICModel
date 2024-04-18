function RateGainPlots(numtrials,mempot)
freq = [8,16,32,64,128,256,512,1024];
directs = input('Data Directory Name:','s');
% numtrials = input('Number of Trials:');
Etype = input('Excitatory Inputs - 1) MSO, 2) DCN (Default = 2) 3) LSO: ');
if isempty(Etype)
    Etype = 2;
end

numE = input('Number of EX inputs (Default = 2):');
if isempty(numE)
    numE = 2;
end

Itype = input('Inhibitory Inputs - 1)DNLL, 2)VNLL (Default = DNLL):');
if isempty(Itype)
    Itype = 1;
end

numINs = input('Number of IN inputs (Default = 3):');
if isempty(numINs)
    numINs = 3;
end

delays = input('IN input lag (ms) Default 3ms:');
if isempty(delays)
    delays = 3;
end

cd(directs)
clear PerTrialSpk
clear PerVS2
clear PerRAY2
clear RayStat
clear VSstat

lincolor = {'r+-','g*-','bo-','y^-'};

load TrialSPK2

z = 1;
k = mempot;
% z = 2;
ratesEx = InputCharsII(numtrials,numE);

    for i = 1:length(freq);
        for g = 1:numtrials
            dummy = length(PerTrialSpk(i,z,k).test(g).data);
            %         set(i,z,g) = dummy/.5;
            flash(g) = dummy/.5;
        end
        permean(i) = mean(flash);
        rategain(i) = permean(i)/rates(1,i);
%         perstd(i) = std(flash);
%         persterr(i) = perstd(i)./(sqrt(numtrials));
        
    end

    lincols = char(lincolor(z));
    figure(1)
    semilogx(freq,rategain,lincols)
%     errorbar(freq,permean,persterr,lincols)
    xlim([1 200])
    ylim([0 3])
    hold on

figure(1)
ylabel('Rate Gain')
xlabel('Period (ms)')
legend('None','PPD','Mixed','PPF');
cd ..

end

function rate = InputCharsII(numtrials,numinputs)
freq = [8,16,32,64,128,256,512,1024];
% directs = input('Data Directory?:','s');
% cd(directs)
for z = 1:length(freq)
    for o = 1:numinputs
        o;
        inputdataR = [];
        for foo = 1:numtrials
            
            
            
            foo;
            inputdataRAW = [];
            period = freq(z);
            str0 = 'ICTestData\';
            strB = num2str(period);
            str1 = '_Period_';
            strinput = num2str(o);
            stroo = '_RunTrial';
            str2 = '.dat';
            stc = num2str(foo);
            fnames = strcat(str0,strB,str1,strinput,stroo,stc,str2);
            
            inputdataRAW = importdata(fnames,'\t');
            inputdataR = cat(1,inputdataR,inputdataRAW);
            
            T = period;
            stim_dur = 500;
            
        end
        totals = length(inputdataR);
        totalinput(o,z) = length(inputdataR);
        rate(o,z) = (totalinput(o,z)/numtrials)/(stim_dur/1000);
    end
end
figure(4)
for o = 1:numinputs
    plot(freq,rate(o,:))
    hold on
end
end
