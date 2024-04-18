
modfreq=[8 16 32 64 128 256 512 1024];
peak=32;
ratelist = abs(log2(peak./modfreq));
% rats = power(2,ratelist);
rats = power(2,ratelist/2);
rates = 1./rats;
scale=80;
% scale = input('Enter Max Peak Rate (Sp/Sec):');
% if isempty(scale)
%     scale = 100;
% end
% % scale = 100;
rates = scale.*rates;

semilogx(modfreq,rates,'bo-')