function ICModelCommand
display('THIS IS A BETA LEVEL UPGRADE! PLEASE DOUBLE CHECK EVERYTHING - COMPLAIN TO CAL');
display('THERE IS NO VCN INPUT AT THE MOMENT - COMPLAIN TO CAL');
display('Cal, please remember to verify all files are all updated correctly');
display('Cal! DNLL changed to ALLpass at 100sp/sec');

% display('Cal! DCN changed to ALLpass at 128sp/sec');
choices = input('IC Sustained (1) or IC Adapting (2):');

global LSOmin
global LSOpeak
global LSOmax
global shape
global shape2
global INpeak

shape = input('For custom EX shape inputs type "1"; normal runs type "0"');
if isempty(shape)
    shape = 0;
end
if shape == 1 
    LSOmin = input('EX input norm rate at 8Hz (Default = 0):');
    if isempty(LSOmin)
        LSOmin = 0;
    end
    LSOpeak = input('EX input norm rate peak freq (default = 32Hz)');
    if isempty(LSOpeak)
        LSOpeak = 32;
    end
    LSOmax = input('EX input norm rate at 256Hz (Default = 0):');
    if isempty(LSOmax)
        LSOmax = 0;
    end
end

shape2 = input('For custom IN shape inputs type "1"; normal runs type "0"'); 
if isempty(shape2)
    shape2 = 0;
end
if shape2 == 1
    INpeak = input('IN input norm rate peak freq (default = 100Hz)');
    if isempty(INpeak)
        INpeak = 100;
    end
end

if choices == 1
    cd('IC Sustained Model v3')
    ICModel2012
elseif choices == 2
    cd('IC Adapting Model v5')
    ICModel2012
else
    
end

cd ..
